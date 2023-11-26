from email import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from datetime import date
import psycopg2

from hora_correos import *

r=0


#instancia del mensaje 
def correos():
    print("legue a la funcion correos ")
    msg=MIMEMultipart()

    today=date.today()


    con=psycopg2.connect(database="CONSULTORIO", user="postgres",
    password="numero10",host="localhost")
    cursor1=con.cursor()

    op="select id_paciente, hora_c from citas where fecha_c=%s"
    cursor1.execute(op,[today])
    line=cursor1.fetchall()

    for row in line:

        id_p=line[r][0]
        hora=line[r][1] 
        op2="select nombre_p,correo_p from pacientes where id_pacientes=%s"
        cursor1.execute(op2,[id_p])
        line2=cursor1.fetchall()

        correo=line2[0][1]#cambiar el 0
        nombre=line2[0][0]#ca,biar el 0

        message =("Hola buenos dias {0}, Le recordamos su cita en la clinica, el dia {1}, a las {2}".format(nombre,today,hora))
            #parametros

        password="Ale123roblesmora"
        msg['From']="practicitasmd@gmail.com"
        msg['To']="{}".format(correo)
        msg['Subject']="Cita en la clinica equipo9"

            #cuerpo del mensaje 
        msg.attach(MIMEText(message,'plain'))

            #crear servidor
        server=smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

            #ingresar credenciales 
        server.login(msg['From'],password)
        server.sendmail(msg['From'],msg['To'],msg.as_string())
        server.quit()
        r+=1



