def sub_cb(topic, msg):
  print((topic, msg))

def connect_and_subscribe(client_id, mqtt_server):
    mqtt_client = MQTTClient(client_id=client_id, server=mqtt_server, keepalive=60)
    mqtt_client.set_callback(sub_cb)#The received topic and the topic message are passed to sub_cb callback function
    mqtt_client.connect()
    mqtt_client.subscribe(topic_sub)#Set the topic_sub (notification)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return mqtt_client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe(client_id, mqtt_server)
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    new_message = client.check_msg()
    if new_message != 'None':
      client.publish(topic_pub, b'received')
    time.sleep(1)
  except OSError as e:
    restart_and_reconnect()