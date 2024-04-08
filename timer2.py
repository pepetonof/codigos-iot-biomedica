from machine import Pin, Timer
from time import time

start_timer = False
motion = False
last_motion_time = 0
delay_interval = 10

def handle_interrupt(pin):
  global motion, last_motion_time, start_timer
  motion = True
  start_timer = True
  last_motion_time = time()

led1 = Pin(2, Pin.OUT)
led2 = Pin(5, Pin.OUT)
pir = Pin(4, Pin.IN, pull=Pin.PULL_UP)

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

def timer_interrupt(t):
    led1.value(not led1.value())

timer = Timer(-1)
timer.init(period=250, mode=Timer.PERIODIC,
           callback=timer_interrupt)   #initializing the timer

while True:
  #revisa si se dececta movimiento y si el timer esta activado
  if motion and start_timer:
    print('Motion detected!')
    led2.value(1)
    start_timer = False
  ##revisa si se han pasado mas de 20 segundo desde que el movimiento fue detectado
  elif motion and (time() - last_motion_time)>delay_interval:
    print('Motion stopped!')
    led2.value(0)
    motion = False