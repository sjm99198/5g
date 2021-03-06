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
GPIO.setup(pin3,GPIO.OUT,initial=GPIO.LOW)

#회전의 강도 
p1= GPIO.PWM(pin1,100)
p2= GPIO.PWM(pin2,100)

alock = GPIO.PWM(pin3, 50)


#문을 자동으로 열고 닫는 기능 함수
###################################################################################
def opendoor ():
    p1.start(22)
    time.sleep(5)
    p1.stop()
    time.sleep(10)
###################################################################################
def closedoor():
    p2.start(22)
    time.sleep(5)
    p2.stop()
###################################################################################
#잠금장치 모터 구동 기능 함수
###################################################################################
def locking():
    alock.start(0)
    alock.ChangeDutyCycle(2.5)
    time.sleep(1)
###################################################################################
def unlocking():
    alock.start(0)
    alock.ChangeDutyCycle(12.5)
    time.sleep(1)
###################################################################################