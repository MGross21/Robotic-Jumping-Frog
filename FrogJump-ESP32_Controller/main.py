# # main.py: Main program logic
# from bno08x_i2c import *
from boot import get_hardware
import time

# # Get hardware instances
i2c1, servo1, servo2, range_low1, range_high1, range_low2, range_high2 = get_hardware()

# # Initialize BNO08X sensor
# bno = BNO08X_I2C(i2c1, debug=False)
# print("BNO08x I2C connection: Done\n")

# # Enable necessary sensors
# bno.enable_feature(BNO_REPORT_ACCELEROMETER)
# print("BNO08x sensors enabling: Done\n")

# # Open file for writing
# with open('sensor_data.csv', 'w') as file:
#     # Write CSV header
#     file.write("time,accel_x,accel_y,accel_z,pos_x,pos_y,pos_z\n")

#     # Initialize position and velocity
#     position = [0.0, 0.0, 0.0]  # X, Y, Z positions
#     velocity = [0.0, 0.0, 0.0]  # X, Y, Z velocities

#     # Control variables
#     last_cycle_time = time.ticks_ms()  # Track the start of the motor cycle
#     extend_done = False
#     retract_done = False

#     start_time = time.ticks_ms()
#     while time.ticks_diff(time.ticks_ms(), start_time) < 10e3:  # Log data for 10 seconds
#         current_time = time.ticks_ms()
#         elapsed_time = time.ticks_diff(current_time, last_cycle_time) / 1000.0  # Time since last cycle in seconds

#         # Motor logic
#         if elapsed_time >= 0.5 and not extend_done:  # Extend at 0.5 seconds
#             servo1.duty(range_high1)
#             servo2.duty(range_low2)
#             extend_done = True
#             print("Motor: Extend")

#         if elapsed_time >= 0.75 and not retract_done:  # Retract at 0.75 seconds
#             servo1.duty(range_low1)
#             servo2.duty(range_high2)
#             retract_done = True
#             print("Motor: Retract")

#         if elapsed_time >= 2.0:  # Reset cycle every 2 seconds
#             last_cycle_time = current_time
#             extend_done = False
#             retract_done = False
#             print("Motor: Cycle Reset")

#         # Get acceleration data
#         accel_x, accel_y, accel_z = bno.acceleration

#         # Update velocity
#         dt = (time.ticks_diff(current_time, start_time)) / 1000.0  # Time elapsed in seconds
#         velocity[0] += accel_x * dt
#         velocity[1] += accel_y * dt
#         velocity[2] += accel_z * dt

#         # Update position
#         position[0] += velocity[0] * dt
#         position[1] += velocity[1] * dt
#         position[2] += velocity[2] * dt

#         # Write data to file
#         file.write(f"{current_time},{accel_x:.6f},{accel_y:.6f},{accel_z:.6f},"
#                    f"{position[0]:.6f},{position[1]:.6f},{position[2]:.6f}\n")
#         file.flush()

#         # Print position for debugging
#         print(f"Position: X={position[0]:.6f} m, Y={position[1]:.6f} m, Z={position[2]:.6f} m")

# # Return Servos to starting Position
# servo1.duty(range_high1)
# servo2.duty(range_low2)
# print("Data logging complete. File saved as 'sensor_data.csv'.")




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