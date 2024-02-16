# La clase tiene una nomenclatura Sustantivos con la primera letra en Mayuscula

from Empleado import Empleado
from Cliente import Cliente

personas= []

def datosBasicos():
    global nombre          
    nombre          = input('Ingrese el Nombre de la persona            : ')
    global apellidoPaterno 
    apellidoPaterno = input('Ingrese el apellido Paterno de la persona  : ')
    global apellidoMaterno 
    apellidoMaterno = input('Ingrese el apellido Materno de la persona  : ')
    global edad            
    edad            = input('Ingrese la edad de la persona              : ')


def cargar():
    respuesta       = input('Ingreso de Personda Cliente/1 o Empleado/2 : ')
    if str(respuesta) == '1':
        datosBasicos()
        tipoCliente = input('Ingrese el tipo de Cliente                 : ')
        cli = Cliente(nombre,apellidoPaterno,apellidoMaterno,edad,tipoCliente)
        personas.append(cli)
    elif str(respuesta) == '2':
        datosBasicos()
        sueldo = input('Ingrese el sueldo del Empleado                  : ')
        puesto = input('Ingrese el puesto del Empleado                  : ')
        emp = Empleado(nombre,apellidoPaterno,apellidoMaterno,edad,sueldo,puesto)
        personas.append(emp)
    else:
        print('el tipo de Persona no es valido')
        deseoDeIntento = input('¿Desea seguir?: ')
        if str(deseoDeIntento).lower()=='si':
            cargar()

cargar()
for per in personas:
    print(per)
