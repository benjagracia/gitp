#Cliente
import time,socket,sys
from tkinter import *

sock = socket.socket()
Persona=str
def A():
    message = "3"
    sock.send(message.encode())
    
def B():
    message="4"
    sock.send(message.encode())
    pass
def C():
    message="5"
    sock.send(message.encode())
    pass
def Agregar():
    message="1"
    sock.send(entryPersona.encode())
    pass
def ayuda():
    pass
def cerrar():
    ventana.destroy()
    sock.close()
    return

def conectar():
    if entryIP.get() == "" or entryNombre.get() == "":
        return
    entryIP.config(state=DISABLED)
    entryNombre.config(state=DISABLED)
    boton.config(state=DISABLED)
    time.sleep(1)
    server_host = entryIP.get()
    name = entryNombre.get()
    port = 1234
    #Iniciar socket

    shost = socket.gethostname()
    ip = socket.gethostbyname(shost)

    time.sleep(1)
    sock.connect((server_host,port))

    print("Conectado\n")
    #Enviar nombre de cliente encriptado
    sock.send(name.encode())

    #Obtener nombre del host
    server_name = sock.recv(1024)
    server_name = server_name.decode()

    botonA = Button(ventana,text = "A",command=A)
    botonA.grid(column = 1, row = 0)
    botonB = Button(ventana,text = "B",command=B)
    botonB.grid(column = 1, row = 1)
    botonC = Button(ventana,text = "C",command=C)
    botonC.grid(column = 1, row = 2)
    botonD = Button(ventana,text= "Agregar", command=Agregar)
    botonD.grid(column=1, row=4)
    entryPersona = Entry(ventana,width = 20)
    entryPersona.grid(column = 1, row = 3)
    botonAyuda = Button(ventana,text = "Ayuda",command=ayuda)
    botonAyuda.grid(column = 1, row = 5)
    print("{} se ha unido.".format(server_name))
      



print("Programa Calculadora Client\n\n")
time.sleep(1)



#Iniciar socket
#sock = socket.socket()

shost = socket.gethostname()
ip = socket.gethostbyname(shost)

ventana = Tk()
ventana.title("Programa CLIENT")
ventana.protocol("WM_DELETE_WINDOW", cerrar)

ventana.geometry('350x200')
label = Label(ventana, text = "Ingresa tu nombre")
label.grid(column = 0, row = 0)

entryNombre = Entry(ventana,width = 20)
entryNombre.grid(column = 0, row = 1)

label = Label(ventana, text = "Ingresa la IP del host")
label.grid(column = 0, row = 2)

entryIP = Entry(ventana,width = 20)
entryIP.grid(column = 0, row = 3)


boton = Button(ventana,text = "Conectar",command=conectar)
boton.grid(column = 0, row = 4)



ventana.mainloop()
