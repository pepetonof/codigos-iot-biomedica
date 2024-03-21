#Controla el nivel de brillo de un led con un potenciometro
from machine import Pin, PWM, ADC
from time import sleep

#Resolucion que se requiere por ADC y el voltaje de referencia
pot = ADC(Pin(4))
pot.width(ADC.WIDTH_10BIT)## 10 bits, dado los posible valores de Freq en PWM
pot.atten(ADC.ATTN_11DB)##Full range voltage 3.3V

#Configuracion de PWM(brillo de led)
led = PWM(Pin(5), 5000)

while True:
    duty_cycle = pot.read()
    volt = duty_cycle/1024
    #Formato usando print y operador string modulo
    #print('El valor del ADC es %d y el voltaje es %1.2f mV' % (duty_cycle, volt))
    
    #Formato usando print y metodo format
    #print(f"El valor del ADC es {duty_cycle} y el voltaje es {volt} mV")
    print('El valor del ADC es {} y el voltaje es {} mV'.format(duty_cycle, volt))
    if duty_cycle<15:
        led.duty(0)
    else:
        led.duty(duty_cycle)
    sleep(0.005)