# La clase tiene una nomenclatura Sustantivos con la primera letra en Mayuscula


class Persona:
    def __init__(self,nombre,apellidoMaterno,apellidoPaterno,edad) -> None:
        self.nombre_    = nombre
        self.apellidoM  = apellidoMaterno
        self.apellidoP  = apellidoPaterno
        self.edad_      = edad

class Empleado(Persona):
    def __init__(self, nombre, apellidoMaterno, apellidoPaterno, edad, salario, puesto) -> None:
        super().__init__(nombre, apellidoMaterno, apellidoPaterno, edad)
        self.salario_   = salario
        self.puesto_    = puesto


class Cliente(Persona):
    def __init__(self, nombre, apellidoMaterno, apellidoPaterno, edad) -> None:
        super().__init__(nombre, apellidoMaterno, apellidoPaterno, edad)


emp = Empleado('Juan', 'Domingo','Perez',32,7000.0,'Estadistico Informatico')
cli = Cliente('Pedro', 'Salveltro','Prieto',28)
