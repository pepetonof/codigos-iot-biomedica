def read_sensor():
    global temp, hum
    print('Temperatures: ')
    temp = hum = 0
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    hum = dht_sensor.humidity()
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      msg = (b'{0:3.1f},{1:3.1f}'.format(temp, hum))
      hum = round(hum, 2)
      print(temp, end=' ')
      print('Valid temperature')
      return msg
    return b'0.0'

# def read_ds_sensor():
#   roms = ds_sensor.scan()
#   print('Found DS devices: ', roms)
#   print('Temperatures: ')
#   ds_sensor.convert_temp()
#   time.sleep(1)
#   for rom in roms:
#     temp = ds_sensor.read_temp(rom)
#     if isinstance(temp, float):
#       # uncomment for Fahrenheit
#       #temp = temp * (9/5) + 32.0
#       msg = (b'{0:3.1f}'.format(temp))
#       print(temp, end=' ')
#       print('Valid temperature')
#       return msg
#   return b'0.0'

def sub_cb(topic, msg):
  print((topic, msg))
  if msg == b'on':
    led.value(1)
  elif msg == b'off':
    led.value(0)

def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub
    mqtt_client = MQTTClient(client_id=client_id, server=mqtt_server, keepalive=60)
    mqtt_client.set_callback(sub_cb)#The received topic and the topic message are passed to sub_cb callback function
    mqtt_client.connect()
    mqtt_client.subscribe(topic_sub)#Set the topic_sub (notification)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return mqtt_client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    if (time.time() - last_sensor_reading) > readings_interval:
      msg = read_sensor()
      client.publish(topic_pub, msg)
      last_sensor_reading = time.time()
#   except onewire.OneWireError:
#     print('Failed to read/publish sensor readings.')
#     time.sleep(1)
  except OSError as e:
    restart_and_reconnect()
