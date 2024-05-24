import time
from umqttsimple import MQTTClient
import ubinascii
import network
import machine
import esp
import micropython

import esp
esp.osdebug(None)
import gc
gc.collect()

#Connect to Wifi 
ssid = 'PepeModem_2.4Gnormal'
password = 'JoseFuentesTomas'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

###IDs for broker
client_id = ubinascii.hexlify(machine.unique_id())
mqtt_server = '192.168.100.54'

topic_sub = b'hello'
topic_pub = b'notification'

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
