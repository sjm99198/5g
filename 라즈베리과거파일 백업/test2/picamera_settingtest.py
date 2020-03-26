# coding: utf-8

import picamera
import time
import datetime
import CCTV_module_05 as setting

# picamera Object 생성
with picamera.PiCamera() as camera:

    # 해상도 설정
    #camera.resolution = (320, 240)

    # 해상도 선택
    res = setting.settingroad()

    if res == '1':
        camera.resolution = (320, 240)
    elif res == '2':
        camera.resolution = (640, 480)
    else :
        camera.resolution = (1024, 768)
        
    now=datetime.datetime.now()

    file_name =  '{}{}{}{}{}{}{}.jpg'.format(
    now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond
    )
    
    camera.start_preview()

    time.sleep(1)

    camera.stop_preview()

    # 촬영 -> 저장   /home/pi/Desktop/rasp/camera/photo
    camera.capture(file_name)











            
            