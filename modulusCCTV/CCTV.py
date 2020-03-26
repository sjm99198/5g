#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import 
import time
import RPi.GPIO as GPIO
import datetime
import picamera

import modulusCCTV as CCTVmain

#request
import requests

#핀 넘버링을 BCM 방식을 사용한다.
GPIO.setmode(GPIO.BCM)
 
# HC-SR04의 트리거 핀을 GPIO 17번, 에코핀을 GPIO 27번에 연결한다.
GPIO_TRIGGER = 21
GPIO_ECHO = 25

if 10 < distance <= 30:
    securityshot()
    print('shot')
elif distance <= 10:
    securityrec()
    print('rec')

print(distance)