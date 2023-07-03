from random import randint

class ActuadorError(Exception):
    def __init__(self,actuadorId,errorType):
        super().__init__()
        self.actuadorId = actuadorId
        self.errorType = errorType

    def __str__(self) -> str:
        return f"Error al encender el actuador {self.actuadorId} ({self.errorType})"

class Actuador:
    def __init__(self,id,tipo):
        self.id = id
        self.tipo = tipo

class Modelo:
    actuador1 = Actuador("1","Luz")
    actuador2 = Actuador("2","Persiana")
    actuador3 = Actuador("3","Electrodoméstico")
    actuadores = [actuador1,actuador2,actuador3]

    def encender(self,id):
        tipo = ""
        num = randint(1,3)
        if num == 3:
            raise ActuadorError(id,"Error de encendido")
        for item in self.actuadores:
            if item.id == str(id):
                tipo = item.tipo
        print(f"Se ha encendido el actuador {id} ({tipo})")
        return f"Se ha encendido el actuador {id} ({tipo})"






    





















