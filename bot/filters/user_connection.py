from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from bot.utils import redis


class IsUserConnectionExist(BoundFilter):

	async def check(self, message: types.Message):
		user_id = message.chat.id 

		result = await redis.check_user_connection(user_id)

		return result
		