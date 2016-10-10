#!../python35/python.exe
# -*- coding: utf-8 -*-
print ("Content-type: text/html\n")
from funciones import * 
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
id = form.getfirst("id")
datos = top_detalle(id)
modo = datos[6].replace("<br>", "")
jugadas = datos[7].split("/")
real = datos[2]+"|"+datos[3]+"|"+datos[4]+"|"+datos[5]
print('''
	<html>
	<head>
		<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>		
		<script type="text/javascript" src="http://code.jquery.com/ui/1.8.18/jquery-ui.min.js"></script>
		<link type="text/css" rel="stylesheet" href="juego.css">
		<link type="text/css" rel="stylesheet" href="atomo.css">
		<link type="text/css" rel="stylesheet" href="http://getbootstrap.com/dist/css/bootstrap.min.css">
	</head>
	<div style="border-style:solid; width: 320px;height: 568px; position: absolute; background-color:#8fccaf; overflow-x: hidden;">
		<table style='width: 100%;'  >
	<tr>
		<td>
			<a style="float:left;" href="top.py?modo='''+form.getfirst("modo")+'''" class="btn btn-lg btn-danger">Regresar</a>
		</td>
		<td>
			<img src="../css/master_logo.png" style="width: 47px;">
		</td>
		<td>
			<a style="float:right;" href="previo_juego.py" class="btn btn-lg btn-primary">Jugar</a>
		</td>
	</tr>
	</table>
	<br>
<center style="font-size:30px;color:#FFF;">Top 10</center>

	<br>	<table  style="width: 100%;height:70%;" class="table table-bordered" >
		<tr>
			<td>
				<br><br>
				<center><p style="color:#FFFFFF">Nombre:<br>'''+datos[0]+'''</center>
<br><br>
				<center><p style="color:#FFFFFF">Tiempo:<br>'''+datos[1]+''' segundos</center>
<br><br>
				<center><p style="color:#FFFFFF">Modalidad:<br>'''+modo+'''</center>
			</td>
			<td>
			 <h3><center>Real<br>'''+str(real)+'''</h3></center>
				<table  style="width: 100%;height:70%;" class="table table-bordered" >
				<tr>
					<td>
					#
					</td>
					<td>
					Jugada
					</td>
				</tr>''')
x = 0; 
while x < len(jugadas) -1:
	print('''	<tr>
					<td>
					'''+str((x+1))+'''
					</td>
					<td>
					'''+jugadas[x]+'''
					</td>
				</tr>''')
	x += 1 
print('''		
				
				</table>
			
			
			</td>
		</tr>''')

print('''</table>
		</body>
	</html>		''')