import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#전극방향 5번핀 방향으로 출력할것인가 6번 방향으로 출력할것인가
pin1 = 5
pin2 = 6
pin3 = 26


#핀 초기갑
GPIO.setup(pin1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pin2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pin3,GPIO.OUT)

#회전의 강도 
p1= GPIO.PWM(pin1,50)
p2= GPIO.PWM(pin2,50)

alock = GPIO.PWM(pin3, 100)



###################################################################################
def opendoor ():
    p1.start(30)
    print('open the door')
    time.sleep(5)
    p1.stop()
    print('Im ready to close sequence:10sc')
    time.sleep(10)
###################################################################################
def closedoor():
    p2.start(22)
    time.sleep(5)
    p2.stop()
    print('closed door')
###################################################################################
def locking():    
    alock.start(0)
    alock.ChangeDutyCycle(10)
    time.sleep(1)
    print('looking door')
###################################################################################
def unlocking():
    alock.start(0)
    alock.ChangeDutyCycle(22)
    time.sleep(1)
    print('unlocking door')
###################################################################################