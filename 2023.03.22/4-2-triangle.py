import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

x = 0

try:
    per = int(input())
    while (1):
        while (x < 255):
            for i in range(len(dac)): GPIO.output(dac[i], dec2bin(x)[i])
            time.sleep(per / 256 / 2)
            x += 1
        while (x > 0):
            for i in range(len(dac)): GPIO.output(dac[i], dec2bin(x)[i])
            time.sleep(per / 256 / 2)
            x -= 1

finally:
    for i in range(len(dac)): GPIO.output(dac[i], 0)
    GPIO.cleanup()
