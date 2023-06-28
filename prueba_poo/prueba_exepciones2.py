from random import randint,random

class SensorError(Exception):
    def __init__(self,sensorId,errorType):
        super().__init__()
        self.sensorId = sensorId
        self.errorType = errorType

    def __str__(self) -> str:
        return f"Error en el sensor {self.sensorId} ({self.errorType})"

class Sensor:
    def __init__(self,id,tipo):
        self.id = id
        self.tipo = tipo

class Modelo:
    sensor1 = Sensor("1","Temperatura")
    sensor2 = Sensor("2","Humedad")
    sensor3 = Sensor("3","Presión")
    sensores = [sensor1,sensor2,sensor3]

    def leerDato(self,id):
        numeroRan = random()
        numError = randint(0,3)
        if numError == 2:
            raise SensorError(id,"Error de lectura")
        tipo=""
        for sensor in self.sensores:
            if sensor.id == str(id):
                tipo = sensor.tipo
        print(f"Dato del sensor {id} ({tipo}): {numeroRan}")

class Controlador:
    def __init__(self,modelo,vista):
        self.modelo = modelo
        self.vista = vista

    def leerDato(self,id):
        self.modelo.leerDato(id)

class Vista:
    def leerDato(self,id):
        self.controlador.leerDato(id)
    
    def run(self):
        print("-- Sistema de control de sensores --")

modelo = Modelo()
vista = Vista()
controlador = Controlador(modelo,vista)
vista.controlador = controlador
vista.run()
for i in range(3):
    try:
        vista.leerDato(i+1)
    except Exception as error:
        print(error)
    





















