#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import 
import time
import datetime
import picamera
import requests
import os

p = 2

#PiCamera 객체 인스턴스 생성
with picamera.PiCamera() as camera:

#해상도 선택 목록
    res = p
    if res == 1:
        camera.resolution = (320, 240)
        print("set:"+p)
    elif res == 2:
        camera.resolution = (640, 480)
        print(p)
    elif res == 3:
        camera.resolution = (1024, 768)
        print('set:'+p)
    elif res == 4:
        camera.resolution = (1280, 960)
        print('set:'+p)
    print('set:'+p)
        
    now= datetime.datetime.now()
        
#파일명 입력받기
    file_name2 = '{}{}{}{}{}{}{}.jpg'.format(
        now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond
    )
#프리뷰화면 표시
    camera.start_preview()
    time.sleep(1)
    camera.capture(file_name2)
#POST

################################################################################
