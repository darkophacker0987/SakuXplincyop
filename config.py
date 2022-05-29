import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "5369003337"))
API_ID = int(getenv("API_ID", "3706077")) #oP
API_HASH = getenv("API_HASH", "5bec73923f996b3092a4209ac556bc58")
