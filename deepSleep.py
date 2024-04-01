from machine import deepsleep
from machine import Pin
from time import sleep

led = Pin (2, Pin.OUT)

#blink LED
led.value(1)
sleep(1)
led.value(0)
sleep(1)

#Para codigos de prueba es recomendable usar la siguiente instruccion
#Si se desea sbir codigo nuevo, la placa debe estar despierta, es necesario
#tomarlo despierta para subir código
sleep(5)

print('Im awake, but Im going to sleep')

#sleep for 10 seconds (10000 milliseconds)
deepsleep(10000)