#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import 
import time
import RPi.GPIO as GPIO
import datetime
import picamera
from fingerprint_test0 import ac
#request
import requests

#핀 넘버링을 BCM 방식을 사용한다.
GPIO.setmode(GPIO.BCM)
 
# HC-SR04의 트리거 핀을 GPIO 17번, 에코핀을 GPIO 27번에 연결한다.
GPIO_TRIGGER = 21
GPIO_ECHO = 25
#서버 URL 설정
url ='http://192.168.0.6:8080/iot/test1.html'
ac = ac

#############################################################################
#사진촬영 함수 설정
def securityshot ():
#PiCamera 객체 인스턴스 생성
    with picamera.PiCamera() as camera:

#해상도 선택 목록
        camera.resolution = (320, 240)
        now= datetime.datetime.now()
        
#파일명 입력받기
        file_name = '{}{}{}{}{}{}{}.jpg'.format(
            now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond
        )
#프리뷰화면 표시
        camera.start_preview()
        time.sleep(1)
        camera.capture(file_name)
#파일전송
        files = {'file':open(file_name,'rb')}
        print(file_name)
        r=requests.post(url,files=files)
        print(r.status_code)

################################################################################
################################################################################
#영상 녹화 함수 설정
def securityrec ():
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        #파일명 입력받기
        file_name = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        #프리뷰 화면
        camera.start_preview()

        #촬영과 저장
        camera.start_recording(output = file_name+'.h264')
        camera.wait_recording(10)
        camera.stop_preview()
        camera.stop_recording()
        #파일전송
        files = {'file':open(file_name+'.h264','rb')}
        print(file_name)
        r=requests.post(url,files=files)
        print(r.status_code)
################################################################################

print("Ultrasonic Distance Measurement")
 
# 초음파를 내보낼 트리거 핀은 출력 모드로, 반사파를 수신할 에코 피은 입력 모드로 설정한다.
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) 
GPIO.setup(GPIO_ECHO,GPIO.IN)
 
try:
    while True:
        stop = 0
        start = 0
        # 먼저 트리거 핀을 OFF 상태로 유지한다
        GPIO.output(GPIO_TRIGGER, False)
        time.sleep(2)
 
        # 10us 펄스를 내보낸다. 
        # 파이썬에서 이 펄스는 실제 100us 근처가 될 것이다.
        # 하지만 HC-SR04 센서는 이 오차를 받아준다.
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
 
        # 에코 핀이 ON되는 시점을 시작 시간으로 잡는다.
        while GPIO.input(GPIO_ECHO)==0:
            start = time.time()
 
        # 에코 핀이 다시 OFF되는 시점을 반사파 수신 시간으로 잡는다.
        while GPIO.input(GPIO_ECHO)==1:
            stop = time.time()

        # Calculate pulse length
        elapsed = stop-start

        # 초음파는 반사파이기 때문에 실제 이동 거리는 2배이다. 따라서 2로 나눈다.
        # 음속은 편의상 340m/s로 계산한다. 현재 온도를 반영해서 보정할 수 있다.
        # 거리 판별 조건(10cm)이내로 측정시 카메라촬영.
        if (stop and start):
            distance = (elapsed * 34000.0) / 2
            print("Distance : %.1f cm" % distance)
            if 10 < distance <= 30:
                securityshot()
                print('shot')
            elif distance <= 10 and ac == 1 :
                securityrec()
                print('rec')

except KeyboardInterrupt:   
    print("Ultrasonic Distance Measurement End")
    GPIO.cleanup()


# Reset GPIO settings
GPIO.cleanup()