from aiogram import types
from aiogram.dispatcher.filters.builtin import Text

from bot.utils import redis
from bot.loader import dp, bot
from bot.keyboards import start_dialog_keyboard


@dp.message_handler(Text('⬅️ Покинуть очередь'))
async def leave_queue_handler(message: types.Message):
	user_id = message.chat.id
	
	await redis.delete_user_from_queue(user_id)
	await message.answer("Вы покинули очередь 👀", reply_markup=start_dialog_keyboard)
