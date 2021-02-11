from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from bot.utils import redis
from bot.loader import dp, bot


class IsUserConnectionExist(BoundFilter):

	async def check(self, message: types.Message):
		user_id = message.chat.id 

		result = await redis.check_user_connection(user_id)

		return result


@dp.message_handler(IsUserConnectionExist())
async def send_text_message(message: types.Message):
	user_id = message.chat.id
	text = message.text

	companion_id = await redis.get_user_connection(user_id)

	await bot.send_message(companion_id, text)
