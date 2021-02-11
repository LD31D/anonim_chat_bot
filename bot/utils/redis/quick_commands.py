import aioredis

from bot.data.config import REDIS_HOST, REDIS_PASSWORD


async def add_user_to_queue(user_id: int):
	redis = await aioredis.create_redis_pool(f'redis://{REDIS_HOST}', password=REDIS_PASSWORD)

	await redis.execute("RPUSH", "users_queue", user_id)

	redis.close()
	await redis.wait_closed()


async def get_len_users_queue():
	redis = await aioredis.create_redis_pool(f'redis://{REDIS_HOST}', password=REDIS_PASSWORD)

	queue_len = await redis.execute("LLEN", "users_queue")

	redis.close()
	await redis.wait_closed()

	return queue_len


async def check_user_in_queue(user_id: int):
	queue_len = await get_len_users_queue()

	if queue_len:
		redis = await aioredis.create_redis_pool(f'redis://{REDIS_HOST}', password=REDIS_PASSWORD)

		users_queue_range = await redis.execute("LRANGE", "users_queue", 0, queue_len)

		redis.close()
		await redis.wait_closed()

		for user in users_queue_range:
			if int(user) == user_id:
				return False

	return True
