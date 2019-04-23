#Host
import time, socket, sys , json, os
#import RPi.GPIO as GPIO
import time
from threading import Thread
'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) #IN1
GPIO.setup(17, GPIO.OUT) #IN2
GPIO.setup(27, GPIO.OUT) #IN3
GPIO.setup(22, GPIO.OUT) #IN4
'''
#CREAR ARCHIVO JSON SI NO EXISTE O LEER EL EXISTENTE
if(os.path.exists('./data.json')):
   with open('data.json') as file:
      data = json.load(file)
else:
   newData = {}
   newData['Person'] = []
   with open('data.json','w') as outfile:
      json.dump(newData,outfile)
   with open('data.json') as file:
      data = json.load(file)

print('Programa\nConfigurando servidor...\n\n')
time.sleep(1)

#Empezar socket obteniendo IP y Port
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234

#Asignarlo al socket
soc.bind(('', port))

print(host_name, '({})'.format(ip))

#Recibir nombre
name = str(input('Ingresa tu nombre: '))
soc.listen(1) #Try to locate using socket

#Esperar nuevas conexiones
print('Esperando nueva conexion...')
connection, addr = soc.accept()

#Recibir conexion
print("Nueva conexion de ", addr[0], "(", addr[1], ")\n")
print('Conexion establecida. Conexion de: {}, ({})'.format(addr[0], addr[0]))

#Recivir y desencriptar mensaje
client_name = connection.recv(1024)
client_name = client_name.decode()


print(client_name + ' se ha conectado.')

#Enviar y encriptar mensaje
connection.send(name.encode())


#Funcion que reinicia la espera si el client se desconecta
def esperarNuevaConexion():
   soc.listen(1) #Try to locate using socket

   #Esperar nuevas conexiones
   print('Esperando nueva conexion...')
   global connection,addr
   connection, addr = soc.accept()

   #Recibir conexion
   print("Nueva conexion de ", addr[0], "(", addr[1], ")\n")
   print('Conexion establecida. Conexion de: {}, ({})'.format(addr[0], addr[0]))

   #Recivir y desencriptar mensaje
   global client_name
   client_name = connection.recv(1024)
   client_name = client_name.decode()


   print(client_name + ' se ha conectado.')

   #Enviar y encriptar mensaje
   connection.send(name.encode())

#Agregar persona con su nombre y tipo al JSON
def agregarPersona(nombre, tipo):
   global data
   data['Person'].append({
      'name': nombre,
      'tipo': tipo
   })
   with open('data.json','w') as outfile:
      json.dump(data,outfile)

#Hacer un string que enliste las personas en el json
def enlistarPersonas():
   string = ""
   for p in data['Person']:
      string += '\nNombre: ' + p['name'] + '\nTipo: ' + p['tipo'] 
   return string


#Funcion ejemplo para hacer algo de acuerdo al tipo de persona
def hacerAlgo(nombre):
   for p in data['Person']:
      #Si persona buscada esta en la lista
      if nombre == p['name']:
         #Si la persona es tipo A
         if p['tipo'] == 'A':
            #hacer algo
            pass

#Ciclo principal
while True:
#Recibir comandos
   opcion = connection.recv(1024)
   #Si se desconecto
   if not opcion:
      print(client_name + " se ha desconectado")
      esperarNuevaConexion()
      continue
   opcion = opcion.decode()

   #Se recibio opcion 1
   if opcion == "1":
      #Se recibe nombre
      nombre = connection.recv(1024)
      #Si se desconecto
      if not nombre:
         print(client_name + " se ha desconectado")
         esperarNuevaConexion()
         continue
      nombre = nombre.decode()
      #Se recibe tipo
      tipo = connection.recv(1024)
      #Se desconecto
      if not tipo:
         print(client_name + " se ha desconectado")
         esperarNuevaConexion()
         continue

      tipo = tipo.decode()

      #Llamar funcion para agregar al json
      agregarPersona(nombre,tipo)
      confirm = "\nPersona agregada al servidor"
      connection.send(confirm.encode())
      print("\nNueva persona agregada\n")
      continue

   #Enviar la lista de personas
   if opcion == "2":

      personas = enlistarPersonas()
      connection.send(personas.encode())

      continue

   if opcion == "3":
      #ruta hacia sector A
      print("llendo hacia sector A")
      '''GPIO.output(18, GPIO.HIGH)
      GPIO.output(17, GPIO.LOW)
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.LOW)
      time.sleep(10) #se movio 10 segundos
      GPIO.output(18, GPIO.HIGH)
      GPIO.output(17, GPIO.LOW)
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.LOW)
      time.sleep(5) #dio vuelta durante 5 segundos'''
      continue
   if opcion == "4":
      #ruta hacia sector B
      print("llendo hacia sector B")
      '''GPIO.output(18, GPIO.HIGH)
      GPIO.output(17, GPIO.LOW)
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.LOW)
      time.sleep(10) #se movio 10 segundos
      GPIO.output(18, GPIO.HIGH)
      GPIO.output(17, GPIO.LOW)
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.LOW)
      time.sleep(5) #dio vuelta durante 5 segundos'''
      continue
   if opcion == "5":
      #ruta hacia sector C
      print("llendo hacia sector C")
      '''GPIO.output(18, GPIO.HIGH)
      GPIO.output(17, GPIO.LOW)
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.LOW)
      time.sleep(10) #se movio 10 segundos
      GPIO.output(18, GPIO.HIGH)
      GPIO.output(17, GPIO.LOW)
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.LOW)
      time.sleep(5) #dio vuelta durante 5 segundos'''
      continue  
   #Eligio opcion de desconectarse, asi que esperar nueva conexion
   if opcion == "6":
      print("recibi 6")
      print(client_name + " se ha desconectado")
      esperarNuevaConexion()
      continue


soc.close()