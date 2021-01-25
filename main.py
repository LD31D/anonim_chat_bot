from aiogram import executor
from bot.handlers import dp


if __name__ == '__main__':
	executor.start_polling(dp)
