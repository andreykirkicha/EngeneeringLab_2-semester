import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for value in range(256):
        signal = decimal2binary(value)
        GPIO.output(dac, signal)
        time.sleep(0.001)
        compValue = GPIO.input(comp)
        if compValue == 0:
            break
    return value

try:
    while (1): 
        value = adc()
        print("ADC value = ", value, "\nVoltage = ", value / 255 * 3.3, " V\n\n")

except ValueError:
    print("Value is not integer\n")

finally:
    for i in range(len(dac)): GPIO.output(dac[i], 0)
    GPIO.cleanup()
