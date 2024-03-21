#Enciente un led utilizando resistencia interna Pull-Up:
#Al leer 1 encenderá el led

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_DOWN)

while True:
    b = button.value()
    if b==True:
        led.value(True)
        print('Led On!', b)
        sleep(0.1)
    led.value(False)