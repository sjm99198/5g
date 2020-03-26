import requests
params ={'match':'1'}
url = 'http://192.168.0.78:5050/match'
r =requests.get(url,params=params)
r.content