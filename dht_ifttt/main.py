# Complete project details at https://RandomNerdTutorials.com

from machine import Pin#, I2C
#import BME280
import dht
import network
import urequests

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'PepeModem_2.4Gnormal'
password = 'JoseFuentesTomas'

api_key = 'nXzAb0zj9hZundKtdj_5FBEvmBkji4XgK3CSAxRL7px'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

sensor = dht.DHT11(Pin(4))

def read_sensor():
  global temp, temp_percentage, hum
  temp = temp_percentage = hum = 0
  try:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    #print(temp, hum)
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      hum = round(hum, 2)
      return temp, hum
    else:
      return('Invalid sensor readings.')
  except OSError as e:
    return('Failed to read sensor.')

try:
  read_sensor()
  sensor_readings = {'value1':temp, 'value2':hum}
  print(sensor_readings)

  request_headers = {'Content-Type': 'application/json'}

  request = urequests.post(
    'http://maker.ifttt.com/trigger/dht/with/key/' + api_key,
    json=sensor_readings,
    headers=request_headers)
  print(request.text)
  request.close()

except OSError as e:
  print('Failed to read/publish sensor readings.')

