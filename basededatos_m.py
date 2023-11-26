import psycopg2

def eliminar_m(id):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    op="delete from medico where id_m = %s"
    cursor1.execute(op,[id])
    con.commit()
    cursor1.close()

#agregar cedula

def agregar_m(i,c,n,a,ce,e,t,d,nc):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[i,c,n,a,ce,e,t,d,nc]
    dato2=[i,c]

    cursor1.execute("insert into medico (id_m,pass_m,nombre_m,apellido_m,cedula_m,especialidad_m,telefono_m,domicilio_m,n_con) values (%s,%s,%s,%s,%s,%s,%s,%s,%s) ",dato)
    cursor1.execute("insert into usuarios (id_usuario,pass_us) values (%s,%s)",dato2)
    con.commit()
    cursor1.close()
    con.close()
    

def modificar_m(c,n,a,ce,e,t,d,nc,id):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[c,n,a,ce,e,t,d,nc,id]

    cursor1.execute("update medico set pass_m=%s,nombre_m=%s,apellido_m=%s,cedula_m=%s,especialidad_m=%s,telefono_m=%s,domicilio_m=%s,n_con=%s where id_m =%s",dato)
    con.commit()
    cursor1.close()
    con.close()




