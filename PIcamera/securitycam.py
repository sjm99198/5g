# coding: utf-8

#picamera 라이브러리
import picamera
import RPi.GPIO as GPIO
#time 라이브러리
import time
import datetime
#핀설정
pir_s=25
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_s, GPIO.IN)


#카메라 함수 설정
def securityshot ():
#PiCamera 객체 인스턴스 생성
    with picamera.PiCamera() as camera:

#해상도 선택 목록
        camera.resolution = (320, 240)
        now= datetime.datetime.now()
        
#파일명 입력받기-AUTO
        file_name = '{}{}{}{}{}{}{}.jpg'.format(
            now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond
        )
#프리뷰화면 표시
        camera.start_preview()
        camera.capture(file_name)

#센싱 판별
try:
    
    while True:
        
        if GPIO.input(pir_s) == True:
            print('Sensor On!!')
            time.sleep(1)
            securityshot()
            print('shot')
            time.sleep(5)
        else:
            print('Sensor Off!!')
            
    
except KeyboardInterrupt:
    GPIO.cleanup()




