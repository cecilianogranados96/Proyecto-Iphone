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
	ruta = datos[3]
else:
	imagen = "profile.png"
	ruta = ""
print('''
	<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="css/main.css">
		<script type="text/javascript" src="../proyecto/js/jquery-2.0.2.min.js"></script>
	</head>
	<div class="demo" style= "width: 320px;height: 550px;">
	<form action="procesar_actualizar.py?num='''+id+'''" id="form-id" enctype="multipart/form-data"  method="post"  >
		<div class="app">
			<div class="top-bar">
				<h1 class="top-bar-title">Editar contacto</h1>
				<a href="contacto.py" class="top-bar-link left">Cancelar</a>
				<a  onclick="document.getElementById('form-id').submit();"  class="top-bar-link right">Ok</a>
			</div>
			<div class="content">
				<table style="margin-top: 12px;    margin-bottom: -37px;" class='table' >
					<tr>
						<td>''')

print('''<img src="datos/imagenes/'''+imagen+'''" class="img2">
				<input type="file" value="'''+ruta+'''" name="imagen" id="file-5" style="display:none;"/>
				<label for="file-5"><span class="color linea " style="top: 28px;position: absolute;left: 28px;    font-size: 13px;"> cambiar</span></label>
			</img>
''')
					
				
						
print('''</td>
						<td>
							<input class="input1"  type="text" name="nombre" class="form-text-input" placeholder="Nombre" value="'''+datos[1]+'''" requerid>
							<input class="input1"  type="text" name="apellido" class="form-text-input"  value="'''+datos[2]+'''" placeholder="Apellido" >
						</td>
					</tr>
				</table>	
				<br>
				
				
''')

import operator
adicionales_orden = sorted(adicionales.items(), key=operator.itemgetter(0))
j = 3
while j <= (len(obligatorios)-1):
	if (datos[j] == "None" or datos[j] == ""):
		valor = ""
	else:
		valor  = datos[j]
	if (obligatorios[j] != "tono" and obligatorios[j] != "imagen" ):
		print('''
		<table style="margin-left:20px;margin-top: 35px;margin-right: 11px;">
				
				<tr>
				<td>
				<table>
				<tr>
				<td class="linea2"> 
				
				<img src="css/more.png"   onclick="eliminar('num')"  style="width: 23px;">	
				<p class="color" style="margin-left:26;position: relative;margin-top: -21px;    margin-right: 11px;"> 
					'''+obligatorios[j]+'''
				</p> 
				
				</td>
				</tr>
				</table>
				</td>
				<td> 
				<input type="text"  class="input2" name="'''+obligatorios[j]+'''" class="'''+obligatorios[j]+'''" id="'''+obligatorios[j]+'''" value="'''+valor+'''"  placeholder=" '''+obligatorios[j]+'''"  /> 
				</td></tr>
				</table>
		</td>
				</tr>
	</table>
		''');
	j += 1
#############################################################################
	
print('''
	<table style="margin-left:20px;margin-top: 35px;margin-right: 11px;">
				<tr>
				<td>
				<table>
				<tr>
				<td class="linea2"> 
				
				<img src="css/more.png"   onclick="eliminar('num')"  style="width: 23px;">	
				<p class="color" style="margin-left:26;position: relative;margin-top: -21px;    margin-right: 11px;"> 
					Movil
				</p> 
				
				</td>
				</tr>
				</table>
				</td>
				<td> 
				<input type="text" type="number"  onkeypress="return isNumeric(event)" oninput="maxLengthCheck(this)" max="8" maxlength = "8"  class="input2" name="movil" class="movil" id="" value="'''+datos[0]+'''"  placeholder=" movil"  /> 
				</td></tr>
				</table>
		</td>
				</tr>
	</table>
''');
if (datos[7] != "None" and datos[7] != ""):
	tono = datos[7]
	print('''
	<br>
	<tr class="th">
		<td colspan="2">
	
			<p class="negro">
				<audio src="datos/tonos/'''+datos[7]+'''" controls></audio>
			</p><br>
		</td>
	</tr>
''');
else:
	tono = "None"

print('''
	<br>
	<input type="file" value="'''+tono+'''" name="tono" id="file-4" style="display:none;" data-multiple-caption="{count} files selected" multiple />
		<label for="file-4"><img src="css/more.png"  style="width: 23px; margin-left:20px;"><span class="color linea "> Nuevo Tono</span></label>
						
''')
j=0		
telefonos = datos[8]
telefonos = telefonos.split("~")
while j <= (len(telefonos)-2):
	if (telefonos[j] == "None" or telefonos[j] ==""):
		valor = ""
	else:
		valor = telefonos[j]
	print('''
			
			<table style="margin-left:20px;margin-top: 35px;margin-right: 11px;">
				
				<tr>
				<td>
				<table>
				<tr>
				<td class="linea2"> 
				
				<img src="css/more.png"   onclick="eliminar('num')"  style="width: 23px;">	
				<p class="color" style="margin-left:26;position: relative;margin-top: -21px;    margin-right: 11px;"> 
					'''+tupla[j]+'''
				</p> 
				
				</td>
				</tr>
				</table>
				</td>
				<td> 
				<input type="number"  onkeypress="return isNumeric(event)" oninput="maxLengthCheck(this)" max="8" maxlength = "8"  class="input2" name="'''+tupla[j]+'''" class="'''+tupla[j]+'''" id="'''+tupla[j]+'''" value="'''+valor+'''"  placeholder="'''+tupla[j]+'''"  /> 
				</td></tr>
				</table>
		</td>
				</tr>
	</table>
	
	
	
''');
	j += 1

	
j=4
import operator
adicionales_orden = sorted(adicionales.items(), key=operator.itemgetter(0))

j=0		
email = datos[9]
email = email.split("~")
while j <= (len(email)-2):
	if (email[j] == "None" or email[j] == ""):
		valor = ""
	else:
		valor = email[j]
	print('''
			<table style="margin-left:20px;margin-top: 35px;margin-right: 11px;">
				
				<tr>
				<td>
				<table>
				<tr>
				<td class="linea2"> 
				
				<img src="css/more.png"     style="width: 23px;">	
				<p class="color" style="margin-left:26;position: relative;margin-top: -21px;    margin-right: 11px;"> 
					'''+tupla2[j]+'''
				</p> 
				
				</td>
				</tr>
				</table>
				</td>
				<td> 
				<input type="text"  class="input2" name="'''+tupla2[j]+'''" class="'''+tupla2[j]+'''" id="'''+tupla2[j]+'''" value="'''+valor+'''"  placeholder="'''+tupla2[j]+'''"  /> 
				</td></tr>
				</table>
		</td>
				</tr>
	</table> 
	
	''');
	j += 1	
import operator
adicionales_orden = sorted(adicionales.items(), key=operator.itemgetter(0))
j=0		
adicion = datos[10]
adicion = adicion.split("~")
while j <= (len(adicionales_orden)-1):
	if adicionales_orden[j][0] != "date":
		tipo = "text"
	else:
		tipo = "date"
	if adicion[j] == "None" or adicion[j] == "":
		valor = ""
	else: 
		valor = adicion[j]
	if (adicionales_orden[j][0] != ""):
		print('''
		
		<table style="margin-left:20px;margin-top: 35px;margin-right: 11px;">
				
				<tr>
				<td>
				<table>
				<tr>
				<td class="linea2"> 
				
				<img src="css/more.png"   onclick="eliminar('num')"  style="width: 23px;">	
				<p class="color" style="margin-left:26;position: relative;margin-top: -21px;    margin-right: 11px;"> 
					'''+adicionales_orden[j][0]+'''
				</p> 
				
				</td>
				</tr>
				</table>
				</td>
				<td> 
				<input type="'''+tipo+'''"  class="input2" name="'''+adicionales_orden[j][0]+'''" class="'''+adicionales_orden[j][0]+'''" id="'''+adicionales_orden[j][0]+'''" value="'''+valor+'''"  placeholder="'''+adicionales_orden[j][0]+'''"  /> 
				</td></tr>
				</table>
		</td>
				</tr>
	</table> 
	''');
	j += 1

	

							
print ('''
	
				<br>
	<table style="width: 100%; margin-left:12px;  margin-top: 0px;" class='table'>
				<tr class="th">
									<td colspan="2">
		<a href="eliminar.py?num='''+id+'''" onclick="return confirmar()" class="sep" style="color: red;">
	<img src="css/less.png"  style="width: 23px;">
	
	Eliminar Contacto</a></td>
								</tr>
			
				</div>
		</table>
		<script>
	function maxLengthCheck(object) {
    if (object.value.length > object.maxLength)
      object.value = object.value.slice(0, object.maxLength)
  }
    
  function isNumeric (evt) {
    var theEvent = evt || window.event;
    var key = theEvent.keyCode || theEvent.which;
    key = String.fromCharCode (key);
    var regex = /[0-9]|\./;
    if ( !regex.test(key) ) {
      theEvent.returnValue = false;
      if(theEvent.preventDefault) theEvent.preventDefault();
    }
  }
		</script>
				<script>
function confirmar()
{
	if(confirm('Seguro de eliminar el contacto?'))
		return true;
	else
		return false;
}
</script>
						</form>				
							</div>
						</div>
						</div>
					</body>
					</html>
''');