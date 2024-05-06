from machine import Pin#, I2C
#import BME280
import dht
import network
import urequests
import time

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'PepeModem_2.4Gnormal'
password = 'JoseFuentesTomas'

#thirdparty = 'http://maker.ifttt.com/trigger/dht/with/key/'
#api_key = 'nXzAb0zj9hZundKtdj_5FBEvmBkji4XgK3CSAxRL7px'

thirdparty = 'https://hook.us1.make.com/'
api_key = '79fckj22faiicrkxgqmuhjqbqmel3cgn'

#thirdparty = 'https://hook.us1.make.com/'
#api_key = 'xms9wxlqmbdmbmfff8mbw2df59w2i4v3'

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
  date=time.localtime()
  date = (b'{0:2d}/{1:2d}/{2:2d} at {3:2d}:{4:2d}:{5:2d}'.format(date[2],date[1],date[0],date[3],date[4],date[5]))
  sensor_readings = {'value1':temp, 'value2':hum, 'date':date}
  request_headers = {'Content-Type': 'application/json'}

  request = urequests.post(
    thirdparty + api_key,
    json=sensor_readings,
    headers=request_headers)
  print(request.text)
  request.close()

except OSError as e:
  print('Failed to read/publish sensor readings.')

