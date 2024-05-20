from time import sleep
from random import randint
from machine import Pin, UART, ADC, SoftI2C, Timer
import ssd1306 #OLED library
from time import sleep

#Pin 2 with LED
led = Pin(2, Pin.OUT)

#ADC
sensor = ADC(Pin(4))
sensor.width(ADC.WIDTH_10BIT)## 10 bits
sensor.atten(ADC.ATTN_11DB)##Full range voltage 3.3V

#I2C
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def timer_interrupt(t):
    global reading
    reading = sensor.read()
    L = reading & 0xFF
    H = (reading >> 8) & 0x03
#     while uart.txdone():
#        uart.write(str(reading))
    uart.write(b'\x64')#100
    uart.write(b'\xc8')#200
    uart.write((H).to_bytes(1,'big'))
    uart.write((L).to_bytes(1,'big'))

#Timer 
timer = Timer(0)
timer.init(period=100, mode=Timer.PERIODIC, callback=timer_interrupt)

#UART
# def rx_interrupt():
#     UART.flush
#     led.value(not led.value())
    
uart = UART(1, baudrate=115200, tx=1, rx=3)#Using same Pines as the UART0 with different UART(1)
# Attach the interrupt handler to the UART RX IRQ
# uart.irq(trigger=uart.RX_ANY, handler=rx_interrupt)


reading = sensor.read()
while True:
    oled.text(str(reading), 0, 10)
    oled.show()
    oled.fill(0)
    if uart.any():
        data = uart.read()
        uart.write('Recibido: \n')
        uart.write(data)
        led.value(not led.value())
