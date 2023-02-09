import socketio
from redis import client
import time

BADGE_NEW_ALERT_EVENT = "new_alert"
BADGE_ALERTS_EVENT = "alerts"

class AlertNamespace(socketio.AsyncNamespace):
  def __init__(self, namespace: str, redis: client.Redis, channel: client.PubSub, sio, channel_name: str):
    super().__init__(namespace)
    self.namespace = namespace
    self.redis = redis
    self.sio = sio
    self.channel = channel
    self.channel_name = channel_name

    self.is_active_new_alert = False
    self.is_active_alerts = False

  async def on_connect(self, sid, environ):
    print('connect', sid)
    await self.channel.subscribe(self.channel_name)


  async def on_disconnect(self, sid):
    print('disconnect', sid)
    await self.channel.unsubscribe(self.channel_name)
    self.is_active_alerts = False
    self.is_active_new_alert = False


  async def on_new_alert(self, sid):
    if (self.is_active_new_alert == True):
      return

    self.is_active_new_alert = True
    await self.new_alert_handler()


  async def on_alerts(self, sid):
    if (self.is_active_alerts == True):
      return

    self.is_active_alerts = True
    await self.alerts_handler()


  async def new_alert_handler(self):
    while self.is_active_new_alert:
      try:
        message = await self.channel.get_message() # {'type': 'subscribe', 'pattern': None, 'channel': 'alert_channel', 'data': [str]}
        print("new_alert_channel", message)
        if message is not None and type(message['data']) is str:
          # redis에 alerts키로 새로운 message를 push한다.
          # 새로운 메세지 유무 이벤트를 클라이언트에 emit한다.
      except Exception as e:
        print(e)
        self.channel.unsubscribe("alert_channel")
        break

      time.sleep(1)
   

  async def alerts_handler(self):
    while self.is_active_alerts:
      try:
        alerts = await self.redis.lrange("alerts", 0, -1)
        print("alerts_data", alerts)
        if alerts is not None:
          # alerts를 클라이언트에 emit한다.
      except Exception as e:
        print(e)
        break

      time.sleep(1)