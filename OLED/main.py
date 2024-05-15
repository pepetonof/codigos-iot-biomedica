from machine import Pin, ADC, SoftI2C, Timer
from time import sleep
import ssd1306

sensor = ADC(Pin(4))
sensor.width(ADC.WIDTH_10BIT)## 10 bits
sensor.atten(ADC.ATTN_11DB)##Full range voltage 3.3V

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def timer_interrupt(t):
    global reading
    reading = sensor.read()

timer = Timer(-1)
timer.init(period=500, mode=Timer.PERIODIC, callback=timer_interrupt)

reading = sensor.read()

while True:
    oled.text('Sensor Value', 0, 0)
    oled.text(str(reading), 0, 10)
    oled.show()
    oled.fill(0)
    



