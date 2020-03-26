import RPi.GPIO as GPIO
import time
from dcmoter_door_module import opendoor, closedoor
GPIO.setmode(GPIO.BCM)


LED=16
pir_s=17

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(pir_s, GPIO.IN)

try:
    
    while True:
            if GPIO.input(pir_s) == True:
                print('Sensor On!!')
                
                GPIO.output(LED, True)
               
            
            else:                
                
                
                    
                GPIO.output(LED, False)
    
except KeyboardInterrupt:
    GPIO.cleanup()




