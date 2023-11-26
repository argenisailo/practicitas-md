import tkinter
from tkinter import *
from tkinter import messagebox, ttk
import random
import psycopg2

from basededatos_rec import *
from basededatos_m import *
from basededatos_con import *
from basededatos_pac import *
from basededatos_citas import *

global id_r, id_m, id_p, id_con, id_c
global entry_id_r, entry_pass_r, entry_nom_r, entry_ape_r, entry_turno_r, entry_jor_r, entry_tel_r, entry_dom_r

global entry_id_m, entry_pass_m, entry_nom_m, entry_ape_m, entry_ced_m, entry_esp_m, entry_con_m, entry_tel_m, entry_dom_m

global entry_id_p, entry_nom_p, entry_ape_p, entry_tel_p, entry_correo_p, entry_edad_p, entry_n_exp, entry_con_p, entry_his_p, entry_citas_pend

global entry_id_con, entry_n_con, entry_m_cargo, entry_esp_med, entry_p_cargo, entry_turno_con, entry_his_con, entry_citas_dia

global entry_id_c, entry_hora_c, entry_fecha_c

def menu_admin():
    global pantalla0
    pantalla0=Tk()
    pantalla0.geometry("650x450")
    pantalla0.configure(bg='white')
    pantalla0.title("Practi-Citas MD (Administrador)")
    pantalla0.iconbitmap("Logo2.ico")
    
    Label(text="Bienvenido a tu menú principal", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 20)).pack()
    
    Label(text="Haz clic sobre cualquier sección del sistema a la que deseas ingresar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(text="", bg="white").pack()
    
    Button(text="Recepcionistas", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_recep(),pantalla0.destroy()]).pack()
    Label(text="", bg="white").pack()
    
    Button(text="Médicos", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_med(),pantalla0.destroy()]).pack()
    Label(text="", bg="white").pack()
    
    Button(text="Consultorios", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla0.destroy()]).pack()
    Label(text="", bg="white").pack()
    
    Button(text="Pacientes", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla0.destroy()]).pack()
    Label(text="", bg="white").pack()
    
    Button(text="Citas", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla0.destroy()]).pack()
    Label(text="", bg="white").pack()
    
    Button(text="Salir", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=salir).pack()
    Label(text="", bg="white").pack()

def info_recep():
    global pantalla1
    pantalla1=Tk()
    pantalla1.geometry("500x400")
    pantalla1.configure(bg='white')
    pantalla1.title("Practi-Citas MD (Administrador)")
    pantalla1.iconbitmap("Logo2.ico")
    
    Label(pantalla1, text="Bienvenido al menú de Recepcionistas", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 18)).pack()
    
    Label(pantalla1, text="Haz clic sobre la opción que deseas realizar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla1, text="", bg="white").pack()
    
    Button(pantalla1, text="Agregar recepcionista", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_recep(),pantalla1.destroy()]).pack()
    Label(pantalla1, text="", bg="white").pack()
    
    Button(pantalla1, text="Buscar recepcionista", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[buscar_recep(),pantalla1.destroy()]).pack()
    Label(pantalla1, text="", bg="white").pack()
    
    Button(pantalla1, text="Modificar recepcionista", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_recep(),pantalla1.destroy()]).pack()
    Label(pantalla1, text="", bg="white").pack()
    
    Button(pantalla1, text="Eliminar recepcionista", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_recep(),pantalla1.destroy()]).pack()
    Label(pantalla1, text="", bg="white").pack()
    
    Button(pantalla1, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[menu_admin(),pantalla1.destroy()]).pack()
    Label(pantalla1, text="", bg="white").pack()

    ##Funciones
    def agregar_recep():
        global pantalla7
        pantalla7=Tk()
        pantalla7.geometry("400x680")
        pantalla7.configure(bg='white')
        pantalla7.title("Practi-Citas MD (Administrador)")
        pantalla7.iconbitmap("Logo2.ico")

        Label(pantalla7, text="Agregar un recepcionista", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()

        Label(pantalla7, text="Introduce los datos correspondientes:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        Label(pantalla7, text="", bg="white").pack()

        Label(pantalla7, text="ID: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        id_r = random.randint(10, 99)
        Label(pantalla7, text=id_r, bg="white", fg="black", font=('Bahnschrift SemiLight', 10)).pack()
        Label(pantalla7, text="", bg="white").pack()

        Label(pantalla7, text="Contraseña: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_pass_r = Entry(pantalla7)
        entry_pass_r.pack()
        Label(pantalla7, text="", bg="white").pack()

        Label(pantalla7, text="Nombre: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_nom_r = Entry(pantalla7)
        entry_nom_r.pack()
        Label(pantalla7, text="", bg="white").pack()

        Label(pantalla7, text="Apellido: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_ape_r = Entry(pantalla7)
        entry_ape_r.pack()
        Label(pantalla7, text="", bg="white").pack()

        Label(pantalla7, text="Turno: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_turno_r = Entry(pantalla7)
        entry_turno_r.pack()
        Label(pantalla7, text="", bg="white").pack()

        Label(pantalla7, text="Jornada: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_jor_r = Entry(pantalla7)
        entry_jor_r.pack()
        Label(pantalla7, text="", bg="white").pack()

        Label(pantalla7, text="Teléfono: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_tel_r = Entry(pantalla7)
        entry_tel_r.pack()
        Label(pantalla7, text="", bg="white").pack()

        Label(pantalla7, text="Domicilio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_dom_r = Entry(pantalla7)
        entry_dom_r.pack()
        Label(pantalla7, text="", bg="white").pack()

        Button(pantalla7,  text="Agregar recepcionista", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_r(int(id_r),entry_pass_r.get(),entry_nom_r.get(),entry_ape_r.get(),entry_turno_r.get(),entry_jor_r.get(),entry_tel_r.get(),entry_dom_r.get()), agregado_r()]).pack()
        Label(pantalla7, text="", bg="white").pack()

        Button(pantalla7, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_recep(),pantalla7.destroy()]).pack()
        Label(pantalla7, text="", bg="white").pack()
    
    def buscar_recep():
        global pantalla8
        pantalla8=Tk()
        pantalla8.geometry("700x580")
        pantalla8.configure(bg='white')
        pantalla8.title("Practi-Citas MD (Administrador)")
        pantalla8.iconbitmap("Logo2.ico")
    
        Label(pantalla8, text="Buscar un recepcionista", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla8, text="Introduce el ID del recepcionista que deseas buscar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_r = Entry(pantalla8)
        entry_id_r.pack()
        Label(pantalla8, text="", bg="white").pack()
    
        Button(pantalla8, text="Buscar recepcionista", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_r(entry_id_r.get())).pack()
        Label(pantalla8, text="", bg="white").pack()

        listbox = Listbox(pantalla8, width=100, height=2)
        listbox.pack()
        Label(pantalla8, text="", bg="white").pack()

        def buscar_r(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select * from recepcion where id_recepcion = %s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()
    
        Button(pantalla8, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_recep(),pantalla8.destroy()]).pack()
        Label(pantalla8, text="", bg="white").pack()
    
    def modificar_recep():
        global pantalla9
        pantalla9=Tk()
        pantalla9.geometry("700x768")
        pantalla9.configure(bg='white')
        pantalla9.title("Practi-Citas MD (Administrador)")
        pantalla9.iconbitmap("Logo2.ico")
    
        Label(pantalla9, text="Modificar un recepcionista", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla9, text="Introduce el ID del recepcionista que deseas modificar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_r = Entry(pantalla9)
        entry_id_r.pack()
        Label(pantalla9, text="", bg="white").pack()
    
        Button(pantalla9, text="Buscar recepcionista", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_r(entry_id_r.get())).pack()
        Label(pantalla9, text="", bg="white").pack()

        listbox = Listbox(pantalla9, width=100, height=2)
        listbox.pack()
        Label(pantalla9, text="", bg="white").pack()

        def buscar_r(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select * from recepcion where id_recepcion = %s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()
    
        Label(pantalla9, text="Contraseña: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_pass_r = Entry(pantalla9)
        entry_pass_r.pack()
        Label(pantalla9, text="", bg="white").pack()
    
        Label(pantalla9, text="Nombre: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_nom_r = Entry(pantalla9)
        entry_nom_r.pack()
        Label(pantalla9, text="", bg="white").pack()
    
        Label(pantalla9, text="Apellido: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_ape_r = Entry(pantalla9)
        entry_ape_r.pack()
        Label(pantalla9, text="", bg="white").pack()
    
        Label(pantalla9, text="Turno: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_turno_r = Entry(pantalla9)
        entry_turno_r.pack()
        Label(pantalla9, text="", bg="white").pack()
    
        Label(pantalla9, text="Jornada: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_jor_r = Entry(pantalla9)
        entry_jor_r.pack()
        Label(pantalla9, text="", bg="white").pack()
    
        Label(pantalla9, text="Teléfono: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_tel_r = Entry(pantalla9)
        entry_tel_r.pack()
        Label(pantalla9, text="", bg="white").pack()
    
        Label(pantalla9, text="Domicilio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_dom_r = Entry(pantalla9)
        entry_dom_r.pack()
        Label(pantalla9, text="", bg="white").pack()
    
        Label(pantalla9, text="", bg="white").pack(side=LEFT)
        Button(pantalla9, text="Modificar recepcionista", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_r(entry_id_r.get(),entry_pass_r.get(),entry_nom_r.get(),entry_ape_r.get(),entry_turno_r.get(),entry_jor_r.get(),entry_tel_r.get(),entry_dom_r.get()),modificado_r()]).pack(side=LEFT)

        Label(pantalla9, text="", bg="white").pack(side=RIGHT)
        Button(pantalla9, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_recep(),pantalla9.destroy()]).pack(side=RIGHT)
        Label(pantalla9, text="", bg="white").pack()

    def eliminar_recep():
        global pantalla10
        pantalla10=Tk()
        pantalla10.geometry("700x580")
        pantalla10.configure(bg='white')
        pantalla10.title("Practi-Citas MD (Administrador)")
        pantalla10.iconbitmap("Logo2.ico")
    
        Label(pantalla10, text="Eliminar un recepcionista", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla10, text="Introduce el ID del recepcionista que deseas eliminar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_r = Entry(pantalla10)
        entry_id_r.pack()
        Label(pantalla10, text="", bg="white").pack()
    
        Button(pantalla10, text="Buscar recepcionista", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_r(entry_id_r.get())).pack()
        Label(pantalla10, text="", bg="white").pack()

        listbox = Listbox(pantalla10, width=100, height=2)
        listbox.pack()
        Label(pantalla10, text="", bg="white").pack()
    
        def buscar_r(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select * from recepcion where id_recepcion = %s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()
    
        Button(pantalla10, text="Eliminar recepcionista", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_r(entry_id_r.get()),eliminado_r()]).pack()
        Label(pantalla10, text="", bg="white").pack()

        Button(pantalla10, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_recep(),pantalla10.destroy()]).pack()
        Label(pantalla10, text="", bg="white").pack()
    
def info_med():
    global pantalla2
    pantalla2=Tk()
    pantalla2.geometry("500x400")
    pantalla2.configure(bg='white')
    pantalla2.title("Practi-Citas MD (Administrador)")
    pantalla2.iconbitmap("Logo2.ico")
    
    Label(pantalla2, text="Bienvenido al menú de Médicos", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 18)).pack()
    
    Label(pantalla2, text="Haz clic sobre la opción que deseas realizar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla2, text="", bg="white").pack()
    
    Button(pantalla2, text="Agregar médico", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_med(),pantalla2.destroy()]).pack()
    Label(pantalla2, text="", bg="white").pack()
    
    Button(pantalla2, text="Buscar médico", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[buscar_med(),pantalla2.destroy()]).pack()
    Label(pantalla2, text="", bg="white").pack()
    
    Button(pantalla2, text="Modificar médico", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_med(),pantalla2.destroy()]).pack()
    Label(pantalla2, text="", bg="white").pack()
    
    Button(pantalla2, text="Eliminar médico", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_med(),pantalla2.destroy()]).pack()
    Label(pantalla2, text="", bg="white").pack()
    
    Button(pantalla2, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[menu_admin(),pantalla2.destroy()]).pack()
    Label(pantalla2, text="", bg="white").pack()

    def agregar_med():
        global pantalla11
        pantalla11=Tk()
        pantalla11.geometry("700x580")
        pantalla11.configure(bg='white')
        pantalla11.title("Practi-Citas MD (Administrador)")
        pantalla11.iconbitmap("Logo2.ico")
    
        Label(pantalla11, text="Agregar un médico", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla11, text="Introduce los datos correspondientes:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        Label(pantalla11, text="", bg="white").pack()
    
        Label(pantalla11, text="ID: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        id_m = random.randint(100, 999)
        Label(pantalla11, text=id_m, bg="white", fg="black", font=('Bahnschrift SemiLight', 10)).pack()
        Label(pantalla11, text="", bg="white").pack()
    
        Label(pantalla11, text="Contraseña: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_pass_m = Entry(pantalla11)
        entry_pass_m.pack()
        Label(pantalla11, text="", bg="white").pack()
    
        Label(pantalla11, text="Nombre: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_nom_m = Entry(pantalla11)
        entry_nom_m.pack()
        Label(pantalla11, text="", bg="white").pack()
    
        Label(pantalla11, text="Apellido: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_ape_m = Entry(pantalla11)
        entry_ape_m.pack()
        Label(pantalla11, text="", bg="white").pack()
    
        Label(pantalla11, text="Cédula: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_ced_m = Entry(pantalla11)
        entry_ced_m.pack()
        Label(pantalla11, text="", bg="white").pack()
    
        Label(pantalla11, text="Especialidad: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_esp_m = Entry(pantalla11)
        entry_esp_m.pack()
        Label(pantalla11, text="", bg="white").pack()
    
        Label(pantalla11, text="Teléfono: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_tel_m = Entry(pantalla11)
        entry_tel_m.pack()
        Label(pantalla11, text="", bg="white").pack()
    
        Label(pantalla11, text="Domicilio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_dom_m = Entry(pantalla11)
        entry_dom_m.pack()
        Label(pantalla11, text="", bg="white").pack()
    
        Label(pantalla11, text="Consultorio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_con_m = Entry(pantalla11)
        entry_con_m.pack()
        Label(pantalla11, text="", bg="white").pack()
    
        Label(pantalla11, text="", bg="white").pack(side=LEFT)
        Button(pantalla11, text="Agregar médico", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_m(int(id_m),entry_pass_m.get(),entry_nom_m.get(),entry_ape_m.get(),entry_ced_m.get(),entry_esp_m.get(),entry_tel_m.get(),entry_dom_m.get(),entry_con_m.get()),agregado_m()]).pack(side=LEFT)

        Label(pantalla11, text="", bg="white").pack(side=RIGHT)
        Button(pantalla11, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_med(),pantalla11.destroy()]).pack(side=RIGHT)
        Label(pantalla11, text="", bg="white").pack()
     
    def buscar_med():
        global pantalla12
        pantalla12=Tk()
        pantalla12.geometry("700x580")
        pantalla12.configure(bg='white')
        pantalla12.title("Practi-Citas MD (Administrador)")
        pantalla12.iconbitmap("Logo2.ico")
    
        Label(pantalla12, text="Buscar un médico", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla12, text="Introduce el ID del médico que deseas buscar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_m = Entry(pantalla12)
        entry_id_m.pack()
        Label(pantalla12, text="", bg="white").pack()
    
        Button(pantalla12, text="Buscar médico", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_m(entry_id_m.get())).pack()
        Label(pantalla12, text="", bg="white").pack()

        listbox = Listbox(pantalla12, width=100, height=2)
        listbox.pack()
        Label(pantalla12, text="", bg="white").pack()
    
        def buscar_m(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select * from medico where id_m = %s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()

        Button(pantalla12, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_med(),pantalla12.destroy()]).pack()
        Label(pantalla12, text="", bg="white").pack()

    def modificar_med():
        global pantalla13
        pantalla13=Tk()
        pantalla13.geometry("700x580")
        pantalla13.configure(bg='white')
        pantalla13.title("Practi-Citas MD (Administrador)")
        pantalla13.iconbitmap("Logo2.ico")

        ##Scroll
        main_frame = Frame(pantalla13)
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
        Label(second_frame, text="Modificar un médico", bg="white", fg="dark slate grey", font=('Bahnschrift SemiLight', 16)).pack()
        Label(second_frame, text="", bg="white").pack()

        Label(second_frame, text="Introduce el ID del médico que deseas modificar:", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_m = Entry(second_frame)
        entry_id_m.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Button(second_frame, text="Buscar médico", bg="steel blue", fg="white", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_m(entry_id_m.get())).pack()
        Label(second_frame, text="", bg="white").pack()

        listbox = Listbox(second_frame)
        listbox.config(width=100, height=2)
        listbox.pack()
        Label(second_frame, text="", bg="white").pack()

        def buscar_m(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select * from medico where id_m = %s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()
    
        Label(second_frame, text="Contraseña: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_pass_m = Entry(second_frame)
        entry_pass_m.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="Nombre: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_nom_m = Entry(second_frame)
        entry_nom_m.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="Apellido: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_ape_m = Entry(second_frame)
        entry_ape_m.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="Cédula: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_ced_m = Entry(second_frame)
        entry_ced_m.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="Especialidad: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_esp_m = Entry(second_frame)
        entry_esp_m.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="Teléfono: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_tel_m = Entry(second_frame)
        entry_tel_m.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="Domicilio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_dom_m = Entry(second_frame)
        entry_dom_m.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="Consultorio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_con_m = Entry(second_frame)
        entry_con_m.pack()
        Label(second_frame, text="", bg="white").pack()
    
        Button(second_frame, text="Modificar médico", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_m(entry_pass_m.get(),entry_nom_m.get(),entry_ape_m.get(),entry_ced_m.get(),entry_esp_m.get(),entry_tel_m.get(),entry_dom_m.get(),entry_con_m.get()),modificado_m()]).pack()
        Label(second_frame, text="", bg="white").pack()

        Button(second_frame, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_med(),pantalla13.destroy()]).pack()
        Label(second_frame, text="", bg="white").pack()

    def eliminar_med(): 
        global pantalla14
        pantalla14=Tk()
        pantalla14.geometry("700x580")
        pantalla14.configure(bg='white')
        pantalla14.title("Practi-Citas MD (Administrador)")
        pantalla14.iconbitmap("Logo2.ico")
    
        Label(pantalla14, text="Eliminar un médico", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()

        Label(pantalla14, text="Introduce el ID del médico que deseas eliminar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_m = Entry(pantalla14)
        entry_id_m.pack()
        Label(pantalla14, text="", bg="white").pack()

        Button(pantalla14, text="Buscar médico", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_m(entry_id_m.get())).pack()
        Label(pantalla14, text="", bg="white").pack()

        listbox = Listbox(pantalla14, width=100, height=2)
        listbox.pack()
        Label(pantalla14, text="", bg="white").pack()

        def buscar_m(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select * from medico where id_m = %s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()
    
        Button(pantalla14, text="Eliminar médico", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_m(entry_id_m.get()),eliminado_m()]).pack()
        Label(pantalla14, text="", bg="white").pack()

        Button(pantalla14, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_med(),pantalla14.destroy()]).pack()
        Label(pantalla14, text="", bg="white").pack()
    
def info_consul():
    global pantalla3
    pantalla3=Tk()
    pantalla3.geometry("500x400")
    pantalla3.configure(bg='white')
    pantalla3.title("Practi-Citas MD (Administrador)")
    pantalla3.iconbitmap("Logo2.ico")
    
    Label(pantalla3, text="Bienvenido al menú de Consultorios", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 18)).pack()
    
    Label(pantalla3, text="Haz clic sobre la opción que deseas realizar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Agregar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_consul(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Buscar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[buscar_consul(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Modificar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_consul(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Eliminar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_consul(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[menu_admin(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()

    def agregar_consul():
        global pantalla15
        pantalla15=Tk()
        pantalla15.geometry("700x580")
        pantalla15.configure(bg='white')
        pantalla15.title("Practi-Citas MD (Administrador)")
        pantalla15.iconbitmap("Logo2.ico")
    
        Label(pantalla15, text="Agregar un consultorio", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla15, text="Introduce los datos correspondientes:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        Label(pantalla15, text="", bg="white").pack()
    
        Label(pantalla15, text="ID: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        id_con = random.randint(1000, 9999)
        Label(pantalla15, text=id_con, bg="white", fg="black", font=('Bahnschrift SemiLight', 10)).pack()
        Label(pantalla15, text="", bg="white").pack()
    
        Label(pantalla15, text="Número de consultorio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_n_con = Entry(pantalla15)
        entry_n_con.pack()
        Label(pantalla15, text="", bg="white").pack()
    
        Button(pantalla15, text="Agregar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_co(int(id_con),entry_n_con.get()),agregado_con()]).pack()
        Label(pantalla15, text="", bg="white").pack()

        Button(pantalla15, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla15.destroy()]).pack()
        Label(pantalla15, text="", bg="white").pack()
    
    def buscar_consul():
        global pantalla16
        pantalla16=Tk()
        pantalla16.geometry("700x580")
        pantalla16.configure(bg='white')
        pantalla16.title("Practi-Citas MD (Administrador)")
        pantalla16.iconbitmap("Logo2.ico")
    
        Label(pantalla16, text="Buscar un consultorio", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla16, text="Introduce el ID del consultorio que deseas buscar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_con = Entry(pantalla16)
        entry_id_con.pack()
        Label(pantalla16, text="", bg="white").pack()
    
        Button(pantalla16, text="Buscar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_co(entry_id_con.get())).pack()
        Label(pantalla16, text="", bg="white").pack()

        listbox = Listbox(pantalla16, width=100, height=2)
        listbox.pack()
        Label(pantalla16, text="", bg="white").pack()

        def buscar_co(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select id_consultorio, n_consultorio,id_m, nombre_m, apellido_m, especialidad_m from consultorio as c inner join medico as m on c.n_consultorio= m.n_con and id_consultorio=%s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()
        
        Button(pantalla16, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla16.destroy()]).pack()
        Label(pantalla16, text="", bg="white").pack()

    def modificar_consul():
        global pantalla17
        pantalla17=Tk()
        pantalla17.geometry("700x580")
        pantalla17.configure(bg='white')
        pantalla17.title("Practi-Citas MD (Administrador)")
        pantalla17.iconbitmap("Logo2.ico")
    
        Label(pantalla17, text="Modificar un consultorio", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla17, text="Introduce el ID del consultorio que deseas modificar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_con = Entry(pantalla17)
        entry_id_con.pack()
        Label(pantalla17, text="", bg="white").pack()
    
        Button(pantalla17, text="Buscar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_co(entry_id_con.get())).pack()
        Label(pantalla17, text="", bg="white").pack()

        listbox = Listbox(pantalla17, width=100, height=2)
        listbox.pack()
        Label(pantalla17, text="", bg="white").pack()

        def buscar_co(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select id_consultorio, n_consultorio,id_m, nombre_m, apellido_m, especialidad_m from consultorio as c inner join medico as m on c.n_consultorio= m.n_con and id_consultorio=%s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()
    
        Label(pantalla17, text="Número de consultorio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_n_con = Entry(pantalla17)
        entry_n_con.pack()
        Label(pantalla17, text="", bg="white").pack()
    
        Button(pantalla17, text="Modificar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_co(entry_id_con.get(),entry_n_con.get()),modificado_con]).pack()
        Label(pantalla17, text="", bg="white").pack()

        Button(pantalla17, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla17.destroy()]).pack()
        Label(pantalla17, text="", bg="white").pack()

    def eliminar_consul():
        global pantalla18
        pantalla18=Tk()
        pantalla18.geometry("700x580")
        pantalla18.configure(bg='white')
        pantalla18.title("Practi-Citas MD (Administrador)")
        pantalla18.iconbitmap("Logo2.ico")
    
        Label(pantalla18, text="Eliminar un consultorio", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla18, text="Introduce el ID del consultorio que deseas eliminar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_con = Entry(pantalla18)
        entry_id_con.pack()
        Label(pantalla18, text="", bg="white").pack()
    
        Button(pantalla18, text="Buscar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_co(entry_id_con.get())).pack()
        Label(pantalla18, text="", bg="white").pack()

        listbox = Listbox(pantalla18, width=100, height=2)
        listbox.pack()
        Label(pantalla18, text="", bg="white").pack()
    
        def buscar_co(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select id_consultorio, n_consultorio,id_m, nombre_m, apellido_m, especialidad_m from consultorio as c inner join medico as m on c.n_consultorio= m.n_con and id_consultorio=%s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()

        Button(pantalla18, text="Eliminar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_co(entry_id_con.get()),eliminado_con()]).pack()
        Label(pantalla18, text="", bg="white").pack()

        Button(pantalla18, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla18.destroy()]).pack()
        Label(pantalla18, text="", bg="white").pack()
    
def info_paciente():
    global pantalla4
    pantalla4=Tk()
    pantalla4.geometry("500x400")
    pantalla4.configure(bg='white')
    pantalla4.title("Practi-Citas MD (Administrador)")
    pantalla4.iconbitmap("Logo2.ico")
    
    Label(pantalla4, text="Bienvenido al menú de Pacientes", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 18)).pack()

    Label(pantalla4, text="Haz clic sobre la opción que deseas realizar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla4, text="", bg="white").pack()
    
    Button(pantalla4, text="Agregar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_pac(),pantalla4.destroy()]).pack()
    Label(pantalla4, text="", bg="white").pack()
    
    Button(pantalla4, text="Buscar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[buscar_pac(),pantalla4.destroy()]).pack()
    Label(pantalla4, text="", bg="white").pack()
    
    Button(pantalla4, text="Modificar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_pac(),pantalla4.destroy()]).pack()
    Label(pantalla4, text="", bg="white").pack()
    
    Button(pantalla4, text="Eliminar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_pac(),pantalla4.destroy()]).pack()
    Label(pantalla4, text="", bg="white").pack()
    
    Button(pantalla4, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[menu_admin(),pantalla4.destroy()]).pack()
    Label(pantalla4, text="", bg="white").pack()

    def agregar_pac():
        global pantalla19
        pantalla19=Tk()
        pantalla19.geometry("700x580")
        pantalla19.configure(bg='white')
        pantalla19.title("Practi-Citas MD (Administrador)")
        pantalla19.iconbitmap("Logo2.ico")

        ##Scroll
        main_frame = Frame(pantalla19)
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
        Label(second_frame, text="Agregar un paciente", bg="white", fg="dark slate grey", font=('Bahnschrift SemiLight', 16)).pack()
        Label(second_frame, text="", bg="white").pack()

        Label(second_frame, text="Introduce los datos correspondientes:", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 14)).pack()
        Label(second_frame, text="", bg="white").pack()
    
        Label(second_frame, text="ID: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        id_p = random.randint(10000, 99999)
        Label(second_frame, text=id_p, bg="white", fg="black", font=('Bahnschrift SemiLight', 10)).pack()
        Label(second_frame, text="", bg="white").pack()
    
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
    
        Button(second_frame, text="Agregar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_p(int(id_p),entry_nom_p.get(),entry_ape_p.get(),entry_tel_p.get(),entry_correo_p.get(),entry_edad_p.get(),entry_n_exp.get(),entry_his_p.get()),agregado_p()]).pack()
        Label(second_frame, text="", bg="white").pack()

        Button(second_frame, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla19.destroy()]).pack()
        Label(second_frame, text="", bg="white").pack()

    def buscar_pac():
        global pantalla20
        pantalla20=Tk()
        pantalla20.geometry("700x580")
        pantalla20.configure(bg='white')
        pantalla20.title("Practi-Citas MD (Administrador)")
        pantalla20.iconbitmap("Logo2.ico")
    
        Label(pantalla20, text="Buscar un paciente", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla20, text="Introduce el ID del paciente que deseas buscar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_p = Entry(pantalla20)
        entry_id_p.pack()
        Label(pantalla20, text="", bg="white").pack()
    
        Button(pantalla20, text="Buscar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_p(entry_id_p.get())).pack()
        Label(pantalla20, text="", bg="white").pack()

        listbox = Listbox(pantalla20, width=100, height=2)
        listbox.pack()
        Label(pantalla20, text="", bg="white").pack()

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

        Button(pantalla20, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla20.destroy()]).pack()
        Label(pantalla20, text="", bg="white").pack()

    def modificar_pac():
        global pantalla21
        pantalla21=Tk()
        pantalla21.geometry("700x580")
        pantalla21.configure(bg='white')
        pantalla21.title("Practi-Citas MD (Administrador)")
        pantalla21.iconbitmap("Logo2.ico")

        ##Scroll
        main_frame = Frame(pantalla21)
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
    
        Button(second_frame, text="Buscar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_p(entry_id_p.get())).pack()
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
    
        Button(second_frame, text="Modificar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_p(entry_id_p.get(),entry_nom_p.get(),entry_ape_p.get(),entry_tel_p.get(),entry_correo_p.get(),entry_edad_p.get(),entry_n_exp.get(),entry_his_p.get()),modificado_p()]).pack()
        Label(second_frame, text="", bg="white").pack()

        Button(second_frame, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla21.destroy()]).pack()
        Label(second_frame, text="", bg="white").pack()

    def eliminar_pac():
        global pantalla22
        pantalla22=Tk()
        pantalla22.geometry("700x580")
        pantalla22.configure(bg='white')
        pantalla22.title("Practi-Citas MD (Administrador)")
        pantalla22.iconbitmap("Logo2.ico")
    
        Label(pantalla22, text="Eliminar un paciente", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla22, text="Introduce el ID del paciente que deseas eliminar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_p = Entry(pantalla22)
        entry_id_p.pack()
        Label(pantalla22, text="", bg="white").pack()
    
        Button(pantalla22, text="Buscar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_p(entry_id_p.get())).pack()
        Label(pantalla22, text="", bg="white").pack()

        listbox = Listbox(pantalla22, width=100, height=2)
        listbox.pack()
        Label(pantalla22, text="", bg="white").pack()

        def buscar_p(id):
            con=psycopg2.connect(database="CONSULTORIO", user="postgres",
            password="numero10",host="localhost")
            cursor1=con.cursor()

            op="select * from pacientes where id_pacientes = %s"
            cursor1.execute(op,[id])
            line=cursor1.fetchall()

            for row in line:
                listbox.insert(END, row)
    
            cursor1.close()

        Button(pantalla22, text="Eliminar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_p(entry_id_p.get()),eliminado_p()]).pack()
        Label(pantalla22, text="", bg="white").pack()

        Button(pantalla22, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla22.destroy()]).pack()
        Label(pantalla22, text="", bg="white").pack()
    
def info_cita():
    global pantalla5
    pantalla5=Tk()
    pantalla5.geometry("500x400")
    pantalla5.configure(bg='white')
    pantalla5.title("Practi-Citas MD (Administrador)")
    pantalla5.iconbitmap("Logo2.ico")
    
    Label(pantalla5, text="Bienvenido al menú de Citas", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 18)).pack()
    
    Label(pantalla5, text="Haz clic sobre la opción que deseas realizar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla5, text="", bg="white").pack()
    
    Button(pantalla5, text="Agregar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_cita(),pantalla5.destroy()]).pack()
    Label(pantalla5, text="", bg="white").pack()
    
    Button(pantalla5, text="Buscar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[buscar_cita(),pantalla5.destroy()]).pack()
    Label(pantalla5, text="", bg="white").pack()
    
    Button(pantalla5, text="Modificar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_cita(),pantalla5.destroy()]).pack()
    Label(pantalla5, text="", bg="white").pack()
    
    Button(pantalla5, text="Eliminar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_cita(),pantalla5.destroy()]).pack()
    Label(pantalla5, text="", bg="white").pack()
    
    Button(pantalla5, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[menu_admin(),pantalla5.destroy()]).pack()
    Label(pantalla5, text="", bg="white").pack()

    def agregar_cita():
        global pantalla23
        pantalla23=Tk()
        pantalla23.geometry("700x580")
        pantalla23.configure(bg='white')
        pantalla23.title("Practi-Citas MD (Administrador)")
        pantalla23.iconbitmap("Logo2.ico")
    
        Label(pantalla23, text="Agregar una cita", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla23, text="Introduce los datos correspondientes:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        Label(pantalla23, text="", bg="white").pack()
    
        Label(pantalla23, text="ID de la cita: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        id_c = random.randint(100000, 999999)
        Label(pantalla23, text=id_c, bg="white", fg="black", font=('Bahnschrift SemiLight', 10)).pack()
        Label(pantalla23, text="", bg="white").pack()
    
        Label(pantalla23, text="ID del paciente: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_p = Entry(pantalla23)
        entry_id_p.pack()
        Label(pantalla23, text="", bg="white").pack()
    
        Label(pantalla23, text="ID del consultorio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_con = Entry(pantalla23)
        entry_id_con.pack()
        Label(pantalla23, text="", bg="white").pack()
    
        Label(pantalla23, text="ID del médico: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_m = Entry(pantalla23)
        entry_id_m.pack()
        Label(pantalla23, text="", bg="white").pack()
    
        Label(pantalla23, text="Hora: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_hora_c = Entry(pantalla23)
        entry_hora_c.pack()
        Label(pantalla23, text="", bg="white").pack()
    
        Label(pantalla23, text="Fecha: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_fecha_c = Entry(pantalla23)
        entry_fecha_c.pack()
        Label(pantalla23, text="", bg="white").pack()

        Button(pantalla23, text="Agregar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_c(int(id_c),entry_id_p.get(),entry_id_con.get(),entry_id_m.get(),entry_hora_c.get(),entry_fecha_c.get()),agregado_c()]).pack()
        Label(pantalla23, text="", bg="white").pack()

        Button(pantalla23, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla23.destroy()]).pack()
        Label(pantalla23, text="", bg="white").pack()

    def buscar_cita():
        global pantalla24
        pantalla24=Tk()
        pantalla24.geometry("700x580")
        pantalla24.configure(bg='white')
        pantalla24.title("Practi-Citas MD (Administrador)")
        pantalla24.iconbitmap("Logo2.ico")
    
        Label(pantalla24, text="Buscar una cita", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla24, text="Introduce el ID de la cita que deseas buscar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_c = Entry(pantalla24)
        entry_id_c.pack()
        Label(pantalla24, text="", bg="white").pack()
    
        Button(pantalla24, text="Buscar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_c(entry_id_c.get())).pack()
        Label(pantalla24, text="", bg="white").pack()

        listbox = Listbox(pantalla24, width=100, height=2)
        listbox.pack()
        Label(pantalla24, text="", bg="white").pack()

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

        Button(pantalla24, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla24.destroy()]).pack()
        Label(pantalla24, text="", bg="white").pack()

    def modificar_cita():
        global pantalla25
        pantalla25=Tk()
        pantalla25.geometry("700x580")
        pantalla25.configure(bg='white')
        pantalla25.title("Practi-Citas MD (Administrador)")
        pantalla25.iconbitmap("Logo2.ico")
    
        Label(pantalla25, text="Modificar una cita", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla25, text="Introduce el ID de la cita que deseas modificar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_c = Entry(pantalla25)
        entry_id_c.pack()
        Label(pantalla25, text="", bg="white").pack()
    
        Button(pantalla25, text="Buscar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_c(entry_id_c.get())).pack()
        Label(pantalla25, text="", bg="white").pack()

        listbox = Listbox(pantalla25, width=100, height=2)
        listbox.pack()
        Label(pantalla25, text="", bg="white").pack()

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

        Label(pantalla25, text="ID del paciente: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_p = Entry(pantalla25)
        entry_id_p.pack()
        Label(pantalla25, text="", bg="white").pack()
    
        Label(pantalla25, text="ID del consultorio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_con = Entry(pantalla25)
        entry_id_con.pack()
        Label(pantalla25, text="", bg="white").pack()
    
        Label(pantalla25, text="ID del médico: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_m = Entry(pantalla25)
        entry_id_m.pack()
        Label(pantalla25, text="", bg="white").pack()
    
        Label(pantalla25, text="Hora: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_hora_c = Entry(pantalla25)
        entry_hora_c.pack()
        Label(pantalla25, text="", bg="white").pack()
    
        Label(pantalla25, text="Fecha: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_fecha_c = Entry(pantalla25)
        entry_fecha_c.pack()
        Label(pantalla25, text="", bg="white").pack()

        Button(pantalla25, text="Modificar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_c(entry_id_c.get(),entry_id_p.get(),entry_id_con.get(),entry_id_m.get(),entry_hora_c.get(),entry_fecha_c.get()),modificado_c()]).pack()
        Label(pantalla25, text="", bg="white").pack()

        Button(pantalla25, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla25.destroy()]).pack()
        Label(pantalla25, text="", bg="white").pack()

    def eliminar_cita():
        global pantalla26
        pantalla26=Tk()
        pantalla26.geometry("700x580")
        pantalla26.configure(bg='white')
        pantalla26.title("Practi-Citas MD (Administrador)")
        pantalla26.iconbitmap("Logo2.ico")
    
        Label(pantalla26, text="Eliminar una cita", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()

        Label(pantalla26, text="Introduce el ID de la cita que deseas eliminar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_c = Entry(pantalla26)
        entry_id_c.pack()
        Label(pantalla26, text="", bg="white").pack()
    
        Button(pantalla26, text="Buscar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_c(entry_id_c.get())).pack()
        Label(pantalla26, text="", bg="white").pack()

        listbox = Listbox(pantalla26, width=100, height=2)
        listbox.pack()
        Label(pantalla26, text="", bg="white").pack()

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

        Button(pantalla26, text="Eliminar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_c(entry_id_c.get()),eliminado_c()]).pack()
        Label(pantalla26, text="", bg="white").pack()

        Button(pantalla26, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla26.destroy()]).pack()
        Label(pantalla26, text="", bg="white").pack()

##Pantallas de agregado
def agregado_r():
    global pantalla27
    pantalla27 = Toplevel(pantalla7)
    pantalla27.geometry("360x150")
    pantalla27.configure(bg='white')
    pantalla27.title("Practi-Citas MD")
    pantalla27.iconbitmap("Logo2.ico")
    
    Label(pantalla27, text="¡Recepcionista agregado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla27, text="", bg="white").pack()
    
    Button(pantalla27, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_recep(),pantalla7.destroy()]).pack()
    Label(pantalla27, text="", bg="white").pack()

def agregado_m():
    global pantalla28
    pantalla28 = Toplevel(pantalla11)
    pantalla28.geometry("360x150")
    pantalla28.configure(bg='white')
    pantalla8.title("Practi-Citas MD")
    pantalla28.iconbitmap("Logo2.ico")
    
    Label(pantalla28, text="¡Médico agregado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla28, text="", bg="white").pack()
    
    Button(pantalla28, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_med(),pantalla11.destroy()]).pack()
    Label(pantalla28, text="", bg="white").pack()

def agregado_con():
    global pantalla29
    pantalla29 = Toplevel(pantalla15)
    pantalla29.geometry("360x150")
    pantalla29.configure(bg='white')
    pantalla29.title("Practi-Citas MD")
    pantalla29.iconbitmap("Logo2.ico")
    
    Label(pantalla29, text="¡Consultorio agregado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla29, text="", bg="white").pack()
    
    Button(pantalla29, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla15.destroy()]).pack()
    Label(pantalla29, text="", bg="white").pack()

def agregado_p():
    global pantalla30
    pantalla30 = Toplevel(pantalla19)
    pantalla30.geometry("360x150")
    pantalla30.configure(bg='white')
    pantalla30.title("Practi-Citas MD")
    pantalla30.iconbitmap("Logo2.ico")
    
    Label(pantalla30, text="¡Paciente agregado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla30, text="", bg="white").pack()
    
    Button(pantalla30, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla19.destroy()]).pack()
    Label(pantalla30, text="", bg="white").pack()

def agregado_c():
    global pantalla31
    pantalla31 = Toplevel(pantalla23)
    pantalla31.geometry("360x150")
    pantalla31.configure(bg='white')
    pantalla31.title("Practi-Citas MD")
    pantalla31.iconbitmap("Logo2.ico")
    
    Label(pantalla31, text="¡Cita agregada!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla31, text="", bg="white").pack()
    
    Button(pantalla31, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla23.destroy()]).pack()
    Label(pantalla31, text="", bg="white").pack()

##Pantallas de modificado
def modificado_r():
    global pantalla32
    pantalla32 = Toplevel(pantalla9)
    pantalla32.geometry("360x150")
    pantalla32.configure(bg='white')
    pantalla32.title("Practi-Citas MD")
    pantalla32.iconbitmap("Logo2.ico")
    
    Label(pantalla32, text="¡Recepcionista modificado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla32, text="", bg="white").pack()
    
    Button(pantalla32, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_recep(),pantalla9.destroy()]).pack()
    Label(pantalla32, text="", bg="white").pack()

def modificado_m():
    global pantalla33
    pantalla33 = Toplevel(pantalla13)
    pantalla33.geometry("360x150")
    pantalla33.configure(bg='white')
    pantalla33.title("Practi-Citas MD")
    pantalla33.iconbitmap("Logo2.ico")
    
    Label(pantalla33, text="¡Médico modificado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla33, text="", bg="white").pack()
    
    Button(pantalla33, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_med(),pantalla13.destroy()]).pack()
    Label(pantalla33, text="", bg="white").pack()

def modificado_con():
    global pantalla34
    pantalla34 = Toplevel(pantalla17)
    pantalla34.geometry("360x150")
    pantalla34.configure(bg='white')
    pantalla34.title("Practi-Citas MD")
    pantalla34.iconbitmap("Logo2.ico")
    
    Label(pantalla34, text="¡Consultorio modificado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla34, text="", bg="white").pack()
    
    Button(pantalla34, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla17.destroy()]).pack()
    Label(pantalla34, text="", bg="white").pack()

def modificado_p():
    global pantalla35
    pantalla35 = Toplevel(pantalla21)
    pantalla35.geometry("360x150")
    pantalla35.configure(bg='white')
    pantalla35.title("Practi-Citas MD")
    pantalla35.iconbitmap("Logo2.ico")
    
    Label(pantalla35, text="¡Paciente modificado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla35, text="", bg="white").pack()
    
    Button(pantalla35, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla21.destroy()]).pack()
    Label(pantalla35, text="", bg="white").pack()

def modificado_c():
    global pantalla36
    pantalla36 = Toplevel(pantalla25)
    pantalla36.geometry("360x150")
    pantalla36.configure(bg='white')
    pantalla36.title("Practi-Citas MD")
    pantalla36.iconbitmap("Logo2.ico")
    
    Label(pantalla36, text="¡Cita modificada!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla36, text="", bg="white").pack()
    
    Button(pantalla36, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla25.destroy()]).pack()
    Label(pantalla36, text="", bg="white").pack()

##Pantallas de eliminado
def eliminado_r():
    global pantalla37
    pantalla37 = Toplevel(pantalla10)
    pantalla37.geometry("360x150")
    pantalla37.configure(bg='white')
    pantalla37.title("Practi-Citas MD")
    pantalla37.iconbitmap("Logo2.ico")
    
    Label(pantalla37, text="¡Recepcionista eliminado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla37, text="", bg="white").pack()
    
    Button(pantalla37, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_recep(),pantalla10.destroy()]).pack()
    Label(pantalla37, text="", bg="white").pack()

def eliminado_m():
    global pantalla38
    pantalla38 = Toplevel(pantalla14)
    pantalla38.geometry("360x150")
    pantalla38.configure(bg='white')
    pantalla38.title("Practi-Citas MD")
    pantalla38.iconbitmap("Logo2.ico")
    
    Label(pantalla38, text="¡Médico eliminado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla38, text="", bg="white").pack()
    
    Button(pantalla38, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_med(),pantalla14.destroy()]).pack()
    Label(pantalla38, text="", bg="white").pack()

def eliminado_con():
    global pantalla39
    pantalla39 = Toplevel(pantalla18)
    pantalla39.geometry("360x150")
    pantalla39.configure(bg='white')
    pantalla39.title("Practi-Citas MD")
    pantalla39.iconbitmap("Logo2.ico")
    
    Label(pantalla39, text="¡Consultorio eliminado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla39, text="", bg="white").pack()
    
    Button(pantalla39, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla18.destroy()]).pack()
    Label(pantalla39, text="", bg="white").pack()

def eliminado_p():
    global pantalla40
    pantalla40 = Toplevel(pantalla22)
    pantalla40.geometry("360x150")
    pantalla40.configure(bg='white')
    pantalla40.title("Practi-Citas MD")
    pantalla40.iconbitmap("Logo2.ico")
    
    Label(pantalla40, text="¡Paciente eliminado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla40, text="", bg="white").pack()
    
    Button(pantalla40, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla22.destroy()]).pack()
    Label(pantalla40, text="", bg="white").pack()

def eliminado_c():
    global pantalla41
    pantalla41 = Toplevel(pantalla26)
    pantalla41.geometry("360x150")
    pantalla41.configure(bg='white')
    pantalla41.title("Practi-Citas MD")
    pantalla41.iconbitmap("Logo2.ico")
    
    Label(pantalla41, text="¡Cita eliminada!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla41, text="", bg="white").pack()
    
    Button(pantalla41, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla26.destroy()]).pack()
    Label(pantalla41, text="", bg="white").pack()

def salir():
    global pantalla6
    pantalla6 = Toplevel(pantalla0)
    pantalla6.geometry("360x150")
    pantalla6.configure(bg='white')
    pantalla6.title("Practi-Citas MD")
    pantalla6.iconbitmap("Logo2.ico")
    
    Label(pantalla6, text="¿Estás seguro de que deseas salir?", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla6, text="", bg="white").pack()
    
    Button(pantalla6, text="Si", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=pantalla0.destroy).pack()
    Label(pantalla6, text="", bg="white").pack()
    
    Button(pantalla6, text="No", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=pantalla6.destroy).pack()
    Label(pantalla6, text="", bg="white").pack()