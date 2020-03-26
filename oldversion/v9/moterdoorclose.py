import RPi.GPIO as GPIO

import time
#모터핀
pin = 5


GPIO.setmode(GPIO.BCM)
#모터
GPIO.setup(pin, GPIO.OUT)
SERVO = GPIO.PWM(pin, 50)



#12.5= 180도 7.5=90도 2.5=0도
#max=8 min=2
###############################
def opendoor():
    SERVO.start(0)
    print("module: opendoor start")
    for i in range(1,100):
        SERVO.ChangeDutyCycle(2+i*0.06)
        time.sleep(0.05)
    time.sleep(2)
    print("module: opendoor O K ")
##############################
def closedoor():
    SERVO.start(0)
    print("module: closedoor start")
    for i in range(1,100):
        SERVO.ChangeDutyCycle(8-i*0.06)
        time.sleep(0.05)
    time.sleep(2)
    print("module: closedoor o K ")
##############################





