from aiogram import types

from bot.utils import redis
from bot.loader import dp, bot
from bot.filters import IsUserConnectionExist


@dp.message_handler(IsUserConnectionExist())
async def send_text_message_handler(message: types.Message):
	user_id = message.chat.id
	text = message.text

	companion_id = await redis.get_user_connection(user_id)

	await bot.send_message(companion_id, text)


@dp.message_handler(IsUserConnectionExist(), content_types=types.ContentType.PHOTO)
async def send_photo_message_handler(message: types.Message):
	user_id = message.chat.id

	photo = message.photo[-1].file_id
	caption = message.caption

	companion_id = await redis.get_user_connection(user_id)

	await bot.send_photo(companion_id, photo, caption=caption)


@dp.message_handler(IsUserConnectionExist(), content_types=types.ContentType.VIDEO)
async def send_video_message_handler(message: types.Message):
	user_id = message.chat.id

	video = message.video.file_id
	caption = message.caption

	companion_id = await redis.get_user_connection(user_id)

	await bot.send_video(companion_id, video, caption=caption)


@dp.message_handler(IsUserConnectionExist(), content_types=types.ContentType.AUDIO)
async def send_audio_message_handler(message: types.Message):
	user_id = message.chat.id

	audio = message.audio.file_id
	caption = message.caption

	companion_id = await redis.get_user_connection(user_id)

	await bot.send_audio(companion_id, audio, caption=caption)


@dp.message_handler(IsUserConnectionExist(), content_types=types.ContentType.VOICE)
async def send_voice_message_handler(message: types.Message):
	user_id = message.chat.id

	voice = message.voice.file_id

	companion_id = await redis.get_user_connection(user_id)

	await bot.send_voice(companion_id, voice)


@dp.message_handler(IsUserConnectionExist(), content_types=types.ContentType.VIDEO_NOTE)
async def send_video_note_message_handler(message: types.Message):
	user_id = message.chat.id

	video_note = message.video_note.file_id

	companion_id = await redis.get_user_connection(user_id)

	await bot.send_video_note(companion_id, video_note)


@dp.message_handler(IsUserConnectionExist(), content_types=types.ContentType.ANY)
async def catch_else_message_format_handler(message: types.Message):
	await message.reply(
			"Сообщение не было отправлено! "
			"На данный момент, бот не поддерживает подобный формат сообщений 😟"
		)
