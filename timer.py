from machine import Pin
from time import time

start_timer = False
motion = False
last_motion_time = 0
delay_interval = 3

def handle_interrupt(pin):
  global motion, last_motion_time, start_timer
  motion = True
  start_timer = True
  last_motion_time = time()

led = Pin(12, Pin.OUT)
pir = Pin(14, Pin.IN)

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
  #revisa si se dececta movimiento y si el timer esta activado
  if motion and start_timer:
    print('Motion detected!')
    led.value(1)
    start_timer = False
  ##revisa si se han pasado mas de 20 segundo desde que el movimiento fue detectado
  elif motion and (time() - last_motion_time)>delay_interval:
    print('Motion stopped!')
    led.value(0)
    motion = False