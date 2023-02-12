from socketio import AsyncServer
from redis.asyncio import Redis

from config.logging_config import logger
from .util.websocket_process import event_processed,remove_processed_event, precessed_events
from .alerts import alerts_handler, alerts_terminate_handler, change_shouldTerminate
from .new_alert import new_alert_handler, NEW_ALERT_CHANNEL


BADGE_NSP= "/badge"
BADGE_NEW_ALERT_EVENT= "new_alert"
BADGE_ALERTS_EVENT= "alerts"
BADGE_ALERTS_TERMINATE_EVENT= "alerts_terminate"

def websocket_start(sio: AsyncServer, redis: Redis):
  pubsub = redis.pubsub()
  pubsub.unsubscribe(NEW_ALERT_CHANNEL)
  
  @sio.event(namespace=BADGE_NSP)
  def connect(sid, eviron):
    logger.info(f'connect {sid}')

    if not event_processed(BADGE_NEW_ALERT_EVENT):
      sio.start_background_task(new_alert_handler, redis, pubsub, sio, BADGE_NEW_ALERT_EVENT, BADGE_NSP)


  @sio.event(namespace=BADGE_NSP)
  async def disconnect(sid):
    logger.info(f'disconnect {sid}')

    await pubsub.unsubscribe(NEW_ALERT_CHANNEL)
    alerts_terminate_handler()
    change_shouldTerminate(False)
    precessed_events.clear()


  @sio.on(BADGE_ALERTS_EVENT, namespace= BADGE_NSP)
  async def alerts_socket_handler(sid):
    logger.info(f'event {BADGE_ALERTS_EVENT}')

    if not event_processed(BADGE_ALERTS_EVENT):
      sio.start_background_task(alerts_handler, redis, sio, BADGE_ALERTS_EVENT, BADGE_NSP)


  @sio.on(BADGE_ALERTS_TERMINATE_EVENT, namespace= BADGE_NSP)
  async def alerts_terminate_socket_handler(sid):
    logger.info(f'event {BADGE_ALERTS_TERMINATE_EVENT}')

    alerts_terminate_handler()
    remove_processed_event(BADGE_ALERTS_EVENT)
