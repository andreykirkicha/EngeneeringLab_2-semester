import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


try:
    while (1): 
        y = input("Input number from 0 to 255:  ")
        if (y == 'q'):
            break
        else:
            y = int(y)
            if (y < 0):
                print("Value is negative\n")
                break
            if (y > 255):
                print("Your value is too large\n")
                break
        for i in range(len(dac)): GPIO.output(dac[i], decimal2binary(y)[i])
        print("Voltage = ", 3.3 * y / 256, "V\n")

except ValueError:
    print("Value is not integer\n")

finally:
    for i in range(len(dac)): GPIO.output(dac[i], 0)
    GPIO.cleanup()
