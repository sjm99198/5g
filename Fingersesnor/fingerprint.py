###############################################################

# 센서 값 정의하기

import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio
import logging
#############################################################

# 지문인식 센서 감지 log 남기기

logger = logging.getLogger('fingerprintlog')
hand = logging.FileHandler('fingerprintlog_.log')

#                              생성시간,   로그레벨 ,       프로세스ID,   메시지
formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s')

# 파일핸들러에 문자열 포메터를 등록
hand.setFormatter(formatter)

logger.addHandler(hand)

logger.setLevel(logging.INFO)

logger.info('지문 일치')
logger.warning('지문 비일치')   

#############################################################3
RS =18 # RS ~ D7 LED 판 센서
EN =23
D4 =24
D5 =25
D6 =8
D7 =7

enrol=5 # 새로운 지문을 등록하는 버튼

led=26 # 미니 전구

HIGH=1
LOW=0

##############################################################

# GPIO핀 초기화 하기(초기 값으로 설정)

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(RS, gpio.OUT)
gpio.setup(EN, gpio.OUT)
gpio.setup(D4, gpio.OUT)
gpio.setup(D5, gpio.OUT)
gpio.setup(D6, gpio.OUT)
gpio.setup(D7, gpio.OUT)
gpio.setup(enrol, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(led, gpio.OUT)

#############################################################

# 지문인식센서 초기화 하기(초기 값으로 설정)

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
except Exception as e:
    print('Exception message: ' + str(e))
    exit(1)
################################################################

# LED 판 센서 초기화 하기(초기 값으로 설정)

def begin():
  lcdcmd(0x33) 
  lcdcmd(0x32) 
  lcdcmd(0x06)
  lcdcmd(0x0C) 
  lcdcmd(0x28) 
  lcdcmd(0x01) 
  time.sleep(0.0005)
 
def lcdcmd(ch): 
  gpio.output(RS, 0)
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x10==0x10:
    gpio.output(D4, 1)
  if ch&0x20==0x20:
    gpio.output(D5, 1)
  if ch&0x40==0x40:
    gpio.output(D6, 1)
  if ch&0x80==0x80:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
  # Low bits
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x01==0x01:
    gpio.output(D4, 1)
  if ch&0x02==0x02:
    gpio.output(D5, 1)
  if ch&0x04==0x04:
    gpio.output(D6, 1)
  if ch&0x08==0x08:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
  
def lcdwrite(ch): 
  gpio.output(RS, 1)
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x10==0x10:
    gpio.output(D4, 1)
  if ch&0x20==0x20:
    gpio.output(D5, 1)
  if ch&0x40==0x40:
    gpio.output(D6, 1)
  if ch&0x80==0x80:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
  # Low bits
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x01==0x01:
    gpio.output(D4, 1)
  if ch&0x02==0x02:
    gpio.output(D5, 1)
  if ch&0x04==0x04:
    gpio.output(D6, 1)
  if ch&0x08==0x08:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
def lcdclear():
  lcdcmd(0x01)
 
def lcdprint(Str):
  l=0:
  l=len(Str)
  for i in range(l):
    lcdwrite(ord(Str[i]))
    
def setCursor(x,y):
    if y == 0:
        n=128+x
    elif y == 1:
        n=192+x
    lcdcmd(n)

######################################################

# 새로운 지문을 등록하는 함수

def enrollFinger(): 
    lcdcmd(1)
    lcdprint("새로운 지문을 등록합니다.")
    time.sleep(2)
    print('잠시만 기다리세요...')
    lcdcmd(1)
    lcdprint("손가락을 올려두세요.")
    
    while ( f.readImage() == False ): # f.readImage : 센서가 지문을 읽는 것 ! # 지문이 인식되기를 기다림
        pass
    f.convertImage(0x01)
    result = f.searchTemplate()
    positionNumber = result[0] 

    if ( positionNumber >= 0 ):
        print('해당 지문은 이미 존재합니다 : #' + str(positionNumber))
        lcdcmd(1)
        lcdprint("  지문이 이미  ")
        lcdcmd(192)
        lcdprint("  존재합니다.  ")
        time.sleep(2)
        return

    # 새로운 지문이라면, 위 if문 에 안걸린다! 바로 아래 코드 실행.


    print('손가락을 떼세요...') # 지문을 등록시에, 두번 인식을 해서 지문 등록 정확성을 up시킨다.
    lcdcmd(1)
    lcdprint(" 손가락을 떼세요 ")
    time.sleep(2)
    print(' 손가락을 다시 올리도록, 잠시만 기다려 주세요. ')
    lcdcmd(1)
    lcdprint("  손가락을  ")
    lcdcmd(192)
    lcdprint("   다시 올려주세요.   ")
    
    while ( f.readImage() == False ): # 두번째 인식. # 지문이 인식되기를 기다림.
        pass
    f.convertImage(0x02)
    
    if ( f.compareCharacteristics() == 0 ):
        print " 지문이 일치하지 않습니다. "
        lcdcmd(1)
        lcdprint("  지문이 일치하지  ")
        lcdcmd(192)
        lcdprint("   않습니다.  ")
        time.sleep(2)
        return
    
    # 두번째 인식 때, 지문이 일치했다면 위 if문 에 안걸린다! 바로 아래 코드 실행.
    
    f.createTemplate() # 새로운 지문이 완벽히 등록 되었을 때
    positionNumber = f.storeTemplate()
    print('지문이 성공적으로 등록되었습니다.')
    lcdcmd(1)
    lcdprint("저장되었습니다 : " + str(positionNumber))
    print('새로운 지문이 저장되었습니다 : #' + str(positionNumber))
    time.sleep(2)

############################################################## 

# 일치하는 지문을 찾는 함수
def searchFinger():
    try:
        print('잠시만 기다리세요...')
        while( f.readImage() == False ):
            #pass
            time.sleep(.5)
            return
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        
        if positionNumber == -1 :
            print(' Fail! 일치하는 지문이 없습니다.')
            lcdcmd(1)
            lcdprint(" Fail! 일치하는 지문이 없습니다. ")
            logger.warning('지문 비일치')   
            time.sleep(2)
            return
        
        else:
            print(' Success! 일치하는 지문을 찾았습니다 : #' + str(positionNumber))
            lcdcmd(1)
            lcdprint(" Success! 지문을 찾았습니다 : " + str(positionNumber)) 
            logger.info('지문 일치')
            time.sleep(2)
             # 지문이 일치하면, 문이 열리도록 아래에 코드 추가할 예정.
    except Exception as e:
        print('센서 기능이 중지되었습니다.')
        print('예외메세지: ' + str(e))
        exit(1)
    
#####################################################        

# 지문인식센서를 시작할 때

begin() 
lcdcmd(0x01)
lcdprint(" 지문인식 프로그램입니다. ")
time.sleep(3)
lcdcmd(0xc0)
lcdprint(" 프로그램을 시작합니다. ")
time.sleep(3)
flag=0
lcdclear()
while 1:
    gpio.output(led, HIGH) # 지문등록시에만 미니전구 꺼지고, 다른 때엔 항상 켜지게 할 것
    lcdcmd(1)
    lcdprint("손가락을 올려주세요.") # 계속 반복
   
    if gpio.input(enrol) == 0: #새로운 지문을 등록하려면 enrol 버튼을 눌러야 한다.
        gpio.output(led, LOW)
        enrollFinger()

    else:
        searchFinger() # 새로운 지문 등록시 외에..계속 실행되는 함수
