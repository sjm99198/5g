#-*- coding: utf-8 -*-
#내부 자동문 센서
import RPi.GPIO as GPIO
import time
from dcmoter_door_module import opendoor, closedoor, locking, unlocking
GPIO.setmode(GPIO.BCM)


LED=16
pir_s=13

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(pir_s, GPIO.IN)
######################################################
def checkin():
    f = open("cin.txt", 'r')
    k2 = f.readline()
    f.close()
    return k2
######################################################
######################################################
def checkon():
    f = open("cin.txt", 'w')
    f.write("in")
    f.close()
    print('setting option road:in')
######################################################
######################################################
def checkoff():
    f = open("cin.txt", 'w')
    f.write("off")
    f.close()
    print('setting option road:off')
######################################################
try:
    
    while True:
            if GPIO.input(pir_s) == True:
                print('Sensor On!!')
                k2=checkin()
                GPIO.output(LED, True)
                if k2 == 'in':
                    print('in ---------> off')
                    closedoor()
                    locking()
                    time.sleep(5)
                    checkoff()
                elif k2 =='off' :
                    print('off ---------> in')
                    unlocking()
                    opendoor()
                    checkon()
            
            else:
                k2=checkin()
                if k2 == 'in':
                    print('also:in --------> off')
                    closedoor()
                    locking()
                    time.sleep(5)
                    checkoff()
                    
                GPIO.output(LED, False)
    
except KeyboardInterrupt:
    GPIO.cleanup()




