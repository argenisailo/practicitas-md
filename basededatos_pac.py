import psycopg2

def eliminar_p(id):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    op="delete from pacientes where id_pacientes = %s"
    cursor1.execute(op,[id])
    con.commit()
    cursor1.close()

def agregar_p(i,n,a,t,c,e,nu,h):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[i,n,a,t,c,e,nu,h]

    cursor1.execute("insert into pacientes (id_pacientes,nombre_p,apellido_p,telefono_p,correo_p,edad_p,n_exp,historial_p) values (%s,%s,%s,%s,%s,%s,%s,%s) ",dato)
    con.commit()
    cursor1.close()
    con.close()

def modificar_p(i,n,a,t,c,e,nu,h):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[i,n,a,t,c,e,nu,h,i]

    cursor1.execute("update citas set id_paciente=%s,nombre_p=%s,apellido_p=%s,telefono_p=%s,correo_p=%s,edad_p=%s,n_exp=%s,historial_p=%s where id_cita =%s",dato)
    con.commit()
    cursor1.close()
    con.close()

