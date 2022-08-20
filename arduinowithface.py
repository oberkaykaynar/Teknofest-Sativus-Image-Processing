import cv2
from pyfirmata import Arduino,SERVO, util
from time import sleep
#Haar cascade classifier yukle
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#kamera okumak icin
video_capture = cv2.VideoCapture(0)

port="COM6"
pin=5
board=Arduino(port)
board.digital[pin].mode=SERVO

def rotateservo(pin,angle):
	board.digital[pin].write(angle)
	sleep(0.015)

def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min) #arduino map komutu gibi


#board = Arduino('COM6')  # Change to your port
#lenPin = board.get_pin('d:5:p')  # PWM Pin

print("Starting to output PWM signal")
while True:
	ret,frame = video_capture.read() #frame oku
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #siyah-beyaz yap
	faces = faceCascade.detectMultiScale(gray, 1.1, 5, minSize=(100,100)) #yuzleri bul

	for (x,y,w,h) in faces: #yuzleri isaretle
		p = _map(x, 1, 509, 1, 180)
		print(p)
		rotateservo(pin,p)

		#servo.move(5,180)
		#lenPin.write(n)

		a=cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0) ,2)
		b=cv2.putText(frame, "berkay", (x,y+h+20), cv2.FONT_HERSHEY_DUPLEX, .5, (0,255,0)) #matriks olarak videonun sayısal karşılığını veriyor

	#esc ile cik
	cv2.imshow('Video', frame)

	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

video_capture.release()
cv2.destroyAllWindows()