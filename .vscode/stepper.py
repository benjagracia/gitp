import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)

GPIO.output(12, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)








time.sleep(3)

GPIO.output(18, GPIO.LOW)
GPIO.cleanup()