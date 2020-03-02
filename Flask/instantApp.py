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
pin = 18  # 서보모터 18핀


# 11번 핀 출력 핀으로 등록, 초기 출력은 LOW = 0  False
GPIO.setup(pin, GPIO.OUT)
SERVO = GPIO.PWM(pin, 50)
SERVO.start(0)



#duty값을 변경 항수
def change_duty(dc):
    SERVO.ChangeDutyCycle(dc)








#####################################################
#컨트롤 url ~:5000/?(색상)=red&p_val=밝기(숫자0~100)


#변수설정
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():

    led = request.args.get('SERVO', '1')
    p_val = request.args.get('p_val','0')

    change_duty(int(p_val))

        

    return led + ':' + p_val

if __name__ ==  '__main__':
    app.run(host='192.168.0.60',port="5005")