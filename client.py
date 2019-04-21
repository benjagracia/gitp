#Cliente
import time,socket,sys
from tkinter import *

sock = socket.socket()

def A():
    pass
def B():
    pass
def C():
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
    botonAyuda = Button(ventana,text = "Ayuda",command=ayuda)
    botonAyuda.grid(column = 1, row = 3)
    print("{} se ha unido.".format(server_name))

    sock.close()



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



