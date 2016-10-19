#!../python35/python.exe
print ("Content-type: text/html\n")
from funciones import * 
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

borrar_datos_ateriores = open('datos/actual.dat', 'w')
config = configuraciones()
random(1)


if int(config[4]) == 4:
	juego_multi()
	print('''
	<script>
		alert("Ganaste el nivel continua avanzando");
		window.location="juego.py?nombre='''+form.getfirst("nombre")+'''&tipo_partida='''+form.getfirst("tipo_partida")+'''";
	</script>''')

	
print('''<html>
	<head>
		<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>		
		<script type="text/javascript" src="http://code.jquery.com/ui/1.8.18/jquery-ui.min.js"></script>
		<link type="text/css" rel="stylesheet" href="juego.css">
		<link type="text/css" rel="stylesheet" href="atomo.css">
		<link type="text/css" rel="stylesheet" href="http://getbootstrap.com/dist/css/bootstrap.min.css">
	</head>
		
	<div style="border-style:solid; width: 320px;height: 568px; position: absolute; background-color:'''+config[8]+''' ">
	<div class="atom">
    <div class="orbital">
        <div class="ruta uno">
            <div class="electron"></div>
        </div>
    </div>
    <div class="orbital e2">
        <div class="ruta uno">
            <div class="electron"></div>
        </div>
    </div>
    <div class="orbital e3">
        <div class="ruta uno">
            <div class="electron"></div>
        </div>
    </div>

</div>
	<table style='width: 100%;' >
	<tr>
		<td>
			<a style="float:left;" href="index.html" class="btn btn-lg btn-danger">Regresar</a>
		</td>
		<td>
			<img src="../css/master_logo.png" style="width: 47px;">
			</td>
		<td>
			<a style="float:right;" href="previo_juego.py" class="btn btn-lg btn-primary">Jugar</a>
		</td>
	</tr>
	</table>
	
	<h1><center><p style="color:#FFFFFF">Felicidades!</p></center></h1>
			<img src="../css/gano.gif" style="position: absolute;    width: 311px;margin-top: 109px;margin-left: -8px;">
		</body>
	</html>	
''')