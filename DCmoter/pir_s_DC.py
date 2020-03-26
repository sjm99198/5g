import RPi.GPIO as GPIO
import time
import finger as match
from dcmoter_door_module import opendoor, closedoor, locking, unlocking
GPIO.setmode(GPIO.BCM)

LED=16
pir_s=13


GPIO.setup(LED, GPIO.OUT)
GPIO.setup(pir_s, GPIO.IN)
print(match)


try:
    
    while True:
        if match == True :
            opendoor()
        else match == False:
            time.sleep(1)
        if GPIO.input(pir_s) == True:
            print('Sensor On!!')
            GPIO.output(LED, True)
            time.sleep(5)
        else:
            print('Sensor Off!!')
            GPIO.output(LED, False)
    
except KeyboardInterrupt:
    GPIO.cleanup()




