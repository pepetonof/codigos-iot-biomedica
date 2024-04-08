try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'PepeModem_2.4Gnormal'
password = 'JoseFuentesTomas'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)


def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>ESP Web Server</h1><a href=\"?led=on\"><button>ON</button></a>&nbsp;
  <a href=\"?led=off\"><button>OFF</button></a></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  try:
    if gc.mem_free() < 102000:#number of bytes 
      gc.collect()
    conn, addr = s.accept()
    conn.settimeout(3.0)#Tiempo (s) de espera en operacion blocking
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)#recibe datos (bytes) max cant inf simult.
    conn.settimeout(None)#blocking socket
    request = str(request)
    #print('Content = %s' % request)
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')
    if led_on == 6:
      print('LED ON', request)
      led.value(1)
    if led_off == 6:
      print('LED OFF', request)
      led.value(0)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
  except OSError as e:
    conn.close()
    print('Connection closed')