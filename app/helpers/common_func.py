import json
from typing import Tuple
import requests
import logging
from utils import webex_api_url
from datetime import datetime


logger = logging.getLogger(__name__)


def get_approved_user() -> list:

    return ["approved_user1", "approved_user2"]


def get_jira_user_id() -> dict:

    lookup_dict = {
        "approved_user1": ("jira_team_id1", "jira_acc_id1", "rtb_epic_id1"),
    }
    return lookup_dict


def get_user_deatil_from_email(lookup_dict: dict, email: str) -> Tuple[str, str, str]:
    return lookup_dict.get(email, (None, None, None))


def extract_json_string(s: str) -> dict:
    start_index = s.index("{")
    end_index = s.rindex("}") + 1
    json_str = s[start_index:end_index]
    json_str = json_str.replace("\n", " ")
    json_dict = json.loads(json_str)

    return json_dict


def send_bot_md_msg(bot_token: str, space_id: str, md_msg: str):
    """A starting message to webex space at the beginning"""
    webex_headers = {
        "Authorization": f"Bearer {bot_token}",
        "content-type": "application/json",
    }

    # To construct a card message
    payload = {
        "roomId": space_id,
        "markdown": "Webex is up and running",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "body": [
                        {
                            "type": "ColumnSet",
                            "columns": [
                                {
                                    "type": "Column",
                                    "items": [
                                        {
                                            "type": "TextBlock",
                                            "text": f"{md_msg}",
                                            "color": "Accent",
                                            "fontType": "Default",
                                            "size": "Large",
                                        },
                                        {
                                            "type": "TextBlock",
                                            "text": datetime.today().strftime(
                                                "%Y-%m-%d %a  %H:%M:%S"
                                            ),
                                            "wrap": True,
                                        },
                                    ],
                                    "width": "stretch",
                                }
                            ],
                        }
                    ],
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "version": "1.2",
                },
            }
        ],
    }

    try:
        requests.request(
            "POST", webex_api_url, headers=webex_headers, data=json.dumps(payload)
        )

        logging.info("Starting message sent to space")

    except requests.exceptions.RequestException as e:
        logger.exception("Requests error occurred with Webex api")
        raise SystemExit(e)
