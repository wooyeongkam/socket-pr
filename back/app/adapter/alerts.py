from socketio import AsyncServer
from redis.asyncio import client
import time

from config.logging_config import logger

shouldTerminate = False

def change_shouldTerminate(value: bool):
  global shouldTerminate
  shouldTerminate = value

async def alerts_handler(redis: client.Redis, sio: AsyncServer, event, namespace):
  while not shouldTerminate:
    try:
      alerts = await redis.lrange("alerts", 0, -1)
      if alerts is not None:
        logger.info(alerts)
        
        # alerts를 클라이언트에 emit한다.

    except Exception as error:
      logger.info(error)
      break

    time.sleep(1)

  change_shouldTerminate(False)


def alerts_terminate_handler():
  logger.info('terminate')
  change_shouldTerminate(True)

