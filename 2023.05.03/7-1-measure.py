import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

tau = 0.005

def adc():
    for value in range(256):
        signal = decimal2binary(value)
        GPIO.output(dac, signal)
        time.sleep(tau)
        compValue = GPIO.input(comp)
        if compValue == 0:
            break
    return value

def leds_output():
    while (1): 
        value = adc() / 32
        for i in range(8):
            if (value > 0):
                GPIO.output(leds[7 - i], 1)
            else:
                GPIO.output(leds[7 - i], 0)
            value -= 1
    return

try:
    value = 0
    mes = []
    t_0 = time.time()
    n = 0

    GPIO.output(troyka, 1)
    while (value < 30):
        value = adc()
        print("ADC value = ", value, "\nVoltage = ", value / 255 * 3.3, " V\n\n")
    
    # пошла зарядка
    GPIO.output(troyka, 0)
    while (value < 250):
        n += 1
        value = adc()
        mes.append(value)
        print("ADC value = ", value, "\nVoltage = ", value / 255 * 3.3, " V\n\n")

    # пошла разрядка
    GPIO.output(troyka, 1)
    while (value > 70):
        n += 1
        value = adc()
        mes.append(value)
        print("ADC value = ", value, "\nVoltage = ", value / 255 * 3.3, " V\n\n")
    
    t = time.time()
    dur = t - t_0
    
    plt.plot(mes)
    plt.show()

    with open('data.txt', 'w', encoding='utf-8') as f_1:
        for item in mes:
            f_1.write(str(item))
            f_1.write('\n')

    with open('settings.txt', 'w', encoding='utf-8') as f_2:
        f_2.write("duration: ")
        f_2.write(str(dur))
        f_2.write(" s\nT: ")
        f_2.write(str(tau))
        f_2.write(" s\nfrequency: ")
        f_2.write(str(1 / dur * n))
        f_2.write(" Hz\nstep: ")
        f_2.write(str(3.3 / 256))

    print("duration: ", dur, " s\nT: ", tau, " s\nfrequency: ", 1 / dur / n, " Hz\nstep: ", 3.3 / 256)

finally:
    for i in range(len(dac)): GPIO.output(dac[i], 0)
    GPIO.cleanup()
