from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from bot.loader import dp
from bot.keyboards import start_dialog_keyboard


@dp.message_handler(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
	    	f'Привет, {message.from_user.full_name}!', 
	    	reply_markup=start_dialog_keyboard
    	)
