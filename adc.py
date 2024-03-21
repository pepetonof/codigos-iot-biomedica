#Lee por el pin 4 (ADC2 CH0) un voltaje
#Recordar que la resolución del ADC del ESP32 es de 12 bits
#mientras que el voltaje de referencia es de 3.3V, aunque este
#puede ser modificado. Por lo tanto
#por cada cambio de bit se leerán 3.3V/4096 = 0.8056 mV

from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(4))
#Resolucion que se requiere
#bit = ADC.WIDTH_9BIT
#bit = ADC.WIDTH_10BIT
#bit = ADC.WIDTH_11BIT
#bit = ADC.WIDTH_12BIT
pot.width(ADC.WIDTH_12BIT)

#Voltaje que se quiere leer
#ADC.ATTN_11DB:3.3V,
#ADC.ATTN_6DB: 2.0V,
#ADC.ATTN_2_5DB: 1.5V,
#ADC.ATTN_0DB: 1.2V
pot.atten(ADC.ATTN_11DB)##3.3V
while True:
    pot_value = pot.read()
    print(pot_value, pot_value*3.3/4096) #Asumiendo que se maneja resolucion 12 bits
    sleep(0.1)