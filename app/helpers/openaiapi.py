from prompts import *

from utils import *
import time
import base64
import requests
from typing import Optional
from openai import AzureOpenAI



class OpenAIClient:
    client = None
    lock = threading.Lock()

    @staticmethod
    def refresh_token():
        while True:
            with OpenAIClient.lock:
                url = "url/oauth2/default/v1/token"
                payload = "grant_type=client_credentials"
                value = base64.b64encode(
                    f"{OPENAI_CLIENT_ID}:{OPENAI_CLIENT_SECRET}".encode("utf-8")
                ).decode("utf-8")
                headers = {
                    "Accept": "*/*",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Authorization": f"Basic {value}",
                }

                token_response = requests.request(
                    "POST", url, headers=headers, data=payload
                )

                OpenAIClient.client = AzureOpenAI(
                    azure_endpoint="https://azure-endpoint.com",
                    api_key=token_response.json()["access_token"],
                    api_version="2023-08-01-preview",
                )
                logging.info("Client refreshed.")
            time.sleep(3500)



def construct_formatter_prompt(query: str) -> list:
    system_prompt = f"{MY_PROMPT}"
    q = f"""{query}"""
    user_prompt = f"""Good job, let's keep it going!\nRemember the pattern is comma in front of names (CTE & column names), all query functions and column names nedded to be capitalised.\nHere is the next query that needs to be reformatted: \n'{q}'\n"""

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": MY_PROMPT},
        {"role": "assistant", "content": MY_PROMPT},
        {"role": "user", "content": MY_PROMPT},
        {"role": "assistant", "content": MY_PROMPT},
        {"role": "user", "content": MY_PROMPT},
        {"role": "assistant", "content": MY_PROMPT},
        {"role": "user", "content": user_prompt},
    ]


def construct_sf_prompt(
    query: str, error: Optional[str] = None, comment: Optional[str] = None
) -> list:
    q = f"""{query}"""
    if error is not None:
        e = f"""{error}"""
        user_prompt = (
            f"""When I run the below in snowflake '{q}',\n I got the error '{e}'."""
        )
        system_prompt = f"{MY_PROMPT}"

        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    else:
        if comment is None:
            c = "query should use only CTE instead of subquery when producing the query, always try to use the GROUP BY and HAVING functions instead of WINDOW function or the QUALIFY function, if there is a date related column in the query, always aim to use the WHERE clause to filter as early as possible for better performance."
        else:
            c = f"""{comment}"""
        user_prompt = f"""Good job, that is what we want, let's keep it going!\nRemember the pattern from above, you MUST start your answer with 'Certainly! Here's your optimized SQL query <with optimisation details if you have any>:\n\n'\nThe below query in snowflake runs very slow '{q}', In order to optimise the snowflake query, '{c}'."""
        system_prompt = f"{OPT_PROMPT}"

        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": MY_PROMPT},
            {"role": "assistant", "content": MY_PROMPT},
            {"role": "user", "content": MY_PROMPT},
            {"role": "assistant", "content": MY_PROMPT},
            {"role": "user", "content": MY_PROMPT},
            {"role": "assistant", "content": MY_PROMPT},
            {"role": "user", "content": MY_PROMPT},
            {"role": "assistant", "content": MY_PROMPT},
            {"role": "user", "content": user_prompt},
        ]


def construct_code_help_prompt(lang: str, content: str) -> list:
    c = f"""{content}"""
    user_prompt = f"""Please help me on the below {lang} question.\nIf your answer includes {lang} code, please send it in the markdown format, example ``` <code> ```.\n\nThis is my question "{c}".\n"""
    system_prompt = MY_PROMPT.format(prog_lang=lang)

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def construct_jira_prompt(role: str, title: str) -> list:
    user_prompt = f"""I am a {role}, please help me complete my jira story's description and acceptance_criteria with my jira story title - "{title}".\n\nHere is the how you should reply:\n\n{{\n\n"title": "{title}",\n\n"description": "As a {role}, I want to <action based on title>, so that <outcome based on title and the action of the sentence>",\n\n"acceptance_criteria": "<acceptance criteria based on title and description>"\n\n}}\n\n"""

    system_prompt = MY_PROMPT.format(role=role)

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def chat_response(msg_list: list) -> str:
    with OpenAIClient.lock:
        client = OpenAIClient.client

    response = client.chat.completions.create(
        model="gpt-35-turbo",
        messages=msg_list,
        user=f'{{"appkey": "{OPENAI_API_KEY}"}}',
    )

    output = response.choices[0].message.content

    return f"<blockquote class=info>{output}\n\n---END---</blockquote>"
