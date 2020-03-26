# coding: utf-8

import Webcam_picture_04 as Wp
import Webcam_screen_03 as Ws

# flask
from flask import Flask, render_template, request

#request
from flask import request

#CORS
from flask_cors import CORS


##################################밑에는 웹에서 처리###########################

app = Flask(__name__)

#Cross origins 이슈 해결
CORS(app)

@app.route('/webcam')
def webcam():
    result, file_name = Wp.outputPicture()
    #result = Ws.outputScreen()
    
    #파일명 출력
    print(file_name)

    #서버 url
    url = ''
    #파일 열기
    files = {'file':open(file_name,'rb')}
    r = request.post(url, files=files)
    r.text
    return result

# @app.route('/webcam', methods=['POST','GET'])
# def webcamPost():
    

@app.route('/webcamView')
def webcamView():
    #result = Wp.outputPicture()
    result = Ws.outputScreen()
    return result

print(__name__)
if __name__ == '__main__':
    app.run(host='192.168.0.66', port=5000, debug=False)
  

