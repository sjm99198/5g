import RPi.GPIO as IO
import RPi.GPIO
import time



pwmPin = 5
dirPin = 6



IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(pwmPin, IO.OUT)
IO.setup(dirPin,IO.OUT)



p = IO.PWM(pwmPin, 100)
p.start(0)




#IO.output(dirPin, True)
#time.sleep(5)
#for x in range (100, 0, -5):
#    p.ChangeDutyCycle(x)
#    time.sleep(0.1)
#time.sleep(1)
#print('Stop and reverse')
IO.output(dirPin, True)   
print('100')
p.ChangeDutyCycle(100)
time.sleep(1)

print('80')
p.ChangeDutyCycle(80)
time.sleep(1)

print('60')
p.ChangeDutyCycle(60)
time.sleep(1)


print('10')
p.ChangeDutyCycle(10)
time.sleep(6)

print('70')
p.ChangeDutyCycle(50)
time.sleep(1)

print('100')
p.ChangeDutyCycle(100)
time.sleep(1)

p.stop(0)
IO.output(dirPin, False)

GPIO.cleanup()
