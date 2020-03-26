#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import 
import time
import datetime
import picamera
import requests


#############################################################################
#사진촬영 함수 설정
def securityshot ():
#PiCamera 객체 인스턴스 생성
    with picamera.PiCamera() as camera:

#해상도 선택 목록
        camera.resolution = (320, 240)
        now= datetime.datetime.now()
        
#파일명 입력받기
        file_name2 = '{}{}{}{}{}{}{}.jpg'.format(
            now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond
        )
#프리뷰화면 표시
        camera.start_preview()
        time.sleep(1)
        camera.capture(file_name2)
        return file_name2
################################################################################
################################################################################
#영상 녹화 함수 설정
def securityrec ():
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
    #파일명 입력받기
        file_name3 = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    #프리뷰 화면
        camera.start_preview()
    
    #촬영과 저장
        camera.start_recording(output = file_name3+'.h264')
        camera.wait_recording(5)
        camera.stop_preview()
        camera.stop_recording()
        return file_name3
################################################################################
