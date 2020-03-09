# coding: utf-8

#flask 라이브러리 요청
from flask import Flask

#CORS
from flask_cors import CORS

# request param 처리를위한 요청
from flask import request


#GPIO 라이브러리 임포트
import RPi.GPIO as GPIO
import datetime
import time
import picamera

####################################################

# 핀번호 할당으로 처리 : 핀번호 설정 
GPIO.setmode(GPIO.BCM)

# 핀번호 설정 : chanel
SERVOR1 = 18  # 모터1

# 11번 핀 출력 핀으로 등록, 초기 출력은 LOW = 0  False
GPIO.setup(SERVOR1, GPIO.OUT )


#pwm객체 인스턴스
#출력핀:18 주파수 50Hz
p = GPIO.PWM(SERVOR1, 50)
#PWM 신호 출력
p.start(0)

#duty값을 변경 항수
#####################################################
def change_duty(dc):
    p.ChangeDutyCycle(dc)

#####################################################
#############################################################################
#카메라 함수 설정
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
################################################################################



#변수설정
app = Flask(__name__)
CORS(app)

@app.route('/shot1')
def shot1():
    return securityshot()


@app.route('/')
def index():

    moter = request.args.get('moter', 'm')
    p_val = request.args.get('p_val','0')
    change_duty(int(p_val))
        
    return moter + ':' + p_val

if __name__ ==  '__main__':
    app.run(host='192.168.0.60',port="5060")
    