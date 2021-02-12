from os import getenv

from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = getenv("BOT_TOKEN")

REDIS_HOST = getenv("REDIS_HOST")
REDIS_PASSWORD = getenv("REDIS_PASSWORD") if getenv("REDIS_PASSWORD") else None
