

class Vehiculo:
    def __init__(self,Indice,Marca,Modelo,Placa,Ano) -> None:
        self.indice = Indice
        self.marca  = Marca
        self.modelo = Modelo
        self.placa  = Placa
        self.ano    = Ano
    def __str__(self) -> str:
        return self.indice + '|' + self.marca + '|' + self.modelo + '|' + self.placa + '|' + self.ano + '\n'
        #return '|'.join(self)

    