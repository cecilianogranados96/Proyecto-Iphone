#!../python35/python.exe
print ("Content-type: text/html\n")
print('''



	<html>
	<head>
		<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>		
		<script type="text/javascript" src="http://code.jquery.com/ui/1.8.18/jquery-ui.min.js"></script>
		<link type="text/css" rel="stylesheet" href="juego.css">
		<link type="text/css" rel="stylesheet" href="atomo.css">
		<link type="text/css" rel="stylesheet" href="http://getbootstrap.com/dist/css/bootstrap.min.css">
	</head>
	<body style="overflow:hidden;">
	<div style="overflow:hidden;border-style:solid; width: 320px;height: 568px; position: absolute; background-color:#8fccaf; overflow-x: hidden;">

	<table style='width: 100%;' >
	<tr>
		<td>
			<a style="float:left;" href="index.html" class="btn btn-lg btn-danger">Regresar</a>
		</td>
		<td>
			<img src="../css/master_logo.png" style="width: 47px;">
		</td>
		<td>
			<a style="float:right;" href="acerca.py" class="btn btn-lg btn-info">Acerca de</a>
		</td>
	</tr>
	</table>

		
		<iframe src="manual.pdf" scrolling="no" style='width: 100%;height: 92%;position: absolute;' ></iframe>
		
	</div>
		</body>
	</html>	
	
''');
