#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import 
import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as GPIO
import datetime
import picamera
import logging

#request
import requests

#핀 넘버링을 BCM 방식을 사용한다.
GPIO.setmode(GPIO.BCM)
 

#서버 URL 설정
url ='http://192.168.0.6:8080/iot/test1.html'

# 지문인식 센서 감지 log 남기기

logger = logging.getLogger('fingerprintlog')
hand = logging.FileHandler('fingerprintlog_.log')
#                              생성시간,   로그레벨 ,       프로세스ID,   메시지
formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s')

# 파일핸들러에 문자열 포메터를 등록
hand.setFormatter(formatter)

logger.addHandler(hand)

logger.setLevel(logging.INFO)

logger.info('지문 일치')
logger.warning('지문 비일치')   
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PIN SET>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
RS =18 # RS ~ D7 LED 판 센서
EN =23
D4 =24
D5 =25
D6 =8
D7 =7

enrol=5 # 새로운 지문을 등록하는 버튼

led=26 # 미니 전구

HIGH=1
LOW=0
# HC-SR04의 트리거 핀을 GPIO 17번, 에코핀을 GPIO 27번에 연결한다.
GPIO_TRIGGER = 21
GPIO_ECHO = 26


# GPIO핀 초기화 하기(초기 값으로 설정)

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(RS, gpio.OUT)
gpio.setup(EN, gpio.OUT)
gpio.setup(D4, gpio.OUT)
gpio.setup(D5, gpio.OUT)
gpio.setup(D6, gpio.OUT)
gpio.setup(D7, gpio.OUT)
gpio.setup(enrol, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(led, gpio.OUT)

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
except Exception as e:
    print('Exception message: ' + str(e))
    exit(1)


################################################################

# LED 판 센서 초기화 하기(초기 값으로 설정)

def begin():
  lcdcmd(0x33) 
  lcdcmd(0x32) 
  lcdcmd(0x06)
  lcdcmd(0x0C) 
  lcdcmd(0x28) 
  lcdcmd(0x01) 
  time.sleep(0.0005)
 
def lcdcmd(ch): 
  gpio.output(RS, 0)
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x10==0x10:
    gpio.output(D4, 1)
  if ch&0x20==0x20:
    gpio.output(D5, 1)
  if ch&0x40==0x40:
    gpio.output(D6, 1)
  if ch&0x80==0x80:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
  # Low bits
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x01==0x01:
    gpio.output(D4, 1)
  if ch&0x02==0x02:
    gpio.output(D5, 1)
  if ch&0x04==0x04:
    gpio.output(D6, 1)
  if ch&0x08==0x08:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
  
def lcdwrite(ch): 
  gpio.output(RS, 1)
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x10==0x10:
    gpio.output(D4, 1)
  if ch&0x20==0x20:
    gpio.output(D5, 1)
  if ch&0x40==0x40:
    gpio.output(D6, 1)
  if ch&0x80==0x80:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
  # Low bits
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x01==0x01:
    gpio.output(D4, 1)
  if ch&0x02==0x02:
    gpio.output(D5, 1)
  if ch&0x04==0x04:
    gpio.output(D6, 1)
  if ch&0x08==0x08:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
def lcdclear():
  lcdcmd(0x01)
 
def lcdprint(Str):
  l=0:
  l=len(Str)
  for i in range(l):
    lcdwrite(ord(Str[i]))
    
def setCursor(x,y):
    if y == 0:
        n=128+x
    elif y == 1:
        n=192+x
    lcdcmd(n)

######################################################



#############################################################################
#사진촬영 함수 설정
def securityshot ():
#PiCamera 객체 인스턴스 생성
    with picamera.PiCamera() as camera:

#해상도 선택 목록
        camera.resolution = (320, 240)
        now= datetime.datetime.now()
        
#파일명 입력받기
        file_name = '{}{}{}{}{}{}{}.jpg'.format(
            now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond
        )
#프리뷰화면 표시
        camera.start_preview()
        time.sleep(1)
        camera.capture(file_name)
#파일전송
        files = {'file':open(file_name,'rb')}
        print(file_name)
        r=requests.post(url,files=files)
        print(r.status_code)

################################################################################
################################################################################
#영상 녹화 함수 설정
def securityrec ():
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        #파일명 입력받기
        file_name = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        #프리뷰 화면
        camera.start_preview()

        #촬영과 저장
        camera.start_recording(output = file_name+'.h264')
        camera.wait_recording(10)
        camera.stop_preview()
        camera.stop_recording()
        #파일전송
        files = {'file':open(file_name+'.h264','rb')}
        print(file_name)
        r=requests.post(url,files=files)
        print(r.status_code)
################################################################################
################################################################################
# 일치하는 지문을 찾는 함수
def searchFinger():
    try:
        print('잠시만 기다리세요...')
        while( f.readImage() == False ):
            #pass
            time.sleep(.5)
            return
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        
        if positionNumber == -1 :
            print(' Fail! 일치하는 지문이 없습니다.')
            lcdcmd(1)
            lcdprint(" Fail! 일치하는 지문이 없습니다. ")
            logger.warning('지문 비일치')   
            time.sleep(2)
            return
        
        else:
            print(' Success! 일치하는 지문을 찾았습니다 : #' + str(positionNumber))
            lcdcmd(1)
            lcdprint(" Success! 지문을 찾았습니다 : " + str(positionNumber)) 
            logger.info('지문 일치')
            time.sleep(2)
             # 지문이 일치하면, 문이 열리도록 아래에 코드 추가할 예정.
    except Exception as e:
        print('센서 기능이 중지되었습니다.')
        print('예외메세지: ' + str(e))
        exit(1)


################################################################################
print("Ultrasonic Distance Measurement")
 
# 초음파를 내보낼 트리거 핀은 출력 모드로, 반사파를 수신할 에코 피은 입력 모드로 설정한다.
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) 
GPIO.setup(GPIO_ECHO,GPIO.IN)
 
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
                securityshot()
                print('shot')
            elif distance <= 10:
                securityrec()
                print('rec')

except KeyboardInterrupt:   
    print("Ultrasonic Distance Measurement End")
    GPIO.cleanup()


# Reset GPIO settings
GPIO.cleanup()