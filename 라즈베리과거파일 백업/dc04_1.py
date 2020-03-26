import RPi.GPIO as IO
import time



pwmPin = 5
dirPin = 6



IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(pwmPin, IO.OUT)
IO.setup(dirPin,IO.OUT)



p = IO.PWM(pwmPin, 100)
p.start(0)



IO.output(dirPin, True)
time.sleep(5)
p.ChangeDutyCycle(0)

p.stop(0)
