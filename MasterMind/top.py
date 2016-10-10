#!../python35/python.exe
# -*- coding: utf-8 -*-
print ("Content-type: text/html\n")
from funciones import * 
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
modo = form.getfirst("modo")

config = configuraciones()
dificuldad = int(config[1]); 
pocision = int(config[2]); 
elementos =  int(config[3]); 
reloj =  int(config[4]); 
tiempo_jugada = int(config[5])
tiempo_juego = int(config[6])
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
			<a style="float:left;" href="previo_top.py" class="btn btn-lg btn-danger">Regresar</a>
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
				<center><p style="color:#FFFFFF">Numero</center>
			</td>
			<td>
				<center><p style="color:#FFFFFF">Nombre</center>
			</td>
			<td>
				<center><p style="color:#FFFFFF">Tiempo</center>
			</td>
			<td>
				<center><p style="color:#FFFFFF">Detalle</center>
			</td>
		</tr>''')
top(int(modo))	
print('''</table>
		</body>
	</html>		''')