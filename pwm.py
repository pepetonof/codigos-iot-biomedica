#Utiliza PWM, el cual requiere de 3 parámetros:
#1.Pin \in [0, 78125]
#2.Frecuencia \in [0, 78125]
#3.Ciclo de trabajo \in [0, 1023]
#En el presente código, simplemente se itera en el ciclo de trabajo

from machine import Pin, PWM
from time import sleep

freq = 5000
led = PWM(Pin(5), freq)

while True:
    for duty_cycle in range(0, 1024):
        print('DutyCycle:\t', duty_cycle)
        led.duty(duty_cycle)
        sleep(0.0005)