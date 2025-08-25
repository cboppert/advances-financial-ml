import threading

from server.server import start_server

if __name__ == '__main__':
  # TODO: Crear un clase base para los procesos
  # Correr el server en un proceso
  # Crear el proceso y correr aqui
  print('Comienzo el cerebro')
  serverThread = threading.Thread(target=start_server)
  serverThread.start()
