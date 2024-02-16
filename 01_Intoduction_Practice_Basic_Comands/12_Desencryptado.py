
# archivo = open('Credenciales.txt','w')
# archivo.write('Usuario     : gatitos21 \nContrasena  : perritos21')
# archivo.close()

archivo  = open('Credenciales.txt','r')
contenidoArchivo = archivo.read()
archivo.close()

accion = input('Ingrese accion 1/encryptar 2/desencryptar : ')

def encryptar(contenido) :
    print(contenido)
    textoFinal =''
    for letra in contenido:
        textoFinal +=chr(ord(letra)+1)
    mensajeEncriptado = textoFinal
    archivo = open('Credenciales.txt','w')
    archivo.write(mensajeEncriptado)
    archivo.close()
    return(mensajeEncriptado)
    
def desencryptar(contenido):
    print(contenido)
    textoFinal =''
    for letra in contenido:
        textoFinal +=chr(ord(letra)-1)
    mensajeDesencriptado = textoFinal
    archivo = open('Credenciales.txt','w')
    archivo.write(mensajeDesencriptado)
    archivo.close()
    return(mensajeDesencriptado)


if accion == 1 or accion =='1':
    print('Mensaje Encryptado: \n'+ encryptar(contenidoArchivo))  
else:
    if accion ==2 or accion=='2':
        print('Mensaje Desencryptado: \n'+desencryptar(contenidoArchivo))
    else:
        print('No hay accion, pruebe con 1 o 2')




