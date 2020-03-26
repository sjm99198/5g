#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import 
import time
import RPi.GPIO as GPIO
#import requestsp-start

#from flask import Flask
from moterdoorclose import opendoor, closedoor

#핀 넘버링을 BCM 방식을 사용한다.
GPIO.setmode(GPIO.BCM)
 
# HC-SR04의 트리거 핀8을 GPIO 17번, 에코핀을 GPIO 27번에 연결한다.
GPIO_TRIGGER = 19
GPIO_ECHO = 26


 
# 초음파를 내보낼 트리거 핀은 출력 모드로, 반사파를 수신할 에코 피은 입력 모드로 설정한다.
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) 
GPIO.setup(GPIO_ECHO,GPIO.IN)
###########################################################################
def checkacces():
    f = open("acces.txt", 'r')
    k4 = f.readline()
    f.close()
    print('문확인:'+k4)
    return k4
#############################################################################
def checkman():
    f = open("cin.txt", 'r')
    k2 = f.readline()
    f.close()
    print('사람확인:'+k2)
    return k2
#############################################################################
def checkdoor():
    f = open("door.txt", 'r')
    k3 = f.readline()
    f.close()
    print('문확인:'+k3)
    return k3
############################################################################
def writeopen():
    f = open("door.txt", 'w')
    f.write("open")
    f.close()
    print('openset')
######################################################
def writeclose():
    f = open("door.txt", 'w')
    f.write("close")
    f.close()
    print('closeset')
######################################################
def checkout():
    f = open("cin.txt", 'w')
    f.write("out")
    f.close()
    print('man is out')
######################################################
    
    
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
            if  distance <= 15:
                k2=checkman()
                print('k2:'+k2)
                k3=checkdoor()
                print('k3:'+k3)
                if k2 == 'in' and k3 == 'open':
                    time.sleep(3)
                    closedoor()
                    writeclose()
                elif k2 == 'in' and k3 == 'close':
                    time.sleep(0.2)
                    print('check out')
                    opendoor()
                    time.sleep(15)
                    closedoor()
                    checkout()
                elif k2 == 'out' and k3 == 'open':
                    time.sleep(0.2)
                    closedoor()
                    writeclose()
                    time.sleep(2)
                elif k2 =='out' and k3 == 'close':
                    print('waring!:invade')
                    time.sleep(3)
            else:
                k4=checkacces()
                print('k4:'+k4)
                if k4 == 'opendoor':
                    opendoor()
                    f = open("acces.txt", 'w')
                    f.write("ok")
                    f.close()
                    
                
                



except KeyboardInterrupt:   
    print("Ultrasonic Distance Measurement End")
    GPIO.cleanup()


