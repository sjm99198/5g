import RPi.GPIO as GPIO
import tkinter as tk
import time
#모터핀
pin = 18


GPIO.setmode(GPIO.BCM)
#모터
GPIO.setup(pin, GPIO.OUT)
SERVO = GPIO.PWM(pin, 50)
SERVO.start(0)

#윈도우 오브젝트
window = tk.Tk()
#윈도우 사이즈
window.geometry('300x300')
angle_value = tk.DoubleVar()
angle_value.set(0)
####################################################################################
def change_angle(dc):
        SERVO.ChangeDutyCycle(angle_value.get())

####################################################################################

#슬라이드 객체
#레이블 숫자범위

slide= tk.Scale(window, label='angle',orient='h', 
    from_=2.5, to=12.5, variable=angle_value, command=change_angle)
#위치설정
slide.pack()

window.mainloop()

SERVO.stop()

GPIO.cleanup()

