import RPi.GPIO as GPIO

import time
#모터핀
pin = 5


GPIO.setmode(GPIO.BCM)
#모터
GPIO.setup(pin, GPIO.OUT)
SERVO = GPIO.PWM(pin, 50)
SERVO.start(0)


#12.5= 180도 7.5=90도 2.5=0도

for i in range(1,60):
    SERVO.ChangeDutyCycle(8-(2+i*0.1))
    time.sleep(0.05)
print("opentest")
time.sleep(3)


SERVO.stop()
GPIO.cleanup()