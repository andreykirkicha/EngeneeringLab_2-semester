import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    value = 0
    signal = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        signal[i] = 1
        GPIO.output(dac, signal)
        time.sleep(0.01)
        compValue = GPIO.input(comp)
        if compValue == 0:
            signal[i] = 0

    for i in range(8):
        if (signal[i] == 1):
            value += 2 ** (7 - i)

    return value

try:
    while (1): 
        value = adc() / 32
        for i in range(8):
            if (value > 0):
                GPIO.output(leds[7 - i], 1)
            else:
                GPIO.output(leds[7 - i], 0)
            value -= 1

finally:
    for i in range(len(dac)): GPIO.output(dac[i], 0)
    GPIO.cleanup()
