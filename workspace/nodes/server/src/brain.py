from dotenv import load_dotenv

from server.server import start_server_thread
from collectors.collectorManager import comienzarLosCollectors

if __name__ == '__main__':
  # TODO: Crear un clase base para los procesos
  # Correr el server en un proceso
  # Crear el proceso y correr aqui
  start_server_thread()
  comienzarLosCollectors()
