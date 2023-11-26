import psycopg2

def eliminar_co(id):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    op1="delete from medico_cons where id_c =%s"
    cursor1.execute(op,[id])
    op="delete from consultorio where id_consultorio = %s"
    cursor1.execute(op,[id])

    con.commit()
    cursor1.close()

def agregar_co(i,n):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[i,n]

    cursor1.execute("insert into consultorio (id_consultorio,n_consultorio) values (%s,%s) ",dato)
    con.commit()
    cursor1.close()
    con.close()

def modificar_co(i,n,id):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[i,n,id]

    cursor1.execute("update consultorio set id_consultorio=%s,n_consultorio=%s where id_consultorio=%s",dato)
    con.commit()
    cursor1.close()
    con.close()

def med_cons(id_m,id_c):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[id_m,id_c]

    cursor1.execute("insert into medico_cons (id_m,id_c) values (%s,%s)",dato)
    con.commit()
    cursor1.close()
    con.close()


