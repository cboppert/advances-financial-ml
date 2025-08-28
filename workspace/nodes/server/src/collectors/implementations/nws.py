import time

NWS_API = "https://api.weather.gov"

def start_nws_collector():
  starttime = time.monotonic()
  while True:
    print("Conseguido el tiempo para Nueva York...")
    time.sleep(60.0 - ((time.monotonic() - starttime) % 60.0))
