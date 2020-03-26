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
SERVOR1 = 18  # 초록색 LED

# 11번 핀 출력 핀으로 등록, 초기 출력은 LOW = 0  False
GPIO.setup(SERVOR1, GPIO.OUT )


#pwm객체 인스턴스
#출력핀:18 주파수 50Hz
p = GPIO.PWM(SERVOR1, 50)
#PWM 신호 출력
p.start(0)
############################################################################
#duty값을 변경 항수
def change_duty(dc):
    p.ChangeDutyCycle(dc)
############################################################################
#화질셋팅 텍스트 생성
def hw():
    f = open("picamerOption.txt", 'w')
    for i in range(1, 2):
    data = "320"
    f.write(data)
    f.close()
############################################################################
#센서 재시작
def restarting():




#####################################################
#컨트롤 url ~:5000/?(색상)=red&p_val=밝기(숫자0~100)


#변수설정
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():

    moter = request.args.get('moter', 'm')
    p_val = request.args.get('p_val','0')

    change_duty(int(p_val))

        

    return moter + ':' + p_val

@app.route('/set320')
def settinghw():
    hw()

@app.route('/restart')
def rstart():
    hw()


if __name__ ==  '__main__':
    app.run(host='192.168.0.78',port="5050")