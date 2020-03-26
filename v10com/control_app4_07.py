# coding: utf-8

#flask 라이브러리 요청
from flask import Flask, request, Response, jsonify, make_response
import pandas as pd
#CORS
from flask_cors import CORS
# request param 처리를위한 요청
from flask import request
from moterdoorclose import opendoor, closedoor
import datetime
import time
import json
import requests
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
        txt="lower"
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
def opening(dc4):
    if dc4 == '1':        
        f = open("cin.txt", 'w')
        f.write("in")
        f.close()
        time.sleep(0.5)
        f3 = open("acces.txt", 'w')
        f3.write("opendoor")
        f3.close()
        time.sleep(0.5)
        f2 = open("door.txt", 'w')
        f2.write("open")
        f2.close()
        time.sleep(3)
        print('openset')
    elif dc4 == '2':
        print('warning')
    elif dc4 == '0':
        print('warning: hacking Error')

########################################################

##########################################################
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
    opening(matchF)
    
    return matchF
##############################################################
@app.route("/log/<cctvDate>", methods =['GET'])
def cctv_log(cctvDate):

    data_dic = cctvDate

    try:
        # 로그파일 불러오기
        df = pd.read_csv("cctv-"+data_dic+".log", sep=' ', \
                    names=['날짜', '시간','로그레벨', '프로세스ID', '라벨', '사진/동영상', '거리', ''], \
                    header=None)
        
        df['사진/동영상'] = df['사진/동영상'].str.replace(
            pat='cheking(', repl='', regex=False)
        df['사진/동영상'] = df['사진/동영상'].str.replace(
            pat='):', repl='', regex=False)

        # '날짜', '시간', '사진/동영상' 컬럼만 output
        cctv_df = df.loc[:, ['날짜', '시간', '사진/동영상']]

        # def color_negative_red(val):
        #     color = 'red' if val == 'Video' else 'black'
        #     return 'color: %s' % color
 
        # cctv_df.style.applymap(color_negative_red)

        return cctv_df.to_html(justify='center')
    except:
        return "Error"
#############################################################
    
if __name__ ==  '__main__':
    app.run(host='192.168.0.78',port="5050")