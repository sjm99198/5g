#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import 
import time
import datetime
import requests
import json
import CCTV_module as Wp

from flask_cors import CORS 
from flask import Flask, request


now = datetime.datetime.now()
app = Flask(__name__)

#Cross origins 이슈 해결
CORS(app)



@app.route('/CCTV2')

def cctvrec():
    file_name3 = Wp.securityshot()
    #result = Ws.outputScreen()
    
    #파일명 출력
    print(file_name3)
    
    #서버 url
    url = 'http://192.168.0.23:8080/smarthome/styler/write'
    #파일 열기
    files = {'photo':open(file_name3,'rb')}
    r = requests.post(url, files=files)
    r.text
    print(r.text)
    print(__name__)

if __name__ == '__main__':
    app.run(host='192.168.0.78', port=5000, debug=False)