from webex_bot.webex_bot import WebexBot
from bot_commands import *
from utils import webex_token, webex_space_id
import threading
import logging

logger = logging.getLogger(__name__)


threading.Thread(target=openaiapi.refresh_token).start()

bot = WebexBot(webex_token, approved_users=get_approved_user())

bot.add_command(SqlDebug())
bot.add_command(SqlOpt())
bot.add_command(SqlFormatter())
bot.add_command(ChatAI())
bot.add_command(CodeHelp())
bot.add_command(JiraStory())
bot.add_command(JiraStoryWrite())

send_bot_md_msg(
    webex_token,
    webex_space_id,
    "Webex Chat Bot is up and running...",
)

if __name__ == "__main__":
    bot.run()
