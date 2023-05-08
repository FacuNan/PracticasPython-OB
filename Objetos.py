class Juguete:
    _encendido = False

    def encendido(self):
        self._encendido = True

    def apaga(self):
        self._encendido = False

    def isEncendido(self):
        return self._encendido


d1 = Juguete()

d1.encendido()
d1.apaga()

print(d1.isEncendido())


class Estatica:
    numero = 1

    def incrementa(self):
        numero += 1



#Herencias


class Dino(Juguete):
    color = None
    nombre = None
    def __init__(self, nombre):
        self.color = "Verde"
        self.nombre = nombre

    Escamas = 35
    def verEscamas(self):
        return self.Escamas

p = Dino("Facu")

print(p.nombre)
#Relaciones Has-a#

class motor():
    tipo = "Diesel"

class ventanas():
    cantidad = 5

class coche():
    motor = motor()
    ventanas = ventanas()



moto = coche()

print(moto.motor.tipo)







