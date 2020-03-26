import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
acces = 0
statement = 1
alam = 0

#전극방향 5번핀 방향으로 출력할것인가 6번 방향으로 출력할것인가
pin1 = 5
pin2 = 6
#회전의 강도 
p1= GPIO.PWM(pin1,100)
p2= GPIO.PWM(pin2,100)


#핀 초기갑
GPIO.setup(pin1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(pin2,GPIO.OUT,initial=GPIO.LOW)


try
    while True:
        if acces == 0:
            p1.start(22)
            print('acces_opene')
            time.sleep(10)
            print('acces_opening')
            statement = 0
            return statement
        elif acces == 1:
            p2.start(22)
            print('acces_close')
            time.sleep(10)
            print('acces_closing')
            statement = 1
            return statement
        elif acces == 2:
            print('none_acces')
            alam = 1
            if statement == 0:
                p2.start(22)
                print('Warning close')
                statement = 1
                return statement 
            return alam


except KeyboardInterrupt:   
    print("Door Auto is OFF")
    GPIO.cleanup()