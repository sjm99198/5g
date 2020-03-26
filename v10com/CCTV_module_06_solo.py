#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import 
import time
import datetime
import picamera
import requests
import os

######################################################################
def setroading():
    f = open("picamerOption.txt", 'r')
    k = f.readline()
    print('setting option road:'+k)
    f.close()
    return k
#############################################################################
#사진촬영 함수 설정
def securityshot (p):
#PiCamera 객체 인스턴스 생성
    with picamera.PiCamera() as camera:

#해상도 선택 목록
        res = p
        if res == 'lowest':
            camera.resolution = (320, 240)
            print('set:'+res)
        elif res == 'lower':
            camera.resolution = (640, 480)
            print('set:'+p)
        elif res == 'low':
            camera.resolution = (1024, 768)
            print('set:'+p)
        elif res == 'middle':
            camera.resolution = (1280, 960)
            print('set:'+p)
        elif res == 'high':
            camera.resolution = (1440, 900)
            print('set:'+p)
        elif res == 'higher':
            camera.resolution = (1680, 1050)
            print('set:'+p)
        elif res == 'highest':
            camera.resolution = (1920, 1200)
            print('set:'+p)
        
        print('modulesetshot:'+res)
        
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
################################################################################
#영상 녹화 함수 설정
def securityrec (p):
    with picamera.PiCamera() as camera:
        res = p
        if res == 'lowest':
            camera.resolution = (320, 240)
            print('set:'+res)
        elif res == 'lower':
            camera.resolution = (640, 480)
            print('set:'+p)
        elif res == 'low':
            camera.resolution = (1024, 768)
            print('set:'+p)
        elif res == 'middle':
            camera.resolution = (1280, 960)
            print('set:'+p)
        elif res == 'high':
            camera.resolution = (1440, 900)
            print('set:'+p)
        elif res == 'higher':
            camera.resolution = (1680, 1050)
            print('set:'+p)
        elif res == 'highest':
            camera.resolution = (1920, 1200)
            print('set:'+p)

        
        print('modulesetshot:'+res)
        
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
################################################################################
