import requests

url='http://google.com'
response = requests.get(url=url)
print(response.status_code)
print(response.text)