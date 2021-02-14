from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_dialog_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔎 Найти собеседника"),
        ],
    ],
    resize_keyboard=True
)


end_dialog_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌ Закончить диалог"),
        ],
    ],
    resize_keyboard=True
)

leave_queue_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Покинуть очередь"),
        ],
    ],
    resize_keyboard=True
)
