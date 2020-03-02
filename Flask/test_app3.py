# coding: utf-8

#flask 라이브러리 요청
from flask import Flask

#CORS
from flask_cors import CORS

# request param 처리를위한 요청
from flask import request


#GPIO 라이브러리 임포트
import RPi.GPIO as GPIO


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



#변수설정
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():

    moter = request.args.get('moter', 'm')
    p_val = request.args.get('p_val','0')
    change_duty(int(p_val))
        
    return moter + ':' + p_val

if __name__ ==  '__main__':
    app.run(host='192.168.0.60',port="5050")
    