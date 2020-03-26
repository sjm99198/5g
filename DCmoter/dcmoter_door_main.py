import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#전극방향 5번핀 방향으로 출력할것인가 6번 방향으로 출력할것인가
pin1 = 5
pin2 = 6
pin3 = 9
#회전의 강도 
p1= GPIO.PWM(pin1,100)
p2= GPIO.PWM(pin2,100)


#핀 초기갑
GPIO.setup(pin1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pin2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pin3,GPIO.OUT,initial=GPIO.LOW)
alock = GPIO.PWM(pin3, 50)
alock.start(0)


###################################################################################
def opendoor ():
    p1.start(22)
    time.sleep(5)
###################################################################################
def closedoor():
    p2.start(22)
    time.sleep(5)
###################################################################################
def locking():
    alock.ChangeDutyCycle(7.5)
###################################################################################
def unlocking():
    alock.ChangeDutyCycle(12.5)
###################################################################################