import RPi.GPIO as GPIO

import time
#모터핀
pin = 18


GPIO.setmode(GPIO.BCM)
#모터
GPIO.setup(pin, GPIO.OUT)
SERVO = GPIO.PWM(pin, 50)
SERVO.start(0)

try:
        while True:
                SERVO.ChangeDutyCycle(1)
                print("1")
                time.sleep(1)
                SERVO.ChangeDutyCycle(2)
                print("2")
                time.sleep(1)
                SERVO.ChangeDutyCycle(3)
                print("3")
                time.sleep(1)
                SERVO.ChangeDutyCycle(4)
                time.sleep(1)
                SERVO.ChangeDutyCycle(5)
                time.sleep(1)
                SERVO.ChangeDutyCycle(6)
                time.sleep(1)
                SERVO.ChangeDutyCycle(7)
                time.sleep(1)
                SERVO.ChangeDutyCycle(8)
                time.sleep(1)
                SERVO.ChangeDutyCycle(9)
                time.sleep(1)
                SERVO.ChangeDutyCycle(10)
                time.sleep(1)
                


except KeyboardInterrupt:
        SERVO.stop()
GPIO.cleanup()

