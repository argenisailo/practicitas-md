import psycopg2

def eliminar_ad(id):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    op="delete from administrador where id_admin = %s"
    cursor1.execute(op,[id])
    con.commit()
    cursor1.close()

def buscar_ad(id):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    op="select * from administrador where id_admin = %s"
    cursor1.execute(op,[id])
    line=cursor1.fetchall()

    for row in line:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])
        print(row[5])
        print(row[6])
    
    cursor1.close()

def agregar_ad(i,c,n,a,t,te,d):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[i,c,n,a,t,te,d]
    dato2=[i,c]

    cursor1.execute("insert into administrador (id_admin,pass_a,nombre_a,apellido_a,turno_a,telefono_a,domicilio_a) values (%s,%s,%s,%s,%s,%s,%s) ",dato)
    cursor1.execute("insert into usuarios (id_usuario,pass_us) values (%s,%s)",dato2)
    con.commit()
    cursor1.close()
    con.close()
    
def modificar_ad(c,n,a,e,t,d,id):
    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    dato=[c,n,a,e,t,d,id]

    cursor1.execute("update administrador set pass_a=%s,nombre_a=%s,apellido_a=%s,turno_a=%s,telefono_a=%s,domicilio_a=%s where id_admin=%s",dato)
    con.commit()
    cursor1.close()
    con.close()

