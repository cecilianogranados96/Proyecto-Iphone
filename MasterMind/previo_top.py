#!../python35/python.exe
# -*- coding: utf-8 -*-
print ("Content-type: text/html\n")
from funciones import * 

print('''<html>
	<head>
		<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>		
		<script type="text/javascript" src="http://code.jquery.com/ui/1.8.18/jquery-ui.min.js"></script>
		<link type="text/css" rel="stylesheet" href="juego.css">
		<link type="text/css" rel="stylesheet" href="atomo.css">
		<link type="text/css" rel="stylesheet" href="http://getbootstrap.com/dist/css/bootstrap.min.css">
	</head>
	
				
	<div style="border-style:solid; width: 320px;height: 568px; position: absolute; background-color:#8fccaf; ">
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
		<table style='width: 100%;'  >
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
	<br>
		<center style="font-size:30px;color:#FFF;">Ver Top 10</center><hr>
		<table   style="margin-top:20px;    border-top: 0px solid #0000;z-index: 1;position: absolute; width: 100%;height: 67%;" >
			<tr>
				<td style="font-size:30px;">
					<center><a href="top.py?modo=0" class="btn btn-lg btn-success">Modo Facil</a>
				</td>
			</tr>
			<tr>
				<td style="font-size:30px;">
					<center><a href="top.py?modo=1" class="btn btn-lg btn-warning">Modo Medio</a>
				</td>
			</tr>
			<tr>
				<td style="font-size:30px;">
					<center><a href="top.py?modo=2" class="btn btn-lg btn-danger">Modo Dificil</a>
				</td>
			</tr>
			</table>
		</body>
	</html>	''')	