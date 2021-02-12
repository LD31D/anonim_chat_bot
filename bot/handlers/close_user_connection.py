from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.filters.builtin import Command

from bot.utils import redis
from bot.loader import dp, bot


class IsUserConnectionExist(BoundFilter):

	async def check(self, message: types.Message):
		user_id = message.chat.id 

		result = await redis.check_user_connection(user_id)

		return result


@dp.message_handler(Command('exit'), IsUserConnectionExist())
async def add_user_to_queue(message: types.Message):
	user_id = message.chat.id
	companion_id = await redis.get_user_connection(user_id)

	await redis.delete_user_connection(companion_id)
	await bot.send_message(companion_id, "Ваш собеседник завершил диалог 🤗")

	await redis.delete_user_connection(user_id)
	await bot.send_message(user_id, "Вы завершили диалог 🤫")
