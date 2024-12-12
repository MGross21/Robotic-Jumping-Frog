# boot.py: Hardware initialization and setup tasks
from machine import I2C, Pin, UART, PWM
import time

# I2C Configuration
I2C1_SDA = Pin(32)
I2C1_SCL = Pin(33)

i2c1 = I2C(1, scl=I2C1_SCL, sda=I2C1_SDA, freq=100000, timeout=200000)
print("I2C Device found at address: ", i2c1.scan(), "\n")

# Servo Configuration
frequency = 50
range_low1 =  50
range_high1 = 122

range_low2 =  28
range_high2 = 100
servo1 = PWM(Pin(13), freq=frequency)
servo2 = PWM(Pin(12), freq=frequency)

# Export variables for use in main.py
def get_hardware():
    return i2c1, servo1, servo2, range_low1, range_high1, range_low2, range_high2