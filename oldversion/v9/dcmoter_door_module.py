
import time
import moterdooropen
import moterdoorclose





###################################################################################
def opendoor ():
    moterdooropen
    print('open the door')
    time.sleep(5)
    
    print('Im ready to close sequence:10sc')
    time.sleep(10)
###################################################################################
def closedoor():
    moterdoorclose
    time.sleep(5)
    print('closed door')
