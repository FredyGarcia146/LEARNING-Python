
from Vehiculo import Vehiculo
import os

def ingresoDatos(datosVehiculo):
    datos = datosVehiculo
    archivo = open('Practica_20220830_POO\Practica_POO_02\Vehiculos.txt','a')
    archivo.write(datos)
    archivo.close()

def contarRegistros():
    if os.path.isfile('Practica_20220830_POO\Practica_POO_02\Vehiculos.txt'):
        archivo = open('Practica_20220830_POO\Practica_POO_02\Vehiculos.txt','r')
        contenido = archivo.read().splitlines()
        print(len(contenido))
        return len(contenido)+1
    else:
        return 1

def cargarDatos():
    indice  =contarRegistros()
    marca   =input('Marca   : ')
    modelo  =input('Modelo  : ')
    placa   =input('Placa   : ')
    ano     =input('Año     : ')

    vehiculo= Vehiculo(str(indice),marca,modelo,placa,ano)
    ingresoDatos(str(vehiculo))

cargarDatos()

