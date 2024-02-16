# w -- borra todo y escribe el archivo
# a -- escriba en el archivo
# r -- lee el archivo

archivo = open('Archivo_Prueba.txt','a')

archivo.write('Creacion de texto\n')

archivo.close()


archivo = open('Archivo_Prueba.txt','r')
#archivo.write('Creacion de texto\n')
print(archivo.read())
archivo.close()
