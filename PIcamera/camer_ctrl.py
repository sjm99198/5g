#coding: utf-8
#모션센서에 신호-> 사진 자동촬영

#라이블러리 import
import RPi.GPIO as GPIO

import picamera

import time
import datetime

LED=16
pir_s=25

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(pir_s, GPIO.IN)


#파일명 입력받기
file_name = '{}{}{}{}{}{}{}.jpg'.format( now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)


try:
    
    while True:
        
        if GPIO.input(pir_s) == True:
            print('Sensor On!!')
            GPIO.output(LED, True)
            time.sleep(5)
            with picamera.PiCamera() as camera:
#촬영하고 저장 /home/pi/Desktop/rasp/camera/photo
                camera.resolution = (320, 240)
                now= datetime.datetime.now()
                camera.capture(file_name)
            

        else:
            print('Sensor Off!!')
            GPIO.output(LED, False)
    
except KeyboardInterrupt:
    GPIO.cleanup()
