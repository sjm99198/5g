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
time.sleep(3)
IO.output(dirPin, True)   
print('10')
p.ChangeDutyCycle(10)
time.sleep(5)




p.stop(0)
IO.output(dirPin, False)

