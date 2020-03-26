import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#전극방향 5번핀 방향으로 출력할것인가 6번 방향으로 출력할것인가
pin1 = 5
pin2 = 6]
#회전의 강도 
p= GPIO.PWM(pin1,50)
p= GPIO.PWM(pin1,50)


#핀 초기갑
GPIO.setup(pin1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pin2,GPIO.OUT,initial=GPIO.LOW)


p.start(30)
print('30')
time.sleep(1)

p.start(20)
print('20')
time.sleep(1)

p.start(10)
print('10')
time.sleep(1)

p.start(5)
print('5')
time.sleep(1)

p.start(0)
print('0')
time.sleep(1)

#GPIO개방
GPIO.cleanup()