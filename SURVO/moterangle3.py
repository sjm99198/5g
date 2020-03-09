from flask import Flask

import RPi.GPIO as GPIO
import time
from flask import Flask
#
pin = 18


GPIO.setmode(GPIO.BCM)
#
GPIO.setup(pin, GPIO.OUT)
SERVO = GPIO.PWM(pin, 50)
SERVO.start(0)

####################################################################################
def func_R():
        SERVO.ChangeDutyCycle(12.5)

def func_C():
        SERVO.ChangeDutyCycle(7.5)

def func_L():
        SERVO.ChangeDutyCycle(2.5)

def func_N(dc):
        SERVO.ChangeDutyCycle(dc)
####################################################################################



####################################################################################
app = Flask(__name__)

@app.route('/SR')
def sw_g():
    return func_R()


@app.route('/SC')
def sw_y():
    return func_C()


@app.route('/SL')
def sw_r():
    return func_L()

@app.route('/')
def index():
    p_val = request.args.get('p_val','0')
    return func_N(p_val)

print(__name__)
if __name__ == '__main__':
    app.run(host='192.168.0.60', port=5005, debug=False)
####################################################################################
