#coding: utf-8

#picamera라이브러리 임포트
import datetime
import time
import picamera
with picamera.PiCamera() as camera

f = open("picamerOption.txt", 'r')
setting = f.readline()
print(setting)
f.close()
camera.resolution = settingcon
now= datetime.datetime.now()
#파일명 입력받기
file_name = '{}{}{}{}{}{}{}.jpg'.format(
    now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond
    )
#프리뷰화면 표시
camera.start_preview()
time.sleep(1)
camera.capture(file_name)