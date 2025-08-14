# devgaganin
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27696177"))
API_HASH = getenv("API_HASH", "0c44906a4feff3b947db76dfa7c57d88")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "6987799874"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://drozmarizabel991hull:Xh89XLrFTYOPgupl@cluster0.x8qoe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002021784050"))
FORCESUB = getenv("FORCESUB", "SkyHub4u")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # this is jkust to help if you dont want to force your bot user to login or if they not interested

