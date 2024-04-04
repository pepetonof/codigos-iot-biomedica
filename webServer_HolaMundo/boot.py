#Importar sockets
try:
  import usocket as socket
except:
  import socket

#Permite conectar ell ESP32 a la red WiFi
import network

#Apaga los mensajes de depuración
import esp
esp.osdebug(None)

#Colector de basura para ahorrar espacio en flash
import gc
gc.collect()

#Credenciales
ssid = 'JoseFuentesTomas'
password = 'JoseFuentesTomas'

#Crea la interfaz de estación
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

#Asegura que funcione solo mientras esta conectado
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())