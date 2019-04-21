import _thread
import time
import RPi.GPIO as GPIO

motor1Done = False
motor2Done = False

def moverMotor(threadID,pos,v,sets):
    posicion = 0
    global motor1Done
    global motor2Done
    for i in range(0,sets):
        motor1Done = False
        motor2Done = False
        count = 0
        steps = int(lines[posicion] + pos)
        while(count < steps or motor1Done == False or motor2Done == False):
            if(threadID == "Thread-1"):
                if(count == steps):
                    motor1Done = True
                if motor1Done == True:
                    continue
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
                if(count == steps):
                    motor2Done = True
                if motor2Done == True:
                    continue
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
            print("Set # " + i + "Thread # " + str(threadID) + " ,Step # " + str(count))
        posicion = posicion + 6

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
v=.0005

try:
   _thread.start_new_thread( moverMotor, ("Thread-1",0,v,int(len(lines)/6)))
   _thread.start_new_thread( moverMotor, ("Thread-2",1,v,int(len(lines)/6)))
   #_thread.start_new_thread( moverMotor, ("Thread-3"),motor3Steps,v)
   #_thread.start_new_thread( moverMotor, ("Thread-4"),motor4Steps)
   #_thread.start_new_thread( moverMotor, ("Thread-5"),motor5Steps)
   #_thread.start_new_thread( moverMotor, ("Thread-6"),motor6Steps)

except:
   print("No se pudo inciar error")
while 1:
   pass