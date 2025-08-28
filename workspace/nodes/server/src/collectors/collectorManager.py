import threading

from collectors.implementations.nws import start_nws_collector

def comienzarLosCollectors():
  nwsThread = threading.Thread(target=start_nws_collector)
  nwsThread.start()
