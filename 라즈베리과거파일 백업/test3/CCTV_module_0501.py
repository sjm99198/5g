#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import 
import time
import datetime
import picamera
import requests
import os
import CCTV_main01 as setting





#############################################################################
#사진촬영 함수 설정
def securityshot ():
#PiCamera 객체 인스턴스 생성
    with picamera.PiCamera() as camera:

#해상도 선택 목록
        res = setting
        if res == 1:
            camera.resolution = (320, 240)
        elif res == 2:
            camera.resolution = (640, 480)
        elif res == 3:
            camera.resolution = (1024, 768)
        else:
            camera.resolution = (1280, 960)
        print('modulesetshot:'+setting)
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
        print('uploadin')
        url = 'http://192.168.0.23:8080/smarthome/cctv/write'
        files = {'cctv':open(file_name2,'rb')}        
        data = {'cctvType': 'p'}
        requests.post(url, data=data, files=files)
################################################################################
################################################################################
#영상 녹화 함수 설정
def securityrec ():
    with picamera.PiCamera() as camera:
        res = setting
        if res == 1:
            camera.resolution = (320, 240)
        elif res == 2:
            camera.resolution = (640, 480)
        elif res == 3:
            camera.resolution = (1024, 768)
        print('modulesetrec:'+setting)
    #파일명 입력받기
        file_name3 = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    #프리뷰 화면
        camera.start_preview()
    
    #촬영과 저장
        camera.start_recording(output = file_name3+'.h264')
        camera.wait_recording(5)
        camera.stop_preview()
        camera.stop_recording()
        
        path=os.getcwd()
        print(path)
        a = file_name3
        os.system('MP4Box -add {}.h264 {}.mp4'.format(a,a))
        
    #POST
        url = 'http://192.168.0.23:8080/smarthome/cctv/write'
        files = {'cctv':open(file_name3+'.mp4','rb')}
        data = {'cctvType': 'v'}
        requests.post(url, data=data, files=files)
################################################################################
