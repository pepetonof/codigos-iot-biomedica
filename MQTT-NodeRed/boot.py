import time
import onewire
# import ds18x20
import dht
from umqttsimple import MQTTClient
import ubinascii
from machine import Pin, reset, unique_id
import micropython
import network

import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'PepeModem_2.4Gnormal'
password = 'JoseFuentesTomas'
mqtt_server = '192.168.100.54'

#EXAMPLE IP ADDRESS
client_id = ubinascii.hexlify(unique_id())
topic_sub = b'output'
topic_pub = b'temp'

last_sensor_reading = 0
readings_interval = 5

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

# ds_pin = machine.Pin(14)
# ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
dht_sensor = dht.DHT11(Pin(4))

led = Pin(2, Pin.OUT, value=0)
