#coding: utf-8

#picamera라이브러리 임포트
import datetime
import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    #파일명 입력받기
    file_name = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    #프리뷰 화면
    camera.start_preview()

    #촬영과 저장
    camera.start_recording(output = file_name+'.h264')
    camera.wait_recording(5)
    camera.stop_preview()
    camera.stop_recording()