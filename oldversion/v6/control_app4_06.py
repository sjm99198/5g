# coding: utf-8

#flask 라이브러리 요청
from flask import Flask

#CORS
from flask_cors import CORS

# request param 처리를위한 요청
from flask import request
from dcmoter_door_module import opendoor

#GPIO 라이브러리 임포트
import RPi.GPIO as GPIO


####################################################

# 핀번호 할당으로 처리 : 핀번호 설정 
GPIO.setmode(GPIO.BCM)

# 핀번호 설정 : chanel
SERVOR1 = 18  # 좌우 모터
SERVOR2 = 12  # 상하 모터
# 11번 핀 출력 핀으로 등록, 초기 출력은 LOW = 0  False
GPIO.setup(SERVOR1, GPIO.OUT )
GPIO.setup(SERVOR2, GPIO.OUT )

#pwm객체 인스턴스
#출력핀:18 주파수 50Hz
p = GPIO.PWM(SERVOR1, 100)
p2 = GPIO.PWM(SERVOR2, 50)
#PWM 신호 출력
p.start(0)
p2.start(0)
#duty값을 변경 항수
def change_duty_p(dc1):
    p.ChangeDutyCycle(dc1)

#####################################################
def change_duty_p2(dc2):
    p2.ChangeDutyCycle(dc2)

#####################################################
def change_duty_p3(dc3):
    print(dc3)
    f=open("picamerOption.txt", 'w')
    if dc3 == 0:
        txt="lowest"
    elif dc3 == 1:
        txt="ower"
    elif dc3 == 2:
        txt= "low"
    elif dc3 == 3:
        txt="middle"
    elif dc3 == 4:
        txt="high"
    elif dc3 == 5:
        txt="higher"
    elif dc3 == 6:
        txt="highest"
    f.write(txt)
    f.close()
########################################################
#변수설정
app = Flask(__name__)
CORS(app)
@app.route('/RL')
def cctvcon():

    moter = request.args.get('moter', 'm')
    p_val = request.args.get('p_val','0')

    change_duty_p(int(p_val)+0.5)

        

    return moter + ':' + p_val

@app.route('/UD/')
def cctvcon2():

    moter2 = request.args.get('moter2', 'm2')
    p_val2 = request.args.get('p_val2','0')

    change_duty_p2(int(p_val2)+0.5)

        

    return moter2 + ':' + p_val2

@app.route('/setting/')
def cctvcon3():

    moter3 = request.args.get('moter3', 'm3')
    p_val3 = request.args.get('p_val3','0')

    change_duty_p3(int(p_val3))

        

    return moter3 + ':' + p_val3

@app.route('/match/')
def matchacces():

    matchF = request.args.get('match', '0')
    print(matchF)
    opendoor()
    return matchF

if __name__ ==  '__main__':
    app.run(host='192.168.0.78',port="5050")