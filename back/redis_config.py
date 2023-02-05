from aioredis import Redis

REDIS_HOST = 'redis-17979.c256.us-east-1-2.ec2.cloud.redislabs.com'
REDIS_PASSWORD = 'LiK1wqItmgBNwscwJxemliEA1RtnLZ0E'
REDIS_PORT = 17979

redis = Redis(
  host=REDIS_HOST,
  port=REDIS_PORT,
  password=REDIS_PASSWORD,
  decode_responses=True
)

redis_pubsub = redis.pubsub()


