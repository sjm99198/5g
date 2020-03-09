import RPi.GPIO as GPIO

import time

#센서핀
pir_R=25
pir_L=23
#모터핀
pin = 16


GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_R, GPIO.IN)
GPIO.setup(pir_L, GPIO.IN)

#모터
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0

#모터함수 설정
def moterR():
        print('R On!!')
        p.ChangeDutyCycle(1)
        
        time.sleep(1)
        p.ChangeDutyCycle(5)
        
        time.sleep(1)
        p.ChangeDutyCycle(8)
        
        time.sleep(1)

def moterL():
        print('L On!!')
        p.ChangeDutyCycle(1)
        
        time.sleep(1)
        p.ChangeDutyCycle(5)
        
        time.sleep(1)
        p.ChangeDutyCycle(8)
        
        time.sleep(1)







try:
    
    while True:
        
        if GPIO.input(pir_R) == True and GPIO.input(pir_L) == True:
            print('Sensor R and L On!!')
            time.sleep(3)
            
        elif GPIO.input(pir_R) == True and  GPIO.input(pir_L) == False:
            print('Sensor R On!!')
            moterR()
            time.sleep(3)
        elif GPIO.input(pir_R) == False and  GPIO.input(pir_L) == True:
            print('Sensor L On!!')
            moterL()
            time.sleep(3)
        else:
            print('Sensor Off!!')
            
            
except KeyboardInterrupt:
    GPIO.cleanup()




