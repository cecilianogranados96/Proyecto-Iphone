#!../python35/python.exe
print ("Content-type: text/html\n")
from funciones import * 
from vectores import * 
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
id = form.getfirst("num")
datos = leer(int(id))
if datos[3] != "None":
	imagen = datos[3]
else:
	imagen = "profile.png"
print('''
<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="css/main.css">
	</head>
	<body>
		<div class="demo" style= "width: 320px;height: 550px;">
			<div class="app">
				<div class="top-bar">
					<a href="contacto.py" class="top-bar-link left icon-back">Atras</a>
					<a href="editar.py?num='''+id+'''" class="top-bar-link right">Editar</a>
				</div>
		<div class="content2">
			<table style="width: 300px; margin-left:12px;  margin-top: 52px;" class='table2'>
			<br><br>
					<tr>
							<td>
								<img src="datos/imagenes/'''+imagen+'''" class="img">
							</td>
							<td style="position: absolute; margin-left: -208px;;margin-top: 8px;">
								<b style="font-weight: bold;">'''+datos[1]+''' '''+datos[2]+''' </b>
								<br>
								<p>'''+datos[0]+'''<p>
							</td>
					</tr>
			<tr class="th" >
			<td><br>	
				<p class="color">Movil</p>
				<p class="negro">'''+datos[0]+'''</p><br></td>
				<td>
					<img src="css/sms.png" class="sms"> <img src="css/call.png" class="call">
				</td>
			</tr>''');
j=0		
telefonos = datos[8]
telefonos = telefonos.split("~")
while j <= (len(telefonos)-2):
	if (telefonos[j] != "None" and telefonos[j] != ""):
		print('''<tr class="th" >
					<td>
						<p class="color">Tel: '''+tupla[j]+'''</p>
						<p class="negro">'''+telefonos[j]+'''</p><br>
					</td>
					<td>
						<img src="css/sms.png" class="sms"> <img src="css/call.png" class="call">
					</td>
				</tr>''');
	j += 1
j=4
import operator
adicionales_orden = sorted(adicionales.items(), key=operator.itemgetter(0))
if (datos[7] != "None" and datos[7] != ""):
	print('''
	<tr class="th">
		<td colspan="2">
			<p class="color">Tono</p><p class="negro">
			<audio src="datos/tonos/'''+datos[7]+'''" controls></audio></p><br>
		</td>
	</tr>

''');
while j <= (len(obligatorios)-1):
	if (datos[j] != "None" and datos[j] != "" and obligatorios[j] != "tono" and obligatorios[j] != "imagen" ):
		print('''
	<tr class="th">
		<td colspan="2">
			<p class="color">'''+obligatorios[j]+'''</p><p class="negro">'''+datos[j]+'''</p><br>
		</td>
	</tr>''');
	j += 1
j=0		
email = datos[9]
email = email.split("~")
while j <= (len(email)-2):
	if (email[j] != "None" and email[j] != "" ):
		print('''<tr class="th" >
					<td>
						<p class="color">'''+tupla2[j]+'''</p>
						<p class="negro">'''+email[j]+'''</p><br>
					</td>
				</tr>''');
	j += 1	
import operator
adicionales_orden = sorted(adicionales.items(), key=operator.itemgetter(0))
j=0		
adicion = datos[10]
adicion = adicion.split("~")
while j <= (len(adicionales_orden)-1):
	if (adicion[j] != "None"  and adicion[j] != "" and adicionales_orden[j][0] != ""):
		print('''
	<br><br>
	<tr class="th">
		<td colspan="2">
			<p class="color">'''+adicionales_orden[j][0]+'''</p><p class="negro">'''+adicion[j]+'''</p><br>
		</td>
	</tr>''');
	j += 1

print('''		
								<tr class="th">
									<td colspan="2"><p class="color sep">Enviar mensaje</p></td>
								</tr>
								<tr class="th">
									<td colspan="2"><p class="color sep">Compartir contacto</p></td>
								</tr>
								<tr class="th">
									<td colspan="2"><p class="color sep">Agregar a favoritos</a>
								</p></td>
								</tr>
								
								<tr class="th">
									<td colspan="2">
										<a href="eliminar.py?num='''+id+'''" onclick="return confirmar()" class="sep" style="color: red;">Eliminar Contacto</a>
									</td>
								</tr>
							</table>		
				</div>
			</div>			
		</div>
		<script>
function confirmar()
{
	if(confirm('Seguro de eliminar el contacto?'))
		return true;
	else
		return false;
}
</script>
	</body>
</html>
<br><br><br>
''');
