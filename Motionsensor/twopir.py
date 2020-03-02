import RPi.GPIO as GPIO

import time


pir_R=25
pir_L=23

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_R, GPIO.IN)
GPIO.setup(pir_L, GPIO.IN)
try:
    
    while True:
        
        if GPIO.input(pir_R) == True and GPIO.input(pir_L) == True:
            print('Sensor R and L On!!')
            time.sleep(3)
            
        elif GPIO.input(pir_R) == True and  GPIO.input(pir_L) == False:
            print('Sensor R On!!')
            time.sleep(3)
        elif GPIO.input(pir_R) == False and  GPIO.input(pir_L) == True:
            print('Sensor L On!!')
            time.sleep(3)
        else:
            print('Sensor Off!!')
            
            
except KeyboardInterrupt:
    GPIO.cleanup()




