from pyfirmata import Arduino,SERVO, util
import servo1
from time import sleep
port="COM6"
pin=5
board=Arduino(port)
board.digital[pin].mode=SERVO
def rotateservo(pin,angle):
	board.digital[pin].write(angle)
	sleep(0.015)
while True:
    #x=input("gir:")
    #if x=="1":
    rotateservo(pin,180)
    #elif x=="2":
        #for i in range(0,90):
            #rotateservo(pin,i)
    #elif x=="3":
        #for i in range(0,270):
            #rotateservo(pin,i)