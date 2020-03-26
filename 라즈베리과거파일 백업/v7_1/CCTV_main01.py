#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import 
import time
import RPi.GPIO as GPIO
import datetime
import picamera
import logging
#import requestsp-start

#from flask import Flask
import CCTV_module_06_solo as k
#모둘 불러오기
from CCTV_module_06_solo import securityshot, securityrec, setroading

#핀 넘버링을 BCM 방식을 사용한다.
GPIO.setmode(GPIO.BCM)
 
# HC-SR04의 트리거 핀8을 GPIO 17번, 에코핀을 GPIO 27번에 연결한다.
GPIO_TRIGGER = 21
GPIO_ECHO = 25

acc = 1


now = datetime.datetime.now()

print("Ultrasonic Distance Measurement")
 
# 초음파를 내보낼 트리거 핀은 출력 모드로, 반사파를 수신할 에코 피은 입력 모드로 설정한다.
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) 
GPIO.setup(GPIO_ECHO,GPIO.IN)
#############################################################################
date = str(datetime.date.today())

logger = logging.getLogger('CCTVlog')
hand = logging.FileHandler('CCTV-'+date+'.log')


#                              생성시간,   로그레벨 ,       프로세스ID,   메시지
formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(process)d %(message)s')

# 파일핸들러에 문자열 포메터를 등록
hand.setFormatter(formatter)

logger.addHandler(hand)

logger.setLevel(logging.INFO)
#############################################################################
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
                logger.info("1st cheking(shot): Distance={}cm ".format(distance))
                #10~30거리의 진입시 발생하는 이벤트
                settingoption = k.setroading()
                print(settingoption)
                time.sleep(0.001)
                #스냅샷기능
                securityshot(settingoption)
                print(settingoption)
                print('shot')
            elif distance <= 10:
                logger.info("2nd cheking(Video): Distance={}cm ".format(distance))
                #10거리 진입시 발생하는 이벤트
                settingoption = k.setroading()
                print(settingoption)                
                time.sleep(0.001)
                #녹화기능
                securityrec(settingoption)
                print(settingoption)
                print('rec')

except KeyboardInterrupt:   
    print("Ultrasonic Distance Measurement End")
    GPIO.cleanup()


