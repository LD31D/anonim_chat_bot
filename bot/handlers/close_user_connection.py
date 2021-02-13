from aiogram import types
from aiogram.dispatcher.filters.builtin import Text

from bot.utils import redis
from bot.loader import dp, bot
from bot.filters import IsUserConnectionExist
from bot.keyboards import start_dialog_keyboard


@dp.message_handler(Text('⬅️ Закончить диалог'), IsUserConnectionExist())
async def close_dialog_handler(message: types.Message):
	user_id = message.chat.id
	companion_id = await redis.get_user_connection(user_id)

	await redis.delete_user_connection(companion_id)
	await bot.send_message(
		companion_id, 
		"Ваш собеседник завершил диалог 🤗", 
		reply_markup=start_dialog_keyboard
		)

	await redis.delete_user_connection(user_id)
	await bot.send_message(
		user_id, 
		"Вы завершили диалог 🤫",
		reply_markup=start_dialog_keyboard
		)
