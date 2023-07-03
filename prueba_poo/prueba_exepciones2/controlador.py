from modelo import Modelo
from vista import Vista

class Controlador(Modelo,Vista):
    def __init__(self):
        super().__init__()

    def vistaEncender(self):
        super().vistaEncender()
        data = [self.sensor1Var,self.sensor2Var,self.sensor3Var]
        for i in range(len(self.sensores)):
            try:
                resultado = self.leerDato(i+1)
                data[i].set(resultado)
            except Exception as error:
                data[i].set(error)
                print(error)