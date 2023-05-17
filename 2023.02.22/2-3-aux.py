import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

GPIO.setmode(GPIO.BCM)

for i in leds: GPIO.setup(i, GPIO.OUT)
for i in aux: GPIO.setup(i, GPIO.IN)

while 1:
    for i in range(len(leds)):
        GPIO.output(leds[i], GPIO.input(aux[i]))

