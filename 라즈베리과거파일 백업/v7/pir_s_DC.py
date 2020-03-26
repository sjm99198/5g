import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

LED=16
pir_s=13


GPIO.setup(LED, GPIO.OUT)
GPIO.setup(pir_s, GPIO.IN)

try:
    
    while True:
        if GPIO.input(pir_s) == True:
            print('Sensor On!!')
            GPIO.output(LED, True)
            time.sleep(5)
        else:
            print('Sensor Off!!')
            GPIO.output(LED, False)
    
except KeyboardInterrupt:
    GPIO.cleanup()




