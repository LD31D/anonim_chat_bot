from os import getenv


BOT_TOKEN = getenv("BOT_TOKEN")

REDIS_HOST = getenv("REDIS_HOST")
REDIS_PASSWORD = getenv("REDIS_PASSWORD") if getenv("REDIS_PASSWORD") else None

HEROKU_APP_NAME = getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(getenv('PORT', 8080))
