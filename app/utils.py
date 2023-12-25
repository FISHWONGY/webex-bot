import openai
from os import getenv
from dotenv import load_dotenv

load_dotenv("develop.env")

openai.api_base = getenv("openai_api_url")
openai.api_type = "azure"
openai.api_version = "2023-08-01-preview"
OPENAI_CLIENT_ID = getenv("client_id")
OPENAI_CLIENT_SECRET: str = getenv("client_secret")
OPENAI_API_KEY: str = getenv("api_key")

webex_api_url = getenv("webex_api_url")
webex_token: str = getenv("webex_token")
webex_space_id: str = getenv("webex_space_id")

jira_email: str = getenv("api_user")
jira_token: str = getenv("api_token")
jira_api_url: str = getenv("jira_api_url")

jira_project_key: str = getenv("project_key")
jira_field1: str = getenv("field1")
jira_field2: str = getenv("field2")
jira_field3: str = getenv("field3")
