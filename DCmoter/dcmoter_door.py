import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#전극방향 5번핀 방향으로 출력할것인가 6번 방향으로 출력할것인가
pin1 = 5
pin2 = 6]
#회전의 강도 
p1= GPIO.PWM(pin1,100)
p2= GPIO.PWM(pin2,100)


#핀 초기갑
GPIO.setup(pin1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pin2,GPIO.OUT,initial=GPIO.LOW)




p1.start(22)
print('p1.20')
time.sleep(10)

p2.start(22)
print('p2.20')
time.sleep(10)


#GPIO개방
GPIO.cleanup()