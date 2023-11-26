import psycopg2

def eliminar_c(id):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    op="delete from citas where id_cita = %s"
    cursor1.execute(op,[id])
    con.commit()
    cursor1.close()

def buscar_c(id):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    op="select n_con, nombre_m, especialidad_m, hora_c, id_paciente, fecha_c from citas as c inner join medico as m on c.id_med= m.id_m and id_cita=%s"
    cursor1.execute(op,[id])
    line=cursor1.fetchall()

    for row in line:
        print('Número de consultorio: ', row[0])
        print('Nombre del médico: ', row[1])
        print('Especialidad médica: ', row[2])
        print('Hora: ', row[3])
        print('ID del paciente: ', row[4])
        print('Fecha: ', row[5])
    
    cursor1.close()

def agregar_c(i,p,mc,h,f,id_m):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[i,p,mc,h,f,id_m]

    cursor1.execute("insert into citas (id_cita,id_paciente,id_med,hora_c,fecha_c,id_med) values (%s,%s,%s,%s,%s,%s) ",dato)
    con.commit()
    cursor1.close()
    con.close()

def modificar_c(p,mc,h,f,id_m,id):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[p,mc,h,f,id_m,id]

    cursor1.execute("update citas set id_paciente=%s,id_mc=%s,hora_c=%s,fecha_c=%s, id_med=%s where id_cita =%s",dato)
    con.commit()
    cursor1.close()
    con.close()

