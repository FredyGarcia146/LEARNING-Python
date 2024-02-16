from Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad,tipo) -> None:
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, edad)
        self.tipoCliente = tipo
