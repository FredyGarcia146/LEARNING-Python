# PE Variables --> POO Propiedades
# PE Funciones --> POO Metodos



class Triangulo:
    def __init__(self,base,alto) -> None:
        self.baseTriangulo = base
        self.altoTriangulo = alto
    
    def areaTringulo(self):
        area = self.baseTriangulo*self.altoTriangulo/2
        return area


figura = Triangulo(10,15)
print('Base del trinagulo : ' + str(figura.baseTriangulo))
print('Alto del trinagulo : ' + str(figura.altoTriangulo))
print('Area del trinagulo : ' + str(figura.areaTringulo()))


