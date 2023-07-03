from modelo import Modelo
from vista import Vista

class Controlador(Modelo,Vista):
    def __init__(self):
        super().__init__()

    def vistaEncender(self):
        super().vistaEncender()
        data = [self.actuador1Var,self.actuador2Var,self.actuador3Var]
        for i in range(len(self.actuadores)):
            try:
                estado = self.encender(i+1)
                data[i].set(estado)
            except Exception as error:
                data[i].set(error)
                print(error)