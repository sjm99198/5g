from flask import Flask

import RPi.GPIO as GPIO
import time
import request
from flask import Flask
#
pin = 18


GPIO.setmode(GPIO.BCM)
#
GPIO.setup(pin, GPIO.OUT)
SERVO = GPIO.PWM(pin, 50)
SERVO.start(0)

####################################################################################
def func_N(dc):
        SERVO.ChangeDutyCycle(dc)
####################################################################################



####################################################################################
app = Flask(__name__)
@app.route('/')
def index():
    p_val = request.args.get('p_val','0')
    return func_N(p_val)

print(__name__)
if __name__ == '__main__':
    app.run(host='192.168.0.78', port=8090, debug=False)
####################################################################################
