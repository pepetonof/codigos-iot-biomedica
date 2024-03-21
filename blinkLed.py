from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
estado = False

while True:
    led.value(not led.value())
    estado = not estado
    print(f'Estado:\t {estado}')
    sleep(0.9)