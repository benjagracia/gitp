import threading
import time
import RPi.GPIO as GPIO

def moverMotor(threadID,pos,v):
    count = 0
    global lines
    global pines

    #Obtener numero de steps de la lista
    steps = int(lines[pos])

    #Iniciar con valor nulo
    numThread = -1

    #Mientras contador sea diferente al numero de steps
    while(count != steps):
        if(threadID == "Thread-1"):
            numThread = 0
        elif(threadID == "Thread-2"):
            numThread = 1
        elif(threadID == "Thread-3"):
            numThread = 2
        elif(threadID == "Thread-4"):
            numThread = 3
        elif(threadID == "Thread-5"):
            numThread = 4
        elif(threadID == "Thread-6"):
            numThread = 5

        #Steps positivos
        if(steps > 0)
            GPIO.output(pines[numThread][0], GPIO.HIGH)
            GPIO.output(pines[numThread][1], GPIO.LOW)
            GPIO.output(pines[numThread][2], GPIO.LOW)
            GPIO.output(pines[numThread][3], GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(pines[numThread][0], GPIO.HIGH)
            GPIO.output(pines[numThread][1], GPIO.HIGH)
            GPIO.output(pines[numThread][2], GPIO.LOW)
            GPIO.output(pines[numThread][3], GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(pines[numThread][0], GPIO.LOW)
            GPIO.output(pines[numThread][1], GPIO.HIGH)
            GPIO.output(pines[numThread][2], GPIO.LOW)
            GPIO.output(pines[numThread][3], GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(pines[numThread][0], GPIO.LOW)
            GPIO.output(pines[numThread][1], GPIO.HIGH)
            GPIO.output(pines[numThread][2], GPIO.HIGH)
            GPIO.output(pines[numThread][3], GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(pines[numThread][0], GPIO.LOW)
            GPIO.output(pines[numThread][1], GPIO.LOW)
            GPIO.output(pines[numThread][2], GPIO.HIGH)
            GPIO.output(pines[numThread][3], GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(pines[numThread][0], GPIO.LOW)
            GPIO.output(pines[numThread][1], GPIO.LOW)
            GPIO.output(pines[numThread][2], GPIO.HIGH)
            GPIO.output(pines[numThread][3], GPIO.HIGH)
            time.sleep(v)
            
            GPIO.output(pines[numThread][0], GPIO.LOW)
            GPIO.output(pines[numThread][1], GPIO.LOW)
            GPIO.output(pines[numThread][2], GPIO.HIGH)
            GPIO.output(pines[numThread][3], GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(pines[numThread][0], GPIO.HIGH)
            GPIO.output(pines[numThread][1], GPIO.LOW)
            GPIO.output(pines[numThread][2], GPIO.LOW)
            GPIO.output(pines[numThread][3], GPIO.HIGH)
            time.sleep(v)

            count+=1

        #Steps negativos
        elif(steps < 0)
            #GPIO Output en negativo
            count-=1
        print(str(threadID) + " ,Step # " + str(count))
        time.sleep(v)

#Abrir archivo en modo leer
s = open("archivo.txt", "r")
lines = s.read()

#Separar por espacios para crear una lista de numeros
lines = lines.replace(';',' ')
lines = lines.split(' ')

#Iniciar GPIO
posicion = 0

#Grupos de 4 pines para cada thread
         #Thread 1  Thread 2  Thread 3  Thread 4       Thread 5      Thread 6
pines = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[18,17,27,22],[23,24,25,5],[6,13,19,26]];

#Configurar los pines
GPIO.setmode(GPIO.BCM)
for thread in range(0,len(pines)):
    for pin in range(0,len(pines[thread])):
        GPIO.setup(pines[thread][pin],GPIO.OUT)

#Velocidad
v=.0009

#Lista de threads
threads = []

#Cantidad de numeros / 6 iteraciones
for i in range(0,int(len(lines)/6)):
    print("Set " + str(i + 1))
    #Limpiar lista de threads
    threads.clear()

    #Iniciar los 6 threads
    for j in range(0,6):
        
        #Asignar funcion a thread, e iniciarlos
        #param(funcion,NombreDeThread,velocidad)
        t = threading.Thread(target=moverMotor, args=("Thread-" + str(j + 1),j + posicion,v))
        threads.append(t)
        t.start()
    #Unir threads ya que terminen todos
    for x in threads:
        x.join()

    #Sumar posicion en lista a 6
    posicion+=6
    print("Threads terminados")