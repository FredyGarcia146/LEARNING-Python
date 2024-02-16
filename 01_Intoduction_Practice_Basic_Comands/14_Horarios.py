import datetime

x = datetime.datetime.now()

print (str(x))

print ("Fecha y hora en formato ISO = %s" % x.isoformat() )

print (u"Año = %s" %x.year)

print ("Mes = %s" %x.month)

print ("Dia =  %s" %x.day)

print ("Formato dd/mm/yyyy =  %s/%s/%s" % (x.day, x.month, x.year) )

print ("Hora = %s" %x.hour)

print ("Minutos = %s" %x.minute)

print ("Segundos =  %s" %x.second)

print ("Formato hh:mm:ss = %s:%s:%s" % (x.hour, x.month, x.second) )