import umail
import network
import dht
from machine import Pin

# Your network credentials
ssid = 'PepeModem_2.4Gnormal'
password = 'JoseFuentesTomas'

# Email details
sender_email = 'netmiauv3@gmail.com'
sender_name = 'ESP32' #sender name
sender_app_password = 'quqqnngzuastyvxg'
recipient_email ='netmiauv3@gmail.com'
email_subject ='Test Email'

def connect_wifi(ssid, password):
  #Connect to your network
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  print(station.ifconfig())

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
    
# Connect to your network
connect_wifi(ssid, password)

sensor = dht.DHT11(Pin(4))
try:
  read_sensor()
  #sensor_readings = {'value1':temp, 'value2':hum}
  #print(sensor_readings)
  # Send the email
  smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
  #Lo to the account
  smtp.login(sender_email, sender_app_password)
  #Set the recipient email passing the recipient's email as argument
  smtp.to(recipient_email)
  smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
  smtp.write("Subject:" + email_subject + "\n")
  smtp.write("Temperature ")
  smtp.write((b'{0:3.1f}'.format(temp)).decode("utf-8"))
  smtp.write("\nHumidity ")
  smtp.write((b'{0:3.1f}'.format(hum)).decode("utf-8"))
  smtp.send()
  smtp.quit()
  #smtp.write("Humidity:\n")
  #msg=b'{0:3.1f}'.format(hum)
  #smtp.write(msg)

  #smtp.write((b'{0:3.1f},{1:3.1f}'.format(temp, hum)))
  ##If you need to send a long string as the email body, break the email message into smaller
  ##chunks and send each chunk using the write() method
  
  ##Close the connection
  

except OSError as e:
  print('Failed to read/publish sensor readings.')


