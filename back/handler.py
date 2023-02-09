from redis import client
import time

async def new_alert_handler(redis: client.Redis, channel: client.PubSub, sio, event, namespace):
  while True:
    try:
      message = await channel.get_message() # {'type': 'subscribe', 'pattern': None, 'channel': 'alert_channel', 'data': [str]}
      print("new_alert_channel", message)
      if message is not None and type(message['data']) is str:
        # redis에 alerts키로 새로운 message를 push한다.
        # 새로운 메세지 유무 이벤트를 클라이언트에 emit한다.
    except Exception as e:
      print(e)
      break

    time.sleep(1)

async def alerts_handler(redis: client.Redis, sio, event, namespace):
  while True:
    try:
      alerts = await redis.lrange("alerts", 0, -1)
      print("alerts_data", alerts)
      if alerts is not None:
        # alerts를 클라이언트에 emit한다.
    except Exception as e:
      print(e)
      break

    time.sleep(1)
