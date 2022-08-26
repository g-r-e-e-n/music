import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "7878052"))
API_HASH = getenv("API_HASH", "8a54507d31d97e7a41141032df195775")
BOT_TOKEN = getenv("BOT_TOKEN", "1998438810:AAFLXC8WNx77x6KFM5puEIGSD1Q01HfwToY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQAONpQgMm8RvKvnwcJvUxfQyOaDmAjUcNGUEcaqz2pTk67TnYh9nr9egV5mLspZbyqpSrgVz5rdwFDAo2D20uGQuMBpb4x5bZuqavYJcvayCSXtk_G9vH8w0ASDG62TJnM2DSoLA5q6Dod5YphTEzFaHE5zoo0giVWbIMirB4dnI5D96YIvcfmtHvJqDWxfx5FSfYSaAIZs1kTWv_Jgpk2j7Iuu39NsNbU6WHFrrGKxBnU1BMYQO4s0U6qgnsxhcxYsb5IEVI8bGq1LbUe_TFunx32tbvx5dZ8vehx_28CWNABrQA7MOkMQH26OAtBHfnAzFqRSlOdNAYSDl1-FWgcudKIwGAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2023242625").split()))
