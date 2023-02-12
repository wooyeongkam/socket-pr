import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.logging_config import logger
from config.redis_config import redis
from config.websocket_config import sio, asgi_app

from adapter.websocket import websocket_start

def create_app():
  app = FastAPI()
  app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
  )

  app.mount('/ws', asgi_app)
  app.sio = sio

  websocket_start(sio, redis)

  return app


app = create_app()

@app.on_event('startup')
async def startup():
  logger.info("app start")

@app.on_event('shutdown')
async def shutdown():
  logger.info('shutdown')

if __name__ == '__main__':
  uvicorn.run("main:app", port=8080, host='0.0.0.0', reload=True)
