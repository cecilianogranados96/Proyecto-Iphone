#!../python35/python.exe
print ("Content-type: text/html\n")
print('''
	<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="css/main.css">
		<script type="text/javascript" src="../proyecto/js/jquery-2.0.2.min.js"></script>
	</head>
	<div class="demo" style= "width: 320px;height: 550px;">
	<form action="procesar_nuevo.py" id="form-id" enctype="multipart/form-data"  method="post"  >
		<div class="app">
			<div class="top-bar">
				<h1 class="top-bar-title">Nuevo Contacto</h1>
				<a href="contacto.py" class="top-bar-link left">Cancelar</a>
				<a  onclick="document.getElementById('form-id').submit();"  class="top-bar-link right">Ok</a>
			</div>
			<div class="content">
				<table style="margin-top: 12px;    margin-bottom: -37px;" class='table' >
					<tr>
						<td>
						<div class="img2">
						<input type="file" name="imagen" id="file-5" style="display:none;"/>
						<label for="file-5"><span class="color linea " style="top: 28px;position: absolute;left: 28px;"> Foto</span></label>
						<div>
						</td>
						<td>
			
  
							<input class="input1"  type="text" name="nombre" class="form-text-input" placeholder="Nombre" requerid>
							<input class="input1"  type="text" name="apellido" class="form-text-input" placeholder="Apellido" >
						</td>
					</tr>
				</table>	
				<br>
				
				
				
				<table class="'+iCnt2+'"  style="margin-left:20px;margin-top: 35px; margin-right: 11px;" id="'+iCnt2+'">
				<tr><td><table><tr><td class="linea2"> 
				<img src="css/less.png"   onclick="eliminar('num')"  style="width: 23px;">	
				<p class="color" style="margin-left:26;position: relative;margin-top: -21px;    margin-right: 11px;"> 
				Movil </p> </td></tr>
				</table></td><td> 
					
					
					

				<input type="number"  onkeypress="return isNumeric(event)" oninput="maxLengthCheck(this)" max="8" maxlength = "8" class="input2"  id=movil" name="movil" class="num"   placeholder=" movil" required  /> 
				</td></tr>
				</table>
				
				<br>
				
				<div id="container_tel" style="margin-top: -42px;"></div>
				
				<div class="color sepa linea"> 
					<img src="css/more.png" onclick="add_tel()" style="width: 23px;"> <text onclick="add_tel()" >agregar telefono<text>
					</div>
					
					<div id="container_email"></div>
					
					<div class="color sepa linea"> 
						<img src="css/more.png" onclick="add_email()"  style="width: 23px;"> <text onclick="add_email()" >agregar Correo<text>
						</div>	
						
						<script>
							var iCnt = 0;
							''')
from vectores import * 

vec = list(tupla)
print("vec = " + str(vec) )						
print('''					var vec_cont = 0;
							function add_tel() {
								if (iCnt <= (vec.length - 1) ) {
									$(container_tel).append('<table class="'+iCnt+'"  style="margin-left:20px;margin-top: 35px;    margin-right: 11px;" id="'+iCnt+'"><tr><td><table><tr><td class="linea2"> <img src="css/less.png"   onclick="eliminar('+ iCnt +')"  style="width: 23px;">	<p class="color" style="margin-left:26;position: relative;margin-top: -21px;    margin-right: 11px;"> ' + vec[iCnt] + ' </p> </td></tr></table></td><td> <input type="number" onkeypress="return isNumeric(event)" oninput="maxLengthCheck(this)" max="8" maxlength = "8" class="input2" name="' + vec[vec_cont] + '" class="' + iCnt + '" id="' + vec[iCnt] + '"  placeholder=" '+ vec[iCnt] + '"  /> </td></tr></table>');
									iCnt = iCnt + 1;
									
									vec_cont = vec_cont + 1;
								}
							}
							var iCnt2 = 10;
							var vec_cont2 = 0;
							''')
 			
vec2 = list(tupla2)
print("vec2 = " + str(vec2) )
									
print('''
							function add_email() {
								if (vec_cont2 <= (vec2.length - 1) ) {
								
									$(container_email).append('<table class="'+iCnt2+'"  style="margin-left:20px;margin-top: 35px;    margin-right: 11px;" id="'+iCnt2+'"><tr><td><table><tr><td class="linea2"> <img src="css/less.png"   onclick="eliminar('+ iCnt2 +')"  style="width: 23px;">	<p class="color" style="margin-left:26;position: relative;margin-top: -21px;    margin-right: 11px;"> ' + vec2[vec_cont2] + ' </p> </td></tr></table></td><td> <input type="email" onchange="validarEmail(this.value)" class="input2" name="' + vec2[vec_cont2] + '" class="' + iCnt2 + '" id="' + vec2[vec_cont2] + '"  placeholder=" '+ vec2[vec_cont2] + '"  /> </td></tr></table>');
									iCnt2 = iCnt2 + 1;
									vec_cont2 = vec_cont2 + 1;
								}
							}
							
function validarEmail(valor) {
var expresion = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
if (!expresion.test(valor)){
	alert("Direccion de Email Invalida - Revisa")
}else{
	console.log("bien")
}
}
							
							function eliminar(iCnt) {
								$('#' + iCnt).remove();
							}
							
							
						
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
						
						<br>	
			
						<input type="file" name="tono" id="file-4" style="display:none;" data-multiple-caption="{count} files selected" multiple />
						<label for="file-4"><img src="css/more.png"  style="width: 23px; margin-left:20px;"><span class="color linea "> Tono</span></label>
						
						
						<br>
						<img src="css/more.png"  style="width: 23px; margin-left:20px;margin-top: 13px;"><input type="text" name="direccion" class="input3" placeholder="Direccion Casa">
						
						<br>
						<img src="css/more.png"  style="width: 23px; margin-left:20px;margin-top: 13px;"><input type="text" name="l_trabajo" class="input3" placeholder="Lugar Trabajo">
						<br>
						<img src="css/more.png"  style="width: 23px; margin-left:20px;margin-top: 13px;"><input type="text" name="l_estudio" class="input3" placeholder="Lugar Estudio">
						
						
						
						<br>
						<div class="color sepa linea"> 
							<img src="css/more.png" onclick="adicionales()" style="width: 23px;"> <text onclick="adicionales()" >mas opciones<text>
							</div>	
							<div style="display:none;" id="mas_opciones">
			''')


for clave in adicionales:
	if (adicionales[clave] == "date" and clave != ""):
		print('''
		<img src="css/more.png"  style="width: 23px; margin-left:20px;margin-top: 13px; position:absolute"><p class="color" style="position: absolute;margin-left: 48px;margin-top: 13px;">'''+clave+'''</p> <br>
		<br>
		<center>
			<input type="date" class="color" name="'''+clave+'''" class="input3" placeholder="'''+clave+'''">
		</center>
		''')						
for clave in adicionales:
	if (adicionales[clave] == "input" and clave != "" ):
		print('''<br><img src="css/more.png"  style="width: 23px; margin-left:20px;margin-top: 13px;"><input type="text" name="'''+clave+'''" class="input3" placeholder="'''+clave+'''"><br>''')
								
								
								
							
print ('''
				</div>
							<script>
								function adicionales(){
									$("#mas_opciones").slideToggle("normal",function(){
										$("#mas_opciones").fadeIn();
									});
								};
							</script>	
						</form>				
							</div>
						</div>
						</div>
					</body>
					</html>
''');