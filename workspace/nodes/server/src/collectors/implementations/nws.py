import requests
import time

NWS_API = "https://api.weather.gov"

def start_nws_collector():
  starttime = time.monotonic()
  while True:
    print("Conseguido el tiempo para Nueva York...")
    getNWSData('glossary')
    time.sleep(60.0 - ((time.monotonic() - starttime) % 60.0))

def getNWSData(path):
  data = requests.get(getNWSUrl(path))
  print(data.text)

def getNWSUrl(path):
  return "%s/%s" %(NWS_API, path)
