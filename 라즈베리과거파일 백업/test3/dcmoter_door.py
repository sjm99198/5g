import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#전극방향 5번핀 방향으로 출력할것인가 6번 방향으로 출력할것인가
pin1 = 5
pin2 = 6


#핀 초기갑
GPIO.setup(pin1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pin2,GPIO.OUT,initial=GPIO.LOW)
#회전의 강도 
p1= GPIO.PWM(pin1,20)
p2= GPIO.PWM(pin2,20)




p1.start(30)
print('p1.20')
time.sleep(1)
p1.stop()
time.sleep(1)
p2.start(30)
print('p2.20')
time.sleep(1)
p2.stop()

#GPIO개방
GPIO.cleanup()