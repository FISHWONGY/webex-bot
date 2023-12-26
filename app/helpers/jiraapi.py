from typing import Optional, Union
import re
import requests
from requests.auth import HTTPBasicAuth
from utils import (
    jira_email,
    jira_token,
    jira_api_url,
    jira_project_key,
    jira_field1,
    jira_field2,
    jira_field3,
)
import logging

logger = logging.getLogger(__name__)


def get_jira_story_details(
    output_dict: dict,
    team_id: str,
    account_id: str,
    epic_id: str,
    sp: Optional[Union[str, int]] = None,
):
    if sp is not None and sp != "":
        try:
            sp = int(sp)
        except ValueError:
            raise ValueError("Parameter 'sp' must be an integer or not provided.")

    payload = {
        "fields": {
            "project": {"key": jira_project_key},
            "summary": output_dict["title"],
            "description": output_dict["description"],
            "customfield_10038": output_dict["acceptance_criteria"],
            "issuetype": {"name": "Story"},
            "assignee": {"accountId": account_id},
            jira_field1: {"id": team_id},
            jira_field2: epic_id,
        }
    }

    if sp is not None:
        payload["fields"][jira_field3] = sp

    return payload


def write_jira_story(payload: dict):
    response = requests.post(
        jira_api_url,
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth(jira_email, jira_token),
        json=payload,
    )

    if response.status_code == 201:
        logging.info(f"Successfully created story")
    else:
        logging.info(f"Failed to create story. Error: {response.json()}")


def parse_role(role: str) -> str:
    role = role.lower()
    if role == "#de":
        return "data engineer"
    elif role == "#da":
        return "data analyst"
    else:
        raise ValueError


def extract_value(pattern: str, message: str):
    match = re.search(pattern, message)
    return match.group(1) if match else None

