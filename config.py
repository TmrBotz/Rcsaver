# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27696177"))
API_HASH = getenv("API_HASH", "0c44906a4feff3b947db76dfa7c57d88")
BOT_TOKEN = getenv("BOT_TOKEN", "7976541534:AAEmpWm6FzFbj8oyAihdNq0Q-JWmKqiPF1A")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6987799874").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://drozmarizabel991hull:Xh89XLrFTYOPgupl@cluster0.x8qoe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002655225425")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002655225425"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
WEBSITE_URL = getenv("WEBSITE_URL", "gplinks.com")
AD_API = getenv("AD_API", "8cefe6e80dc4dd1f046e74f32e3d3fee248306f3")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
