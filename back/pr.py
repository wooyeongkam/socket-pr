import os
import time
import socketio
from aiohttp import web
from handler import new_alert_handler, alerts_handler
from redis_config import redis, redis_pubsub

sio = socketio.AsyncServer(cors_allowed_origins="*")
app = web.Application()
sio.attach(app)

NEW_ALERT_CHANNEL = "alert_channel"
BADGE_NSP = "/badge"
BADGE_NEW_ALERT_EVENT = "new_alert"
BADGE_ALERTS_EVENT = "alerts"

@sio.event(namespace=BADGE_NSP)
def connect(sid, eviron):
  print('connect', sid)

@sio.event(namespace=BADGE_NSP)
def disconnect(sid):
    print('disconnect ', sid)

@sio.on(BADGE_NEW_ALERT_EVENT, namespace=BADGE_NSP)
async def new_alert_channel_handler(sid):
    await redis_pubsub.subscribe(NEW_ALERT_CHANNEL)
    await new_alert_handler(redis, redis_pubsub, sio, BADGE_NEW_ALERT_EVENT, BADGE_NSP)
    await redis_pubsub.unsubscribe(NEW_ALERT_CHANNEL)

@sio.on(BADGE_ALERTS_EVENT, namespace= BADGE_NSP)
async def alerts_socket_handler(sid):
    await alerts_handler(redis, sio, BADGE_ALERTS_EVENT, BADGE_NSP)


if __name__ == '__main__':
    web.run_app(app, host="localhost", port=8080)