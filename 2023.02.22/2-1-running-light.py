import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)

for i in leds:
    GPIO.setup(i, GPIO.OUT)

while 1:
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)