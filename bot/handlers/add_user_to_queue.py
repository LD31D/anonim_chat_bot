from aiogram.dispatcher.filters.builtin import Command

from bot.utils import redis
from bot.loader import dp, bot


@dp.message_handler(Command('go'))
async def add_user_to_queue(message):
	user_id = message.chat.id

	if await redis.check_user_in_queue(user_id):
		await redis.add_user_to_queue(user_id)

		if (await redis.get_len_users_queue()) >= 2:
			first_user_id, second_user_id = await redis.get_users_couple()

			await redis.create_users_connections(first_user_id, second_user_id)

			text = "Ваш собеседник был найден. Можете начать общение 😜"
			await bot.send_message(first_user_id, text)
			await bot.send_message(second_user_id, text)

			return 

		await message.answer("Ожидайте своего собеседника 😊")

	else:	
		await message.answer("Вы уже находитесь в очереди! Ожидайте своего собеседника 😊")
