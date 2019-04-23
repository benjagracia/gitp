#Cliente
import time,socket,sys

print("Programa Calculadora Client\n\n")
time.sleep(1)

#Iniciar socket
sock = socket.socket()

shost = socket.gethostname()
ip = socket.gethostbyname(shost)

#Asignar Host e IP al socket
print(shost, " ({})".format(ip))
server_host = input("Ingresa IP del servidor: ")

name = input("Ingresa tu nombre: ")
port = 1234
print("Intentando conectarse al servidor: {}, ({})".format(server_host,port))
time.sleep(1)

sock.connect((server_host,port))

print("Conectado\n")
#Enviar nombre de cliente encriptado
sock.send(name.encode())

#Obtener nombre del host
server_name = sock.recv(1024)
server_name = server_name.decode()

print("{} se ha unido.".format(server_name))

while True:

    print("Elige la operacion: \n1. Agregar persona\n2. Enlistar personas\n3. Departamento A\n4. Departamento B\n5. Departamento C\n6. Salir\n ")
    
    message = input(str("Operacion: "))
    if message == "1":
        sock.send(message.encode())
        
        nombre = input(str("Escribe un nombre: "))
        sock.send(nombre.encode())
        tipo = input(str("Escribe un tipo: "))
        sock.send(tipo.encode())
        
        mensajeConfirm = sock.recv(1204)
        mensajeConfirm = mensajeConfirm.decode()
        print(mensajeConfirm)
        print("\n")
        continue

    if message == "2":
        sock.send(message.encode())
        print("\n")

        personas = sock.recv(1024)
        personas = personas.decode()
        print(personas)
        continue
    if message =="3":
        sock.send(message.encode())
        print("\n")
        continue
    if message =="4":
        sock.send(message.encode())
        print("\n")
        continue
    if message =="5":
        sock.send(message.encode())
        print("\n")
        continue  
    if message == "3":
        sock.send(message.encode())
        print("\n")
        break

sock.close()