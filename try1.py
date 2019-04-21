s = open("archivo.txt", "r")
lines = s.read()
lines = lines.replace(';',' ')
lines = lines.split(' ')

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

k=0

posicion = 0
for i in range(0,int(len(lines)/6)):
    print("Set numero " + str((posicion / 6) + 1))
    motor1Count = 0
    motor2Count = 0
    motor3Count = 0
    motor4Count = 0
    motor5Count = 0
    motor6Count = 0

    motor1Steps = int(lines[posicion])
    motor2Steps = int(lines[posicion + 1])
    motor3Steps = int(lines[posicion + 2])
    motor4Steps = int(lines[posicion + 3])
    motor5Steps = int(lines[posicion + 4])
    motor6Steps = int(lines[posicion + 5])
    while (motor1Count < motor1Steps or motor2Count < motor2Steps or motor3Count < motor3Steps or motor4Count < motor4Steps or motor5Count < motor5Steps or motor6Count < motor6Steps):

        if motor1Count < motor1Steps:
            print("Se cambio el motor 1 en iteracion " + str(motor1Count + 1))
            
            GPIO.output(18, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18, GPIO.LOW)
            
            motor1Count = motor1Count + 1
        if motor2Count < motor2Steps:
            print("Se cambio el motor 2 en iteracion " + str(motor2Count + 1))
            
            GPIO.output(17, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(17, GPIO.LOW)
            
            motor2Count = motor2Count + 1
        if motor3Count < motor3Steps:
            print("Se cambio el motor 3 en iteracion " + str(motor3Count + 1))
            
            GPIO.output(27, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(27, GPIO.LOW) 
            
            motor3Count = motor3Count + 1
        if motor4Count < motor4Steps:
            print("Se cambio el motor 4 en iteracion " + str(motor4Count + 1))
            
            GPIO.output(22, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(22, GPIO.LOW) 
            
            motor4Count = motor4Count + 1
        if motor5Count < motor5Steps:
            print("Se cambio el motor 5 en iteracion " + str(motor5Count + 1))
            
            GPIO.output(23, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(23, GPIO.LOW)

            motor5Count = motor5Count + 1
        if motor6Count < motor6Steps:
            print("Se cambio el motor 6 en iteracion " + str(motor6Count + 1))
            GPIO.output(24, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(24, GPIO.HIGH)

            motor6Count = motor6Count + 1
    posicion = posicion + 6
    
GPIO.cleanup()