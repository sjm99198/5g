import RPi.GPIO as GPIO
import time



# 핀번호 할당으로 처리 : 핀번호 설정 
GPIO.setmode(GPIO.BCM)

# 핀번호 설정 : chanel
pin = 18  # 서보모터 18핀


# 11번 핀 출력 핀으로 등록, 초기 출력은 LOW = 0  False
GPIO.setup(pin, GPIO.OUT)
SERVO = GPIO.PWM(pin, 50)
SERVO.start(0)

#duty값을 변경 항수
def change_duty(dc):
        SERVO.ChangeDutyCycle(dc)
        time.sleep(1)
        SERVO.