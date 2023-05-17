import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setmode(GPIO.BCM)

for i in dac: GPIO.setup(i, GPIO.OUT)
for i in range(len(dac)): GPIO.output(dac[i], number[i])
time.sleep(15)

for i in dac: GPIO.output(i, 0)
GPIO.cleanup()

"""
255     3.250
127     1.622
64      0.822
32      0.498
5       0.483
0       0.483
256     -
"""