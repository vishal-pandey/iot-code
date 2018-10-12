import requests
import RPi.GPIO as GPIO
from time import sleep

#r = requests.get("https://iot.vishalpandey.xyz").text
#print(r)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT, initial=GPIO.LOW)

while 1:
	r = requests.get("https://iot.vishalpandey.xyz").text
	print(r)
	if r=='1':
		GPIO.output(5,GPIO.HIGH)

	else :
		GPIO.output(5,GPIO.LOW)

