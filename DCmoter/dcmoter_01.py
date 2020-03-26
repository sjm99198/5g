import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)

pin1 = 6
pin2 = 5

GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin1,GPIO.OUT)

try:
    while True:

        GPIO.output(pin1, True)
        GPIO.output(pin2, False)
        print('moter on, pin1')

        
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()