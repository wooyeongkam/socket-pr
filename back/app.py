import os
import dotenv
  
from flask import Flask, url_for, render_template
from flask_cors import CORS, cross_origin
from socketio import Server, WSGIApp
from namespaces import ChatNamespace
 
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_FOLDER = os.path.join(ROOT_PATH, "src")
TEMPLATE_FOLDER = STATIC_FOLDER
 
app = Flask(
  __name__,
  static_url_path="/static/",
  static_folder=STATIC_FOLDER,
  template_folder=TEMPLATE_FOLDER
)

CORS(app, resources={r'*': {'origins': '*'}})

def dated_url_for(endpoint, **values):
  if endpoint == 'static':
    filename = values.get('filename', None)
    if filename:
      file_path = os.path.join(app.static_folder, filename)
      values['q'] = int(os.stat(file_path).st_mtime)
  return url_for(endpoint, **values)
 
@app.context_processor
def override_url_for():
  return dict(url_for=dated_url_for)
 
@app.route('/', methods=["GET", "POST"])
@cross_origin()
def index():

  return 'ok'
 
sio = Server(
  async_mode="threading",
  logger=app.logger,
  engineio_logger=app.logger
)
sio.register_namespace(ChatNamespace(sio, '/chat'))
 
app.wsgi_app = WSGIApp(sio, app.wsgi_app)
 
if __name__ == "__main__":
  dotenv.load_dotenv(dotenv_path=".env")
  
  app.run(host="localhost", port=3001, threaded=True)