import threading

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
  return Response('Hello World')

# TODO: Crear brain.py... un proceso para dirigir otros procesos
def start_server():
  print('Comienzo el servidor')

  with Configurator() as config:
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6543, app)
  server.serve_forever()
  return server

# Comienzo el servidor
def start_server_thread():
  serverThread = threading.Thread(target=start_server)
  serverThread.start()
