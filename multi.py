import _thread
import time
import RPi.GPIO as GPIO



def moverMotor(threadID,steps,v):
    count = 0
    while(count < steps):
        if(threadID == "Thread-1"):
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

        elif(threadID == "Thread-2"):     
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
        count+=1
        print("Thread " + str(threadID) + " , Step # " + str(count))

s = open("archivo.txt", "r")
lines = s.read()
lines = lines.replace(';',' ')
lines = lines.split(' ')
posicion = 0

motor1Steps = int(lines[posicion])
motor2Steps = int(lines[posicion + 1])
motor3Steps = int(lines[posicion + 2])
motor4Steps = int(lines[posicion + 3])
motor5Steps = int(lines[posicion + 4])
motor6Steps = int(lines[posicion + 5])

k=0
v=.0007

try:
   _thread.start_new_thread( moverMotor, ("Thread-1",motor1Steps,0.07))
   _thread.start_new_thread( moverMotor, ("Thread-2",motor2Steps,0.07))
   #_thread.start_new_thread( moverMotor, ("Thread-3"),motor3Steps)
   #_thread.start_new_thread( moverMotor, ("Thread-4"),motor4Steps)
   #_thread.start_new_thread( moverMotor, ("Thread-5"),motor5Steps)
   #_thread.start_new_thread( moverMotor, ("Thread-6"),motor6Steps)

except:
   print("No se pudo inciar error")
while 1:
   pass