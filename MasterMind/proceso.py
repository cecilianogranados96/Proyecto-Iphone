#!../python35/python.exe
print ("Content-type: text/html\n")
from funciones import * 
config = configuraciones()
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
real = form.getfirst("orden_real").split(",")
nombre = form.getfirst("nombre")
segundos = form.getfirst("tiempo")
dificultad = form.getfirst("dificultad")
#convertir a lista


tipo_partida = form.getfirst("tipo_partida")

numero = form.getfirst("num") 
valores = []
valores = form.getfirst("input").split(",")
print('''<td style="position: absolute; margin-top: '''+str(390-(47*int(numero)))+'''px;">
<table class="resultados" style="width: 100%;">
<tr>
<td style="font-size: 30px;">'''+form.getfirst("num")+'''</td>''')
#construccion de lo enviado 
for x in range (1,5):
	ruta = "datos/elementos/"+ config[3] + "/" + valores[x-1] + ".png"			
	print('''
		<td>
		   <div class="c con2" style="background: url('''+ruta+''') no-repeat;background-size: contain;"></div>
		</td>''')
print('''<td><table><tr>''')

if tipo_partida != 'None':
	jugadas = juego_actual(form.getfirst("input"))


r = resultado(valores,real)
if (r.count("black") == 4):
	al_top(nombre,segundos,form.getfirst("orden_real"),dificultad)
	print('''<body><script type="text/javascript">window.location="gano.py?nombre='''+form.getfirst("nombre")+'''&tipo_partida='''+form.getfirst("tipo_partida")+'''";</script></body>''')
print ('''<tr>
			<td>
				<div class="c container2" style="background:'''+r[0]+''';" ></div>
			</td>
			<td>
				<div class="c container2" style="background:'''+r[1]+''';" ></div>
			</td>
		 </tr>
		    <tr>
		    <td>
				<div class="c container2" style="background:'''+r[2]+''';" ></div>
		    </td>
		    <td>
				<div class="c container2" style="background:'''+r[3]+''';" ></div>
	    	</td>
		</tr>''')
print('''</tr></table></td></tr></table></td>''')
