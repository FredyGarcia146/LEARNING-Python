class Persona:
    def __init__(self,nombre,apellidoPaterno,apellidoMaterno,edad) -> None:
        self.nombre_    = nombre
        self.apellidoP  = apellidoPaterno
        self.apellidoM  = apellidoMaterno
        self.edad_      = edad

    def __str__(self):
        return self.nombre_ + ' ' + self.apellidoP + ' ' + self.apellidoM