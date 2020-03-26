#from flask import Falsk, render_template
from flask import request
from flask_cors import CORS

import requests
import logging
import datetime
import time

import Adafruit_DHT
import RPi.GPIO as GPIO
#############################################################
# 지문인식 센서 감지 log 남기기
date = str(datetime.date.today())

logger = logging.getLogger('temperaturelog')
hand = logging.FileHandler('tempHumid-'+date+'.log')


#                              생성시간,   로그레벨 ,       프로세스ID,   메시지
formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s')

# 파일핸들러에 문자열 포메터를 등록
hand.setFormatter(formatter)

logger.addHandler(hand)

logger.setLevel(logging.INFO)


###############################################################

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

A = 17 #모터 A핀
B = 27 #모터 B핀

start_btn = 6 #선풍기 on/off 버튼


#A,B GPIO setup설정
GPIO.setup(A,GPIO.OUT,initial=GPIO.LOW) 
GPIO.setup(B,GPIO.OUT,initial=GPIO.LOW)
#GPIO.setup(start_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(start_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#온습도센서
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 19


#회전의 강도
def strength(state):
    if state == 'strong_wind':
        print("very hot!! strong wind start")
        p1=GPIO.PWM(A,30) # 모터 각도(?)
        p2=GPIO.PWM(B,30) # 모터 각도(?)
        p1.start(40) # 모터 세기.. 즉, 바람의 강도
        time.sleep(10) # 온도 인식 후, 10초간 강풍으로 불겠다는 거~~ => 시간설정 자유로 가능

        return 'strong_wind'

    elif state == 'weak_wind':
        print("so so... weak wind start")
        p1=GPIO.PWM(A,10) # 모터 각도(?)
        p2=GPIO.PWM(B,10) # 모터 각도(?)
        p1.start(20) #m 모터 세기.. 즉, 바람의 강도
        time.sleep(10) # 온도 인식 후, 10초간 약풍으로 불겠다는 거~~ => 시간설정 자유로 가능


        return 'weak_wind'
    
    elif state == 'no_wind':
        print("no wind. because of low temperature")
        p1=GPIO.PWM(A,0.1)
        p2=GPIO.PWM(B,0.1)
       # p1.start(0.1) 
        time.sleep(10) # 온도 인식 후, 온도가 낮으니, 모터가 안돌아감~ 바람 안불겠다는 거~~ => 시간설정 자유로 가능


        return 'no_wind'


def dht11():
    #while 1:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
            logger.info("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))

            if(temperature >= 30.0):
                strength('strong_wind')
                print("온도를 재측정합니다.")
                
            elif(temperature >= 27.0 and temperature < 30.0):
                strength('weak_wind')
                print("온도를 재측정합니다.")
                
            elif(temperature < 27.0):
                strength('no_wind')
                print("온도를 재측정합니다.")
                
        else:
            print("Sensor failure. Check again. ");
            
        time.sleep(0.5);

#def dht_none():
    #val = None

        
        

def dht_start():
    while 1:
        dht11()



while 1:

    if GPIO.input(start_btn) == 1:     #버튼을 눌렀을 때, 선풍기가 꺼짐....근데 이미 선풍기가 돌아갔다면, 온도 재측정까지 시간은 기다려야함 ㅠㅠ
         print("oh no...good bye..")
         GPIO.output(A,GPIO.LOW)
         GPIO.output(B,GPIO.LOW)
    
    elif GPIO.input(start_btn) == 0: #버튼을 안눌렀을 때, 선풍기는 자동으로 계속 실행이 된다.
        print("oh yes! smart fan start!")
        dht11()
  

GPIO.cleanup()
