from aiogram import executor

from bot.loader import bot
from bot.handlers import dp
from bot.config import WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_URL


async def on_startup(dp):
	await db.create()
	await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


if __name__ == '__main__':
	executor.start_polling(dp)

	executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=False,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
