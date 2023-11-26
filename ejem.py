from hora_correos import *
from correos import *
from datetime import datetime

def ejecutar():
    t=Temporizador('12:59:00',1,correos)
    t.start()
    t.stop()

a=datetime.now()

print(a.hour)

if a.hour == 13:
    correos()