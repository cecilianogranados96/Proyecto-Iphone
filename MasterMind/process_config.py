#!../python35/python.exe
print ("Content-type: text/html\n")
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
nombre = form.getfirst("nombre");
dificuldad = form.getfirst("dificuldad");
pocision = form.getfirst("pocision");
elementos = form.getfirst("elementos");
reloj = form.getfirst("reloj");

tiempo_juego = form.getfirst("tiempo_juego");
tiempo_jugada = form.getfirst("tiempo_jugada");

config = open("datos/config.dat","w")
config.write(nombre+","+dificuldad+","+pocision+","+elementos+","+reloj+","+tiempo_jugada+","+tiempo_juego)
print('''<body><script type="text/javascript">window.location="config.py";</script></body>''')