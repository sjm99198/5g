#-*- coding: utf-8 -*-
#내부 자동문 센서
import RPi.GPIO as GPIO
import time

pin= 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p=GPIO.PWM(pin, 50)
p.start(0)
p.ChangeDutyCycle(2.5)
time.sleep(1)
p.ChangeDutyCycle(7.5)
time.sleep(1)
p.ChangeDutyCycle(12.5)
time.sleep(1)



p.stop
GPIO.cleanup()


