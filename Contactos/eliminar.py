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
id = form.getfirst("num")

eliminar(int(id))


print('''<body>
<script type="text/javascript">alert("Eliminado con exito!")</script>

<script type="text/javascript">window.location="contacto.py";</script></body>''')




