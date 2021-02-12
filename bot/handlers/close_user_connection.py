from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from bot.utils import redis
from bot.loader import dp, bot
from bot.filters import IsUserConnectionExist


@dp.message_handler(Command('exit'), IsUserConnectionExist())
async def close_dialog_handler(message: types.Message):
	user_id = message.chat.id
	companion_id = await redis.get_user_connection(user_id)

	await redis.delete_user_connection(companion_id)
	await bot.send_message(companion_id, "Ваш собеседник завершил диалог 🤗")

	await redis.delete_user_connection(user_id)
	await bot.send_message(user_id, "Вы завершили диалог 🤫")
