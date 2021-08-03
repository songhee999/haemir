import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
SERVO = 16
GPIO.setup(SERVO, GPIO.OUT)
SERVO_PWM = GPIO.PWM(SERVO,50)
SERVO_PWM.start(0)

try:
while(True):
	SERVO_PWM.ChangeDutyCycle(5)
	time.sleep(3)
	SERVO_PWM.ChangeDutyCycle(7.5) 
	time.sleep(3)
	SERVO_PWM.ChangeDutyCycle(10)
	time.sleep(3)

finally:
	SERVO_PWM.stop()
	GPIO.cleanup()