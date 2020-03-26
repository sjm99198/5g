import requests

#비 센서사용=지문인식결과 전송 코드
params ={'match':'1'}
url = 'http://192.168.0.78:5050/match'
r =requests.get(url,params=params)
r.content