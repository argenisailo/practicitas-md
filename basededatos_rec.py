import psycopg2

def eliminar_r(id):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    op="delete from recepcion where id_recepcion = %s"
    cursor1.execute(op,[id])
    con.commit()
    cursor1.close()

def agregar_r(i,c,n,a,tu,j,te,d):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[i,c,n,a,tu,j,te,d]
    dato2=[i,c]

    cursor1.execute("insert into recepcion (id_recepcion,pass_r,nombre_r,apellido_r,turno_r,jornada_r,telefono_r,domicilio_r) values (%s,%s,%s,%s,%s,%s,%s,%s) ",dato)
    cursor1.execute("insert into usuarios (id_usuario,pass_us) values (%s,%s)",dato2)
    con.commit()
    cursor1.close()
    con.close()

def modificar_r(id,c,n,a,tu,j,te,d):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[c,n,a,tu,j,te,d,id]

    cursor1.execute("update recepcion set pass_r=%s,nombre_r=%s,apellido_r=%s,turno_r=%s,jornada_r=%s,telefono_r=%s,domicilio_r=%s where id_recepcion =%s",dato)
    con.commit()
    cursor1.close()
    con.close()