import RPi.GPIO as GPIO
import time

trig = 19
echo = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

flag = 0
LED = 21
count = 0

GPIO.output(16,False)
GPIO.output(20,False)
GPIO.output(21,False)

try:
	while True:
		GPIO.output(trig,False)
		time.sleep(0.5)
		
		GPIO.output(trig,True)
		time.sleep(0.0001)
		GPIO.output(trig,False)

		while GPIO.input(echo)==0:
			pulse_start = time.time()

		while GPIO.input(echo)==1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration*17000
		distance = round(distance,2)
		
		if flag==0 :
			standard = distance
			flag = 1

		GPIO.output(LED,True)
		if distance < standard -50 :
			if count == 0 :
				GPIO.output(LED,False)
				LED = 20
				GPIO.output(LED,True)
			count = count + 1
			if count == 10 :
				GPIO.output(LED,False)
				LED = 16
				GPIO.output(LED,True)
				time.sleep(5)
				GPIO.output(LED,False)
				count = 0
				LED = 21
				GPIO.output(LED,True)
		if (distance >= standard -50) & (count !=0) :
			GPIO.output(LED,False)
			count = 0
			LED = 21
			GPIO.output(LED,True)

		print "Distance : ",distance,"cm"

except:
	GPIO.cleanup()


