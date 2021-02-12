from aiogram import Dispatcher

from .user_connection import IsUserConnectionExist


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsUserConnectionExist)
