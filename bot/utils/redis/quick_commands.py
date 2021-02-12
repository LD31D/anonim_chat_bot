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
	queue_len = await get_len_users_queue() # Getting len of queue

	if queue_len:
		redis = await aioredis.create_redis_pool(f'redis://{REDIS_HOST}', password=REDIS_PASSWORD)

		# Getting all users in queue for checking user in queue 
		users_queue_range = await redis.execute("LRANGE", "users_queue", 0, queue_len)

		redis.close()
		await redis.wait_closed()

		return user_id not in list(map(int, users_queue_range))

	return True


async def get_users_couple():
	redis = await aioredis.create_redis_pool(f'redis://{REDIS_HOST}', password=REDIS_PASSWORD)

	first_user_id = int(await redis.execute("LPOP", "users_queue"))
	second_user_id = int(await redis.execute("LPOP", "users_queue"))

	redis.close()
	await redis.wait_closed()

	return first_user_id, second_user_id


async def create_users_connections(first_user_id: int, second_user_id: int):
	redis = await aioredis.create_redis_pool(f'redis://{REDIS_HOST}', password=REDIS_PASSWORD)

	await redis.execute("HSET", "users_connections", first_user_id, second_user_id)
	await redis.execute("HSET", "users_connections", second_user_id, first_user_id)

	redis.close()
	await redis.wait_closed()


async def check_user_connection(user_id: int):
	redis = await aioredis.create_redis_pool(f'redis://{REDIS_HOST}', password=REDIS_PASSWORD)

	result = await redis.execute("HEXISTS", "users_connections", user_id)

	redis.close()
	await redis.wait_closed()

	return result


async def get_user_connection(user_id: int):
	redis = await aioredis.create_redis_pool(f'redis://{REDIS_HOST}', password=REDIS_PASSWORD)

	companion_id = int(await redis.execute("HGET", "users_connections", user_id))

	redis.close()
	await redis.wait_closed()

	return companion_id


async def delete_user_connection(user_id: int):
	redis = await aioredis.create_redis_pool(f'redis://{REDIS_HOST}', password=REDIS_PASSWORD)

	await redis.execute("HDEL", "users_connections", user_id)

	redis.close()
	await redis.wait_closed()
