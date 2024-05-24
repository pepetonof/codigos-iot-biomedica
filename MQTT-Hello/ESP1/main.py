#Runs whenever a message is published on a topic the ESP is subscribed to
#The function should be accept as parameters the topic and the message
#The callback function  handless what happens when a specific message is received on a topic
def sub_cb(topic, msg):
    print((topic, msg))

def connect_and_subscribe(client_id, mqtt_server):
    mqtt_client = MQTTClient(client_id=client_id, server=mqtt_server, keepalive=60)
    mqtt_client.set_callback(sub_cb)#The received topic and the topic message are passed to sub_cb callback function
    mqtt_client.connect()
    mqtt_client.subscribe(topic_sub)#Set the topic_sub (notification)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return mqtt_client

#In case on not succesfull connection, wait and use the reset() method
def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()

#Try to connect to the MQTT broker and subcrive
try:
  client = connect_and_subscribe(client_id, mqtt_server)
except OSError as e: #In case of error, reset the ESP
  restart_and_reconnect()
  

while True:
  try:
    client.check_msg()#Checks whether a pending message form the server is available
#     if new_message !='None':
#         client.publish(topic_pub, b'received')
#     time.sleep(1)
    if (time.time() - last_message) > message_interval:#Time to send a new message
      msg = b'Hello #%d' % counter
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect() #In case of error, reset the ESP
