import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin1 = 5
pin2 = 6
#p= GPIO.PWM(pin1,50)

GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)


GPIO.output(pin1, True)
GPIO.output(pin2, False)
print('moter on, pin1 3sec F')
time.sleep(3)

GPIO.output(pin1, True)
GPIO.output(pin2, True)
print('moter on, pin1 3sec T')
time.sleep(3)

