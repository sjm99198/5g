import RPi.GPIO as GPIO

import time
#모터핀
pin = 18


GPIO.setmode(GPIO.BCM)
#모터
GPIO.setup(pin, GPIO.OUT)
SERVO = GPIO.PWM(pin, 50)
SERVO.start(0)


#12.5= 180도 7.5=90도 2.5=0도
try:
        while True:
                SERVO.ChangeDutyCycle(7.5)
                print("opentest")
                time.sleep(3)
                
                


except KeyboardInterrupt:
        SERVO.stop()
GPIO.cleanup()

