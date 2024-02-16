from Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, salario, puesto):
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, edad)
        self.salario_   = salario
        self.puesto_    = puesto