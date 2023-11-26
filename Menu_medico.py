import tkinter
from tkinter import *
from tkinter import messagebox, ttk
import psycopg2

from basededatos_pac import *
from basededatos_citas import *

global id_p, nombre_p, apellido_p, telefono_p, correo_p, edad_p, n_expediente, consultorio_p, historial_p, citas_pend
global entry_id_p, entry_nom_p, entry_ape_p, entry_tel_p, entry_correo_p, entry_edad_p, entry_n_exp, entry_con_p, entry_his_p, entry_citas_pend

global id_c, hora_c, fecha_c, id_m
global entry_id_c, entry_hora_c, entry_fecha_c,entry_id_m

def menu_med():
    global pantalla0
    pantalla0=Tk()
    pantalla0.geometry("650x380")
    pantalla0.configure(bg='white')
    pantalla0.title("Practi-Citas MD (Médico)")
    pantalla0.iconbitmap("Logo2.ico")
    
    Label(pantalla0, text="Bienvenido a tu menú principal", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 20)).pack()
    
    Label(pantalla0, text="Haz clic sobre cualquier sección del sistema a la que deseas ingresar: ", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla0, text="", bg="white").pack()
    
    Button(pantalla0, text="Pacientes", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla0.destroy()]).pack()
    Label(pantalla0, text="", bg="white").pack()
    
    Button(pantalla0, text="Citas", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla0.destroy()]).pack()
    Label(pantalla0, text="", bg="white").pack()
    
    Button(pantalla0, text="Salir", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=salir).pack()
    Label(pantalla0, text="", bg="white").pack()
    
def info_paciente():
    global pantalla2
    pantalla2=Tk()
    pantalla2.geometry("500x310")
    pantalla2.configure(bg='white')
    pantalla2.title("Practi-Citas MD (Médico)")
    pantalla2.iconbitmap("Logo2.ico")
    
    Label(pantalla2, text="Bienvenido al menú de Pacientes", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 18)).pack()
    
    Label(pantalla2, text="Haz clic sobre la opción que deseas realizar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla2, text="", bg="white").pack()
    
    Button(pantalla2, text="Buscar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[buscar_pac(),pantalla2.destroy()]).pack()
    Label(pantalla2, text="", bg="white").pack()
    
    Button(pantalla2, text="Modificar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_pac(),pantalla2.destroy()]).pack()
    Label(pantalla2, text="", bg="white").pack()
    
    Button(pantalla2, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[menu_med(),pantalla2.destroy()]).pack()
    Label(pantalla2, text="", bg="white").pack()

    def buscar_pac():
        global pantalla5
        pantalla5=Tk()
        pantalla5.geometry("700x580")
        pantalla5.configure(bg='white')
        pantalla5.title("Practi-Citas MD (Administrador)")
        pantalla5.iconbitmap("Logo2.ico")
    
        Label(pantalla5, text="Buscar un paciente", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla5, text="Introduce el ID del paciente que deseas buscar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_p = Entry(pantalla5)
        entry_id_p.pack()
        Label(pantalla5, text="", bg="white").pack()
    
        Button(pantalla5, text="Buscar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_p(entry_id_p.get())).pack()
        Label(pantalla5, text="", bg="white").pack()

        listbox = Listbox(pantalla5, width=100, height=2)
        listbox.pack()
        Label(pantalla5, text="", bg="white").pack()
    
        def buscar_p(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select * from paciente where id_pacientes = %s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()

        Button(pantalla5, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla5.destroy()]).pack()
        Label(pantalla5, text="", bg="white").pack()

    def modificar_pac():
        global pantalla6
        pantalla6=Tk()
        pantalla6.geometry("700x580")
        pantalla6.configure(bg='white')
        pantalla6.title("Practi-Citas MD (Administrador)")
        pantalla6.iconbitmap("Logo2.ico")
    
        ##Scroll
        main_frame = Frame(pantalla6)
        main_frame.pack(fill=BOTH, expand=1)
        main_frame.config(bg="white")

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        my_canvas.config(bg="white")

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        second_frame = Frame(my_canvas)
        second_frame.config(bg="white")

        my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
        Label(second_frame, text="", bg="white").pack()
        Label(second_frame, text="Modificar un paciente", bg="white", fg="dark slate grey", font=('Bahnschrift SemiLight', 16)).pack()
        Label(second_frame, text="", bg="white").pack()

        Label(second_frame, text="Introduce el ID del paciente que deseas modificar:", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_p = Entry(second_frame)
        entry_id_p.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Button(second_frame, text="Buscar paciente", bg="steel blue", fg="white", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_p(entry_id_p.get())).pack()
        Label(second_frame, text="", bg="white").pack()

        listbox = Listbox(second_frame)
        listbox.config(width=100, height=2)
        listbox.pack()
        Label(second_frame, text="", bg="white").pack()

        def buscar_p(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select * from paciente where id_pacientes = %s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()

        Label(second_frame, text="Nombre: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_nom_p = Entry(second_frame)
        entry_nom_p.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="Apellido: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_ape_p = Entry(second_frame)
        entry_ape_p.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="Teléfono: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_tel_p = Entry(second_frame)
        entry_tel_p.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="Correo: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_correo_p = Entry(second_frame)
        entry_correo_p.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="Edad: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_edad_p = Entry(second_frame)
        entry_edad_p.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="Número de expediente: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_n_exp = Entry(second_frame)
        entry_n_exp.pack()
        Label(second_frame, text="", bg="white").pack()

        Label(second_frame, text="Historial: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_his_p = Entry(second_frame)
        entry_his_p.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Button(second_frame, text="Modificar paciente", bg="steel blue", fg="white", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_p(entry_id_p.get(),entry_nom_p.get(),entry_ape_p.get(),entry_tel_p.get(),entry_correo_p.get(),entry_edad_p.get(),entry_n_exp.get(),entry_his_p.get()),modificado_p()]).pack()
        Label(second_frame, text="", bg="white").pack()

        Button(second_frame, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla6.destroy()]).pack()
        Label(second_frame, text="", bg="white").pack()
    
def info_cita():
    global pantalla3
    pantalla3=Tk()
    pantalla3.geometry("500x310")
    pantalla3.configure(bg='white')
    pantalla3.title("Practi-Citas MD (Médico)")
    pantalla3.iconbitmap("Logo2.ico")
    
    Label(pantalla3, text="Bienvenido al menú de Citas", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 18)).pack()
    
    Label(pantalla3, text="Haz clic sobre la opción que deseas realizar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Buscar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[buscar_cita(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Modificar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_cita(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[menu_med(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()

    def buscar_cita():
        global pantalla7
        pantalla7=Tk()
        pantalla7.geometry("700x580")
        pantalla7.configure(bg='white')
        pantalla7.title("Practi-Citas MD (Administrador)")
        pantalla7.iconbitmap("Logo2.ico")
    
        Label(pantalla7, text="Buscar una cita", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla7, text="Introduce el ID de la cita que deseas buscar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_c = Entry(pantalla7)
        entry_id_c.pack()
        Label(pantalla7, text="", bg="white").pack()
    
        Button(pantalla7, text="Buscar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_c(entry_id_c.get())).pack()
        Label(pantalla7, text="", bg="white").pack()

        listbox = Listbox(pantalla7, width=100, height=2)
        listbox.pack()
        Label(pantalla7, text="", bg="white").pack()
    
        def buscar_c(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select n_con, nombre_m, especialidad_m, hora_c, id_paciente, fecha_c from citas as c inner join medico as m on c.id_med= m.id_m and id_cita=%s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()

        Button(pantalla7, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla7.destroy()]).pack()
        Label(pantalla7, text="", bg="white").pack()

    def modificar_cita():
        global pantalla8
        pantalla8=Tk()
        pantalla8.geometry("700x580")
        pantalla8.configure(bg='white')
        pantalla8.title("Practi-Citas MD (Administrador)")
        pantalla8.iconbitmap("Logo2.ico")
    
        Label(pantalla8, text="Modificar una cita", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()

        Label(pantalla8, text="Introduce el ID de la cita que deseas modificar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_c = Entry(pantalla8)
        entry_id_c.pack()
        Label(pantalla8, text="", bg="white").pack()
    
        Button(pantalla8, text="Buscar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_c(entry_id_c.get())).pack()
        Label(pantalla8, text="", bg="white").pack()

        listbox = Listbox(pantalla8, width=100, height=2)
        listbox.pack()
        Label(pantalla8, text="", bg="white").pack()

        def buscar_c(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select n_con, nombre_m, especialidad_m, hora_c, id_paciente, fecha_c from citas as c inner join medico as m on c.id_med= m.id_m and id_cita=%s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()

        Label(pantalla8, text="ID del paciente: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_p = Entry(pantalla8)
        entry_id_p.pack()
        Label(pantalla8, text="", bg="white").pack()
    
        Label(pantalla8, text="ID del consultorio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_con = Entry(pantalla8)
        entry_id_con.pack()
        Label(pantalla8, text="", bg="white").pack()
    
        Label(pantalla8, text="ID del médico: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_m = Entry(pantalla8)
        entry_id_m.pack()
        Label(pantalla8, text="", bg="white").pack()
    
        Label(pantalla8, text="Hora: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_hora_c = Entry(pantalla8)
        entry_hora_c.pack()
        Label(pantalla8, text="", bg="white").pack()
    
        Label(pantalla8, text="Fecha: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_fecha_c = Entry(pantalla8)
        entry_fecha_c.pack()
        Label(pantalla8, text="", bg="white").pack()

        Button(pantalla8, text="Modificar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_c(entry_id_c.get(),entry_id_p.get(),entry_id_con.get(),entry_id_m.get(),entry_hora_c.get(),entry_fecha_c.get()),modificado_c()]).pack()
        Label(pantalla8, text="", bg="white").pack()

        Button(pantalla8, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla8.destroy()]).pack()
        Label(pantalla8, text="", bg="white").pack()

##Pantallas de modificado
def modificado_p():
    global pantalla35
    pantalla35 = Toplevel(pantalla6)
    pantalla35.geometry("360x150")
    pantalla35.configure(bg='white')
    pantalla35.title("Practi-Citas MD")
    pantalla35.iconbitmap("Logo2.ico")
    
    Label(pantalla35, text="¡Paciente modificado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla35, text="", bg="white").pack()
    
    Button(pantalla35, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla6.destroy()]).pack()
    Label(pantalla35, text="", bg="white").pack()

def modificado_c():
    global pantalla36
    pantalla36 = Toplevel(pantalla8)
    pantalla36.geometry("360x150")
    pantalla36.configure(bg='white')
    pantalla36.title("Practi-Citas MD")
    pantalla36.iconbitmap("Logo2.ico")
    
    Label(pantalla36, text="¡Cita modificada!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla36, text="", bg="white").pack()
    
    Button(pantalla36, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla8.destroy()]).pack()
    Label(pantalla36, text="", bg="white").pack()

def salir():
    global pantalla4
    pantalla4 = Toplevel(pantalla0)
    pantalla4.geometry("360x150")
    pantalla4.configure(bg='white')
    pantalla4.title("Practi-Citas MD")
    pantalla4.iconbitmap("Logo2.ico")
    
    Label(pantalla4, text="¿Estás seguro de que deseas salir?", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla4, text="", bg="white").pack()
    
    Button(pantalla4, text="Si", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=pantalla0.destroy).pack()
    Label(pantalla4, text="", bg="white").pack()
    
    Button(pantalla4, text="No", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=pantalla4.destroy).pack()
    Label(pantalla4, text="", bg="white").pack()