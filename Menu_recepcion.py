import tkinter
from tkinter import *
from tkinter import messagebox, ttk
import random
import psycopg2

from basededatos_con import *
from basededatos_pac import *
from basededatos_citas import *

global id_p, id_con, id_c
global entry_id_p, entry_nom_p, entry_ape_p, entry_tel_p, entry_correo_p, entry_edad_p, entry_n_exp, entry_con_p, entry_his_p, entry_citas_pend

global entry_id_con, entry_n_con, entry_m_cargo, entry_esp_med, entry_p_cargo, entry_turno_con, entry_his_con, entry_citas_dia

global entry_id_c, entry_hora_c, entry_fecha_c, entry_id_m

def menu_recep():
    global pantalla0
    pantalla0=Tk()
    pantalla0.geometry("650x430")
    pantalla0.configure(bg='white')
    pantalla0.title("Practi-Citas MD (Recepcionista)")
    pantalla0.iconbitmap("Logo2.ico")
    
    Label(pantalla0, text="Bienvenido a tu menú principal", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 20)).pack()
    
    Label(pantalla0, text="Haz clic sobre cualquier sección del sistema a la que deseas ingresar: ", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla0, text="", bg="white").pack()
    
    Button(pantalla0, text="Consultorios", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla0.destroy()]).pack()
    Label(pantalla0, text="", bg="white").pack()
    
    Button(pantalla0, text="Pacientes", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla0.destroy()]).pack()
    Label(pantalla0, text="", bg="white").pack()
    
    Button(pantalla0, text="Citas", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla0.destroy()]).pack()
    Label(pantalla0, text="", bg="white").pack()
    
    Button(pantalla0, text="Salir", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=salir).pack()
    Label(pantalla0, text="", bg="white").pack()
    
def info_consul():
    global pantalla2
    pantalla2=Tk()
    pantalla2.geometry("500x360")
    pantalla2.configure(bg='white')
    pantalla2.title("Practi-Citas MD (Recepcionista)")
    pantalla2.iconbitmap("Logo2.ico")
    
    Label(pantalla2, text="Bienvenido al menú de Consultorios", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 18)).pack()
    
    Label(pantalla2, text="Haz clic sobre la opción que deseas realizar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla2, text="", bg="white").pack()
    
    Button(pantalla2, text="Agregar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_consul(),pantalla2.destroy()]).pack()
    Label(pantalla2, text="", bg="white").pack()
    
    Button(pantalla2, text="Buscar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[buscar_consul(),pantalla2.destroy()]).pack()
    Label(pantalla2, text="", bg="white").pack()
    
    Button(pantalla2, text="Modificar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_consul(),pantalla2.destroy()]).pack()
    Label(pantalla2, text="", bg="white").pack()
    
    Button(pantalla2, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[menu_recep(),pantalla2.destroy()]).pack()
    Label(pantalla2, text="", bg="white").pack()

    def agregar_consul():
        global pantalla6
        pantalla6=Tk()
        pantalla6.geometry("700x580")
        pantalla6.configure(bg='white')
        pantalla6.title("Practi-Citas MD (Recepcionista)")
        pantalla6.iconbitmap("Logo2.ico")
    
        Label(pantalla6, text="Agregar un consultorio", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla6, text="Introduce los datos correspondientes:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        Label(pantalla6, text="", bg="white").pack()
    
        Label(pantalla6, text="ID: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        id_con = random.randint(1000, 9999)
        Label(pantalla6, text=id_con, bg="white", fg="black", font=('Bahnschrift SemiLight', 10)).pack()
        Label(pantalla6, text="", bg="white").pack()
    
        Label(pantalla6, text="Número de consultorio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_n_con = Entry(pantalla6)
        entry_n_con.pack()
        Label(pantalla6, text="", bg="white").pack()
    
        Button(pantalla6, text="Agregar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_co(int(id_con),entry_n_con.get()),agregado_con()]).pack()
        Label(pantalla6, text="", bg="white").pack()

        Button(pantalla6, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla6.destroy()]).pack()
        Label(pantalla6, text="", bg="white").pack()

    def buscar_consul():
        global pantalla7
        pantalla7=Tk()
        pantalla7.geometry("700x580")
        pantalla7.configure(bg='white')
        pantalla7.title("Practi-Citas MD (Recepcionista)")
        pantalla7.iconbitmap("Logo2.ico")
    
        Label(pantalla7, text="Buscar un consultorio", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla7, text="Introduce el ID del consultorio que deseas buscar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_con = Entry(pantalla7)
        entry_id_con.pack()
        Label(pantalla7, text="", bg="white").pack()
    
        Button(pantalla7, text="Buscar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_co(entry_id_con.get())).pack()
        Label(pantalla7, text="", bg="white").pack()

        listbox = Listbox(pantalla7, width=100, height=2)
        listbox.pack()
        Label(pantalla7, text="", bg="white").pack()
    
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

        Button(pantalla7, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla7.destroy()]).pack()
        Label(pantalla7, text="", bg="white").pack()

    def modificar_consul():
        global pantalla8
        pantalla8=Tk()
        pantalla8.geometry("700x580")
        pantalla8.configure(bg='white')
        pantalla8.title("Practi-Citas MD (Recepcionista)")
        pantalla8.iconbitmap("Logo2.ico")
    
        Label(pantalla8, text="Modificar un consultorio", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla8, text="Introduce el ID del consultorio que deseas modificar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_con = Entry(pantalla8)
        entry_id_con.pack()
        Label(pantalla8, text="", bg="white").pack()
    
        Button(pantalla8, text="Buscar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_co(entry_id_con.get())).pack()
        Label(pantalla8, text="", bg="white").pack()

        listbox = Listbox(pantalla8, width=100, height=2)
        listbox.pack()
        Label(pantalla8, text="", bg="white").pack()

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
    
        Label(pantalla8, text="Número de consultorio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_n_con = Entry(pantalla8)
        entry_n_con.pack()
        Label(pantalla8, text="", bg="white").pack()
    
        Button(pantalla8, text="Modificar consultorio", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_co(entry_id_con.get(),entry_n_con.get()),modificado_con()]).pack()
        Label(pantalla8, text="", bg="white").pack()

        Button(pantalla8, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla8.destroy()]).pack()
        Label(pantalla8, text="", bg="white").pack()
    
def info_paciente():
    global pantalla3
    pantalla3=Tk()
    pantalla3.geometry("500x400")
    pantalla3.configure(bg='white')
    pantalla3.title("Practi-Citas MD (Recepcionista)")
    pantalla3.iconbitmap("Logo2.ico")
    
    Label(pantalla3, text="Bienvenido al menú de Pacientes", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 18)).pack()
    
    Label(pantalla3, text="Haz clic sobre la opción que deseas realizar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Agregar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_pac(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Buscar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[buscar_pac(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Modificar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_pac(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Eliminar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_pac(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()
    
    Button(pantalla3, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[menu_recep(),pantalla3.destroy()]).pack()
    Label(pantalla3, text="", bg="white").pack()

    def agregar_pac():
        global pantalla9
        pantalla9=Tk()
        pantalla9.geometry("700x580")
        pantalla9.configure(bg='white')
        pantalla9.title("Practi-Citas MD (Recepcionista)")
        pantalla9.iconbitmap("Logo2.ico")

        ##Scroll
        main_frame = Frame(pantalla9)
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
    
        Label(second_frame, text="Agregar un paciente", bg="white", fg="dark slate grey", font=('Bahnschrift SemiLight', 16)).pack()
    
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
    
        Button(second_frame, text="Agregar paciente", bg="steel blue", fg="white", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_p(int(id_p),entry_nom_p.get(),entry_ape_p.get(),entry_tel_p.get(),entry_correo_p.get(),entry_edad_p.get(),entry_n_exp.get(),entry_his_p.get()),agregado_p()]).pack()
        Label(second_frame, text="", bg="white").pack()

        Button(second_frame, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla9.destroy()]).pack()
        Label(second_frame, text="", bg="white").pack()

    def buscar_pac():
        global pantalla10
        pantalla10=Tk()
        pantalla10.geometry("700x580")
        pantalla10.configure(bg='white')
        pantalla10.title("Practi-Citas MD (Recepcionista)")
        pantalla10.iconbitmap("Logo2.ico")
    
        Label(pantalla10, text="Buscar un paciente", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla10, text="Introduce el ID del paciente que deseas buscar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_p = Entry(pantalla10)
        entry_id_p.pack()
        Label(pantalla10, text="", bg="white").pack()
    
        Button(pantalla10, text="Buscar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_p(entry_id_p.get())).pack()
        Label(pantalla10, text="", bg="white").pack()

        listbox = Listbox(pantalla10, width=100, height=2)
        listbox.pack()
        Label(pantalla10, text="", bg="white").pack()
    
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

        Button(pantalla10, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla10.destroy()]).pack()
        Label(pantalla10, text="", bg="white").pack()

    def modificar_pac():
        global pantalla11
        pantalla11=Tk()
        pantalla11.geometry("700x580")
        pantalla11.configure(bg='white')
        pantalla11.title("Practi-Citas MD (Recepcionista)")
        pantalla11.iconbitmap("Logo2.ico")

        ##Scroll
        main_frame = Frame(pantalla11)
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

        Button(second_frame, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla11.destroy()]).pack()
        Label(second_frame, text="", bg="white").pack()

    def eliminar_pac():
        global pantalla12
        pantalla12=Tk()
        pantalla12.geometry("700x580")
        pantalla12.configure(bg='white')
        pantalla12.title("Practi-Citas MD (Recepcionista)")
        pantalla12.iconbitmap("Logo2.ico")
    
        Label(pantalla12, text="Eliminar un paciente", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla12, text="Introduce el ID del paciente que deseas eliminar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_p = Entry(pantalla12)
        entry_id_p.pack()
        Label(pantalla12, text="", bg="white").pack()
    
        Button(pantalla12, text="Buscar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_p(entry_id_p.get())).pack()
        Label(pantalla12, text="", bg="white").pack()

        listbox = Listbox(pantalla12, width=100, height=2)
        listbox.pack()
        Label(pantalla12, text="", bg="white").pack()

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

        Button(pantalla12, text="Eliminar paciente", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_p(entry_id_p.get()),eliminado_p()]).pack()
        Label(pantalla12, text="", bg="white").pack()

        Button(pantalla12, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla12.destroy()]).pack()
        Label(pantalla12, text="", bg="white").pack()
    
def info_cita():
    global pantalla4
    pantalla4=Tk()
    pantalla4.geometry("500x400")
    pantalla4.configure(bg='white')
    pantalla4.title("Practi-Citas MD (Recepcionista)")
    pantalla4.iconbitmap("Logo2.ico")
    
    Label(pantalla4, text="Bienvenido al menú de Citas", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 18)).pack()
    
    Label(pantalla4, text="Haz clic sobre la opción que deseas realizar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla4, text="", bg="white").pack()
    
    Button(pantalla4, text="Agregar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_cita(),pantalla4.destroy()]).pack()
    Label(pantalla4, text="", bg="white").pack()
    
    Button(pantalla4, text="Buscar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[buscar_cita(),pantalla4.destroy()]).pack()
    Label(pantalla4, text="", bg="white").pack()
    
    Button(pantalla4, text="Modificar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_cita(),pantalla4.destroy()]).pack()
    Label(pantalla4, text="", bg="white").pack()
    
    Button(pantalla4, text="Eliminar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_cita(),pantalla4.destroy()]).pack()
    Label(pantalla4, text="", bg="white").pack()
    
    Button(pantalla4, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[menu_recep(),pantalla4.destroy()]).pack()
    Label(pantalla4, text="", bg="white").pack()

    def agregar_cita():
        global pantalla13
        pantalla13=Tk()
        pantalla13.geometry("700x580")
        pantalla13.configure(bg='white')
        pantalla13.title("Practi-Citas MD (Recepcionista)")
        pantalla13.iconbitmap("Logo2.ico")
    
        Label(pantalla13, text="Agregar una cita", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla13, text="Introduce los datos correspondientes:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        Label(pantalla13, text="", bg="white").pack()
    
        Label(pantalla13, text="ID de la cita: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        id_c = random.randint(100000, 999999)
        Label(pantalla13, text=id_c, bg="white", fg="black", font=('Bahnschrift SemiLight', 10)).pack()
        Label(pantalla13, text="", bg="white").pack()
    
        Label(pantalla13, text="ID del paciente: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_p = Entry(pantalla13)
        entry_id_p.pack()
        Label(pantalla13, text="", bg="white").pack()
    
        Label(pantalla13, text="ID del consultorio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_con = Entry(pantalla13)
        entry_id_con.pack()
        Label(pantalla13, text="", bg="white").pack()
    
        Label(pantalla13, text="ID del médico: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_m = Entry(pantalla13)
        entry_id_m.pack()
        Label(pantalla13, text="", bg="white").pack()
    
        Label(pantalla13, text="Hora: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_hora_c = Entry(pantalla13)
        entry_hora_c.pack()
        Label(pantalla13, text="", bg="white").pack()
    
        Label(pantalla13, text="Fecha: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_fecha_c = Entry(pantalla13)
        entry_fecha_c.pack()
        Label(pantalla13, text="", bg="white").pack()

        Button(pantalla13, text="Agregar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[agregar_c(int(id_c),entry_id_p.get(),entry_id_con.get(),entry_id_m.get(),entry_hora_c.get(),entry_fecha_c.get()),agregado_c()]).pack()
        Label(pantalla13, text="", bg="white").pack()

        Button(pantalla13, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla13.destroy()]).pack()
        Label(pantalla13, text="", bg="white").pack()

    def buscar_cita():
        global pantalla14
        pantalla14=Tk()
        pantalla14.geometry("700x580")
        pantalla14.configure(bg='white')
        pantalla14.title("Practi-Citas MD (Recepcionista)")
        pantalla14.iconbitmap("Logo2.ico")
    
        Label(pantalla14, text="Buscar una cita", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        id_c=StringVar()
        Label(pantalla14, text="Introduce el ID de la cita que deseas buscar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_c = Entry(pantalla14, textvariable=id_c)
        entry_id_c.pack()
        Label(pantalla14, text="", bg="white").pack()
    
        Button(pantalla14, text="Buscar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_c(entry_id_c.get())).pack()
        Label(pantalla14, text="", bg="white").pack()

        listbox = Listbox(pantalla14, width=100, height=2)
        listbox.pack()
        Label(pantalla14, text="", bg="white").pack()
    
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

        Button(pantalla14, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla14.destroy()]).pack()
        Label(pantalla14, text="", bg="white").pack()

    def modificar_cita():
        global pantalla15
        pantalla15=Tk()
        pantalla15.geometry("700x580")
        pantalla15.configure(bg='white')
        pantalla15.title("Practi-Citas MD (Recepcionista)")
        pantalla15.iconbitmap("Logo2.ico")
    
        Label(pantalla15, text="Modificar una cita", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()
    
        Label(pantalla15, text="Introduce el ID de la cita que deseas modificar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_c = Entry(pantalla15)
        entry_id_c.pack()
        Label(pantalla15, text="", bg="white").pack()
    
        Button(pantalla15, text="Buscar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_c(entry_id_c.get())).pack()
        Label(pantalla15, text="", bg="white").pack()

        listbox = Listbox(pantalla15, width=100, height=2)
        listbox.pack()
        Label(pantalla15, text="", bg="white").pack()

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

        Label(pantalla15, text="ID del paciente: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_p = Entry(pantalla15)
        entry_id_p.pack()
        Label(pantalla15, text="", bg="white").pack()
    
        Label(pantalla15, text="ID del consultorio: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_con = Entry(pantalla15)
        entry_id_con.pack()
        Label(pantalla15, text="", bg="white").pack()
    
        Label(pantalla15, text="ID del médico: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_id_m = Entry(pantalla15)
        entry_id_m.pack()
        Label(pantalla15, text="", bg="white").pack()
    
        Label(pantalla15, text="Hora: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_hora_c = Entry(pantalla15)
        entry_hora_c.pack()
        Label(pantalla15, text="", bg="white").pack()
    
        Label(pantalla15, text="Fecha: ", bg="white", fg="steel blue", font=('Bahnschrift SemiLight', 10)).pack()
        entry_fecha_c = Entry(pantalla15)
        entry_fecha_c.pack()
        Label(pantalla15, text="", bg="white").pack()

        Button(pantalla15, text="Modificar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[modificar_c(entry_id_c.get(),entry_id_p.get(),entry_id_con.get(),entry_id_m.get(),entry_hora_c.get(),entry_fecha_c.get()),modificado_c()]).pack()
        Label(pantalla15, text="", bg="white").pack()

        Button(pantalla15, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla15.destroy()]).pack()
        Label(pantalla15, text="", bg="white").pack()

    def eliminar_cita():
        global pantalla16
        pantalla16=Tk()
        pantalla16.geometry("700x580")
        pantalla16.configure(bg='white')
        pantalla16.title("Practi-Citas MD (Recepcionista)")
        pantalla16.iconbitmap("Logo2.ico")
    
        Label(pantalla16, text="Eliminar una cita", bg="white", fg="dark slate grey", width="400", height="3", font=('Bahnschrift SemiLight', 16)).pack()

        Label(pantalla16, text="Introduce el ID de la cita que deseas eliminar:", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
        entry_id_c = Entry(pantalla16)
        entry_id_c.pack()
        Label(pantalla16, text="", bg="white").pack()
    
        Button(pantalla16, text="Buscar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:buscar_c(entry_id_c.get())).pack()
        Label(pantalla16, text="", bg="white").pack()

        listbox = Listbox(pantalla15, width=100, height=2)
        listbox.pack()
        Label(pantalla15, text="", bg="white").pack()

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

        Button(pantalla16, text="Eliminar cita", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[eliminar_c(entry_id_c.get()),eliminado_c()]).pack()
        Label(pantalla16, text="", bg="white").pack()

        Button(pantalla16, text="Regresar", bg="steel blue", fg="white", height="1", width="30", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla16.destroy()]).pack()
        Label(pantalla16, text="", bg="white").pack()

##Pantallas de agregado
def agregado_con():
    global pantalla29
    pantalla29 = Toplevel(pantalla6)
    pantalla29.geometry("360x150")
    pantalla29.configure(bg='white')
    pantalla29.title("Practi-Citas MD")
    pantalla29.iconbitmap("Logo2.ico")
    
    Label(pantalla29, text="¡Consultorio agregado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla29, text="", bg="white").pack()
    
    Button(pantalla29, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla6.destroy()]).pack()
    Label(pantalla29, text="", bg="white").pack()

def agregado_p():
    global pantalla30
    pantalla30 = Toplevel(pantalla9)
    pantalla30.geometry("360x150")
    pantalla30.configure(bg='white')
    pantalla30.title("Practi-Citas MD")
    pantalla30.iconbitmap("Logo2.ico")
    
    Label(pantalla30, text="¡Paciente agregado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla30, text="", bg="white").pack()
    
    Button(pantalla30, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla9.destroy()]).pack()
    Label(pantalla30, text="", bg="white").pack()

def agregado_c():
    global pantalla31
    pantalla31 = Toplevel(pantalla13)
    pantalla31.geometry("360x150")
    pantalla31.configure(bg='white')
    pantalla31.title("Practi-Citas MD")
    pantalla31.iconbitmap("Logo2.ico")
    
    Label(pantalla31, text="¡Cita agregada!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla31, text="", bg="white").pack()
    
    Button(pantalla31, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla13.destroy()]).pack()
    Label(pantalla31, text="", bg="white").pack()

##Pantallas de modificado
def modificado_con():
    global pantalla34
    pantalla34 = Toplevel(pantalla8)
    pantalla34.geometry("360x150")
    pantalla34.configure(bg='white')
    pantalla34.title("Practi-Citas MD")
    pantalla34.iconbitmap("Logo2.ico")
    
    Label(pantalla34, text="¡Consultorio modificado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla34, text="", bg="white").pack()
    
    Button(pantalla34, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_consul(),pantalla8.destroy()]).pack()
    Label(pantalla34, text="", bg="white").pack()

def modificado_p():
    global pantalla35
    pantalla35 = Toplevel(pantalla11)
    pantalla35.geometry("360x150")
    pantalla35.configure(bg='white')
    pantalla35.title("Practi-Citas MD")
    pantalla35.iconbitmap("Logo2.ico")
    
    Label(pantalla35, text="¡Paciente modificado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla35, text="", bg="white").pack()
    
    Button(pantalla35, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla11.destroy()]).pack()
    Label(pantalla35, text="", bg="white").pack()

def modificado_c():
    global pantalla36
    pantalla36 = Toplevel(pantalla15)
    pantalla36.geometry("360x150")
    pantalla36.configure(bg='white')
    pantalla36.title("Practi-Citas MD")
    pantalla36.iconbitmap("Logo2.ico")
    
    Label(pantalla36, text="¡Cita modificada!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla36, text="", bg="white").pack()
    
    Button(pantalla36, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla15.destroy()]).pack()
    Label(pantalla36, text="", bg="white").pack()

##Pantallas de eliminado
def eliminado_p():
    global pantalla40
    pantalla40 = Toplevel(pantalla12)
    pantalla40.geometry("360x150")
    pantalla40.configure(bg='white')
    pantalla40.title("Practi-Citas MD")
    pantalla40.iconbitmap("Logo2.ico")
    
    Label(pantalla40, text="¡Paciente eliminado!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla40, text="", bg="white").pack()
    
    Button(pantalla40, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_paciente(),pantalla12.destroy()]).pack()
    Label(pantalla40, text="", bg="white").pack()

def eliminado_c():
    global pantalla41
    pantalla41 = Toplevel(pantalla16)
    pantalla41.geometry("360x150")
    pantalla41.configure(bg='white')
    pantalla41.title("Practi-Citas MD")
    pantalla41.iconbitmap("Logo2.ico")
    
    Label(pantalla41, text="¡Cita eliminada!", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla41, text="", bg="white").pack()
    
    Button(pantalla41, text="Ok", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=lambda:[info_cita(),pantalla16.destroy()]).pack()
    Label(pantalla41, text="", bg="white").pack()

def salir():
    global pantalla5
    pantalla5 = Toplevel(pantalla0)
    pantalla5.geometry("360x150")
    pantalla5.configure(bg='white')
    pantalla5.title("Practi-Citas MD")
    pantalla5.iconbitmap("Logo2.ico")
    
    Label(pantalla5, text="¿Estás seguro de que deseas salir?", bg="white", fg="steel blue", width="400", height="1", font=('Bahnschrift SemiLight', 14)).pack()
    Label(pantalla5, text="", bg="white").pack()
    
    Button(pantalla5, text="Si", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=pantalla0.destroy).pack()
    Label(pantalla5, text="", bg="white").pack()
    
    Button(pantalla5, text="No", bg="steel blue", fg="white", height="1", width="15", font=('Bahnschrift SemiLight', 10), command=pantalla5.destroy).pack()
    Label(pantalla5, text="", bg="white").pack()