from concurrent.futures import thread
from datetime import datetime, timedelta
from threading import Thread
from time import sleep

class Temporizador(Thread):
    def __init__(self, hora, delay, funcion):
        super(Temporizador, self).__init__()
        self._estado = True
        self.hora = hora
        self.delay = delay
        self.funcion = funcion

    def stop(self):
        self._estado = False

    def run(self):
        aux = datetime.strptime(self.hora, '%H:%M:%S')
        hora = datetime.now()
        hora = hora.replace(hour = aux.hour, minute=aux.minute, second=aux.second, microsecond = 0)
        if hora <= datetime.now():
            hora += timedelta(days=1)

        while self._estado:
            if hora <= datetime.now():
                self.funcion()
                hora += timedelta(days=1)
            sleep(self.delay)
        











