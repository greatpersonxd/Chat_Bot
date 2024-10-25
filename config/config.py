from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "23170386"
# -------------------------------------------------------------
API_HASH = "11c7c26954dd7239cfa2a01719be2e45"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
DB_NAME = "shizuDB"
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7009601543"))
SUPPORT_GRP = "PARADISE_SOCITEY"
UPDATE_CHNL = "The_incricible"
OWNER_USERNAME = "llMR_KAMINAXDll"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002046320443"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "7520092354").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/greatpersonxd/Chat_Bot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
