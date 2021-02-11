from aiogram.dispatcher.filters.builtin import Command

from bot.loader import dp
from bot.utils import redis


@dp.message_handler(Command('go'))
async def add_user_to_queue(message):
	user_id = message.chat.id

	if await redis.check_user_in_queue(user_id):
		await redis.add_user_to_queue(user_id)
		
	await message.answer("Ожидайте своего собеседника")
