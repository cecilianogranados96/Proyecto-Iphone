#!../python35/python.exe
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
	
				
	<div style="width: 320px;height: 568px; position: absolute; background-color:'''+config[8]+'''; ">
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

<img src="../css/master_iso.png" style="width: 315px;margin-top:15px;">
		<table   style="margin-top:20px;    border-top: 0px solid #0000;z-index: 1;position: absolute; width: 100%;height: 67%;" >
			<tr>
				<td style="font-size:30px;">
					<center><a href="previo_juego.py" class="btn btn-lg btn-primary">Jugar</a>
				</td>
			</tr>
			<tr>
				<td style="font-size:30px;">
					<center><a href="previo_top.py" class="btn btn-lg btn-success">Top 10 </a>
				</td>
			</tr>
			<tr>
				<td style="font-size:30px;">
					<center><a href="config.py" class="btn btn-lg btn-warning">Configuracion</a>
				</td>
			</tr>
			<tr>
				<td style="font-size:30px;">
					<center><a href="acerca.py" class="btn btn-lg btn-info">Acerca de</a>
				</td>
			</tr>				
			<tr>
				<td style="font-size:30px;">
					<center><a href="manual.py" class="btn btn-lg btn-danger">Manual</a>
				</td>
			</tr>
			<tr>
				<td style="font-size:30px;">
					<center><a href="../index.py"  target="_parent" class="btn btn-lg btn-default">Salir</a>
				</td>
			</tr>
			</table>
		</body>
	</html>	''')