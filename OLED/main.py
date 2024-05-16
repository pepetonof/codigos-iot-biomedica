from time import sleep
from random import randint
from machine import Pin, UART, ADC, SoftI2C, Timer
import ssd1306 #OLED library
from time import sleep


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
    #uart.writechar(H)
    #uart.writechar(L)
    while uart.txdone():
        uart.write(str(reading)+'\n')
#         uart.write(b)
#     while uart.txdone():
#         uart.write(str(reading)+'\n')
#     while uart.txdone():
#         uart.write(str(reading)+'\n')
#     while uart.txdone():
#         uart.write(str(reading)+'\n')
    

#Timer 
timer = Timer(0)
timer.init(period=1000, mode=Timer.PERIODIC, callback=timer_interrupt)

#UART
# def rx_interrupt():
#     led.value(not led.value())
uart = UART(1, baudrate=115200, tx=1, rx=3)#Using same Pines as the UART0 with different UART

# Attach the interrupt handler to the UART RX IRQ
#uart.irq(trigger=UART.RX_ANY, handler=on_uart_rx)

#Pin 2 with LED
led = Pin(2, Pin.OUT)

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
