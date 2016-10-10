#!../python35/python.exe
# -*- coding: utf-8 -*-
print ("Content-type: text/html\n")
from funciones import * 
config = configuraciones()

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

	
		<table style='width: 100%;' >
	<tr>
		<td>
			<a style="float:left;" href="index.html" class="btn btn-lg btn-danger">Regresar</a>
		</td>
		<td>
			<img src="../css/master_logo.png" style="width: 47px;">
		</td>
		<td>
			<a style="float:right;" href="config.py" class="btn btn-lg btn-info">Configuracion</a>
		</td>
	</tr>
	</table>
	

<form class="form-horizontal" method="GET" action="juego.py" style="margin-left:15px; margin-top:35px;">
<center style="font-size:30px;color:#FFF;">Jugar</center>
<hr><center>
  <label class="control-label" for="nombre"><center>Nombre</label>  
	<input id="nombre" name="nombre" type="text" placeholder="Nombre" value="''' + config[0] + '''" class="form-control input-md" required=""> 

<hr>
 <center><input type="submit" class="btn btn-lg btn-primary"  value="Jugar"></center>
</fieldset>
</form>

<br>

Calificacion:<br><br>
<table class="table">
<tr>
	<td>
		<center>
		<div style="-webkit-border-radius: 200px 200px 200px 200px;border: 1px solid rgba(0, 0, 0, 0);width: 30px;height: 30px;background-color: #FFF;"></div> 
	</td>
	<td>
			Ficha en lista pero en pocision incorrecta
	</td>
</tr>	
<tr>
	<td><center>
	<div style="-webkit-border-radius: 200px 200px 200px 200px;border: 1px solid rgba(0, 0, 0, 0); width: 30px;height: 30px;background-color: #000;"></div> 
	</td>
	<td>
		Ficha en pocision correcta y en la lista
	</td>
</tr>
<tr>
	<td><center>
	<div style="-webkit-border-radius: 200px 200px 200px 200px;border: 1px solid rgb(0, 0, 0); width: 30px; height: 30px;"></div>
	</td>
	<td>
		Ficha no se encuentra en la lista
	</td>
</tr>	

</table>


		</body>
	</html>		''')