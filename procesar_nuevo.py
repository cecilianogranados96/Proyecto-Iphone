#!../python35/python.exe
import cgi
import operator
from funciones import * 
from vectores import * 
import shutil

print ("Content-type: text/html\n")

import os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()


fileitem = form['imagen']
if fileitem.filename:
   fn = os.path.basename(fileitem.filename)
   open("datos/imagenes/" +fn, 'wb').write(fileitem.file.read())
   imagen = fn
else:
   imagen = "None"


tono = form['tono']
if tono.filename:
   fn2 = os.path.basename(tono.filename)
   open("datos/tonos/" +fn2, 'wb').write(tono.file.read())
   tono = fn2
else:
   tono = "None"

  
datos = ""
for x in obligatorios:
	if (x == "imagen"):
		datos += imagen + ","
	elif (x == "tono"):
		datos += tono + ","
	elif str(form.getfirst(x)) == "":
		datos += "None,"
	else:
		datos += str(form.getfirst(x))+ "," 


telefonos = ""
for x in tupla: #Telefonos
	telefonos += str(form.getfirst(x)) + "~"


emails = ""
for x in tupla2: #Telefonos
		emails += str(form.getfirst(x)) + "~"

adicionales_orden = sorted(adicionales.items(), key=operator.itemgetter(0))

adicion = ""
for clave in adicionales_orden:
		adicion += str(form.getfirst(clave[0])) + "~"

		
vector = datos + telefonos +","+ emails +","+ adicion

#print(datos)

insertar(vector)


print('''<body><script type="text/javascript">window.location="contacto.py";</script></body>''')




