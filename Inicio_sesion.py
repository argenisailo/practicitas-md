import tkinter
from tkinter import *
from tkinter import messagebox


##inicios de sesion 
from Menu_admin import *
from Menu_medico import *
from Menu_recepcion import *

##base de datos 
import psycopg2

a = 0

def entrar_base(id,contr):
    
    try:
        con=psycopg2.connect(database="CONSULTORIO", user="postgres",
        password="numero10",host="localhost")
        cursor1=con.cursor()
        print("Conexión exitosa")
        us="select id_usuario from usuarios where id_usuario=%s"
        cursor1.execute(us,[id])
        line=cursor1.fetchone()[0]

        cont="select pass_us from usuarios where id_usuario=%s"
        cursor1.execute(cont,[id])
        line2=cursor1.fetchone()[0]
        longi=len(contr)
        
        if  line == id and line2[0:longi]==contr:
            if id == 1:
                menu_admin()
                pantalla.clear()
            if id > 9 and id < 100:
                menu_recep()
            if id > 99 and id < 1000:
                menu_med()
        else:
            a=0
        con.close()
    except:
        print("no encontrado")

def menu_acceso():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("300x380")
    pantalla.configure(bg='white')
    pantalla.title("¡Bienvenido!")
    pantalla.iconbitmap("Logo2.ico")
    
    image=PhotoImage(file="Logo2.png")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()
    
    Label(text="Acceso a Practi-Citas MD", bg="white", fg="steel blue", width="300", height="2", font=('Bahnschrift SemiLight', 18)).pack()
    Label(text="", bg="white").pack()
    
    Button(text="Iniciar Sesión", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[inicio_sesion(),pantalla.destroy()]).pack()
    Label(text="", bg="white").pack()
    
    pantalla.mainloop()

def inicio_sesion():
    global pantalla1_1
    pantalla1_1 = Tk()
    pantalla1_1.geometry("400x250")
    pantalla1_1.configure(bg='white')
    pantalla1_1.title("Practi-Citas MD")
    pantalla1_1.iconbitmap("Logo2.ico")
    
    Label(pantalla1_1, text="Ingresa tu nombre de usuario y tu contraseña", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 12)).pack()
    Label(pantalla1_1, text="", bg="white").pack()
    
    global nomusuario_verify
    global conusuario_verify
    
    nomusuario_verify=StringVar()
    conusuario_verify=StringVar()
    
    global nomusuario_entry
    global conusuario_entry
    
    Label(pantalla1_1, text="Usuario", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
    nomusuario_entry = Entry(pantalla1_1, textvariable=nomusuario_verify)
    nomusuario_entry.pack()
    Label(pantalla1_1, bg="white").pack()
    
    Label(pantalla1_1, text="Contraseña", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
    conusuario_entry = Entry(pantalla1_1, textvariable=conusuario_verify)
    conusuario_entry.pack()
    Label(pantalla1_1, bg="white").pack()
    
    Button(pantalla1_1, text="Iniciar Sesión", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[entrar_base(int(nomusuario_entry.get()),conusuario_entry.get()),pantalla1_1.destroy()]).pack()
    
menu_acceso()
