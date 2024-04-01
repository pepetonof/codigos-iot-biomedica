#Interrupciones
#Una vez que se detecta movimiento, un led es encendido
#durante 20 s
#La función de gestión de interrupciones
#debe aceprar un parámetro del tipo Pin
#El Pin que servirá como interrupcion se declara como pin de
#entrada
#Utilizar el método irq() (interrupt request)
#Como argumentos recibe el modo de disparoTrigger y handler
#Pin.IRQ_FALLING
#Pin.IRQ_RISING
#Pin.LOW_LEVEL
#Pin.HIGH_LEVEL
#Pueden considerarse disyunciones
#handler se refiere a la función que se llamata cuando se
#detecte una interrupción

from machine import Pin
from time import sleep

motion = False

def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

led = Pin(2, Pin.OUT)
pir = Pin(14, Pin.IN)
pir.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)

while True:
  if motion:
    print('Motion detected! Interrupt caused by:', interrupt_pin)
    led.value(1)
    sleep(1)
    led.value(0)
    print('Motion stopped!')
    motion = False
