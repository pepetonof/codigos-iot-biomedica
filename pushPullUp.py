#Enciente un led utilizando resistencia interna Pull-Up:
#Al leer 0 encenderá el led

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    b = button.value()
    if b==False:
        led.value(True)
        print('Led On!', b)
        sleep(0.1)
    led.value(False)