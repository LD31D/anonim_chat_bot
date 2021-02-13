from aiogram import types
from aiogram.dispatcher.filters.builtin import Text

from bot.utils import redis
from bot.loader import dp, bot
from bot.keyboards import end_dialog_keyboard


@dp.message_handler(Text('🔎 Найти собеседника'))
async def add_user_to_queue_handler(message: types.Message):
	user_id = message.chat.id

	if await redis.check_user_in_queue(user_id):
		await redis.add_user_to_queue(user_id)

		if (await redis.get_len_users_queue()) >= 2:
			first_user_id, second_user_id = await redis.get_users_couple()

			await redis.create_users_connections(first_user_id, second_user_id)

			text = "Ваш собеседник был найден. Можете начать общение 😜"
			await bot.send_message(first_user_id, text, reply_markup=end_dialog_keyboard)
			await bot.send_message(second_user_id, text, reply_markup=end_dialog_keyboard)

			return 

		await message.answer("Ожидайте своего собеседника 😊")

	else:	
		await message.answer("Вы уже находитесь в очереди! Ожидайте своего собеседника 😊")
