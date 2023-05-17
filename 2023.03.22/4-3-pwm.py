import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 1000)
p.start(0)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while (1):
        x = int(input("Intput coefficient:  "))
        p.ChangeDutyCycle(x)
        print(x * 3.3 / 100)

finally:
    GPIO.output(18, 0)
    GPIO.cleanup()
