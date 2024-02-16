


def impresionCostoDeTienda(producto, precio, descuento):
    print ('Precio del Producto     :' + producto + ' con precio de ' + str(precio) 
    + ' tiene un descuento de ' + str(int(precio)*float(descuento)))
    return (float(precio)-int(precio)*float(descuento))


def ingreseTransaccion():
    productoTienda=input('Ingrese Producto :')
    precioTienda =input('Ingrese Precio :')
    descuentoTienda = input('Ingrese Descuento :')
    valorAPagar=impresionCostoDeTienda(productoTienda,precioTienda,descuentoTienda)
    print('Debe pagar un total de   :' + str(valorAPagar))

ingreseTransaccion()
