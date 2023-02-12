from socketio import AsyncServer
from redis.asyncio import client
import time

from config.logging_config import logger

NEW_ALERT_CHANNEL = "alert_channel"

async def new_alert_handler(redis: client.Redis, pubsub: client.PubSub, sio: AsyncServer, event, namespace):
  await pubsub.subscribe(NEW_ALERT_CHANNEL)
  await handle_new_alert(redis, pubsub, sio, event, namespace)
  await pubsub.unsubscribe(NEW_ALERT_CHANNEL)


async def handle_new_alert(redis: client.Redis, pubsub: client.PubSub, sio: AsyncServer, event, namespace):
  while NEW_ALERT_CHANNEL in pubsub.channels:
    try:
      message = await pubsub.get_message(timeout=5)
      if message is not None and type(message['data']) is str:
        logger.info(message['data'])
        
        # emit_new_alert 실행

    except Exception as error:
      logger.info(error)
      break

    time.sleep(1)


async def emit_new_alert(data: str, redis: client.Redis, sio: AsyncServer, event, namespace):
  logger.info(data)
  # redis에 alerts키로 새로운 message를 push한다.

  # 새로운 메세지 유무 이벤트를 클라이언트에 emit한다.
  