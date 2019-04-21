import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
v = 0.001
k = 0
while(k<512):
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    time.sleep(v)
    
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    time.sleep(v)
    
    GPIO.output(18, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    time.sleep(v)
    
    GPIO.output(18, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    time.sleep(v)
    
    GPIO.output(18, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    time.sleep(v)
    
    GPIO.output(18, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(v)
    
    GPIO.output(18, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    time.sleep(v)
    
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(v)
    
    print(k)
    k=k+1
    


GPIO.cleanup()