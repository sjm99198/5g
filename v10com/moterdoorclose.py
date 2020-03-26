import RPi.GPIO as GPIO

import time
#모터핀
pin = 5


GPIO.setmode(GPIO.BCM)
#모터
GPIO.setup(pin, GPIO.OUT)
SERVO2 = GPIO.PWM(pin, 50)



#12.5= 180도 7.5=90도 2.5=0도

###############################
def opendoor():
    SERVO2.start(0)
    for i in range(1,50):
        SERVO2.ChangeDutyCycle(2+i*0.12)
        time.sleep(0.07)
    print("opendoor module")
    time.sleep(3)
##############################
def closedoor():
    SERVO2.start(0)
    for i in range(1,50):
        SERVO2.ChangeDutyCycle(8-(2+i*0.12))
        time.sleep(0.07)
    print("closedoor module")
    time.sleep(3)
##############################





