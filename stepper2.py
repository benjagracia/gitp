import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
v = 0.001
k = 0
while(k<512):
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    time.sleep(v)
    
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    time.sleep(v)
    
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    time.sleep(v)
    
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(5, GPIO.LOW)
    time.sleep(v)
    
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(5, GPIO.LOW)
    time.sleep(v)
    
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    time.sleep(v)
    
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(5, GPIO.LOW)
    time.sleep(v)
    
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    time.sleep(v)
    
    print(k)
    k=k+1
    


GPIO.cleanup()