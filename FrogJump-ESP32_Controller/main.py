# # main.py: Main program logic
# from bno08x_i2c import *
from boot import get_hardware
import time

# # Get hardware instances
i2c1, servo1, servo2, range_low1, range_high1, range_low2, range_high2 = get_hardware()

from machine import Pin, PWM
from time import sleep, ticks_ms, ticks_diff

frequency = 50
range_low1 = 50
range_high1 = 122

range_low2 = 28
range_high2 = 100

servo1 = PWM(Pin(13), freq=frequency)
servo2 = PWM(Pin(12), freq=frequency)

start_time = ticks_ms()

while ticks_diff(ticks_ms(), start_time) < 10000: 
    servo1.duty(range_high1)
    #sleep(0.09)
    servo2.duty(range_low2)     
    sleep(1)
    servo1.duty(range_low1)
    #sleep(0.09)
    servo2.duty(range_high2)  
    sleep(0.35)
    print("Cycle complete")

servo1.duty(range_high1)
servo2.duty(range_low2)
print("Finished")