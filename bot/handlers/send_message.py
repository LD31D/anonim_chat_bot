from aiogram import types

from bot.utils import redis
from bot.loader import dp, bot
from bot.filters import IsUserConnectionExist


@dp.message_handler(IsUserConnectionExist())
async def send_text_message_handler(message: types.Message):
	user_id = message.chat.id
	text = message.text

	companion_id = await redis.get_user_connection(user_id)

	await bot.send_message(companion_id, text)
