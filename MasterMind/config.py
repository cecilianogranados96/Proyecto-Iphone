#!../python35/python.exe
print ("Content-type: text/html\n")
from funciones import * 
config = configuraciones()
dificuldad = int(config[1]); 
pocision = int(config[2]); 
elementos =  int(config[3]); 
reloj =  int(config[4]); 
tiempo_jugada = int(config[5])
tiempo_juego = int(config[6])
tiempo_multinivel = int(config[7])

print('''
	<html>
	<head>
		<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>		
		<script type="text/javascript" src="http://code.jquery.com/ui/1.8.18/jquery-ui.min.js"></script>
		<link type="text/css" rel="stylesheet" href="juego.css">
		<link type="text/css" rel="stylesheet" href="atomo.css">
		<link type="text/css" rel="stylesheet" href="http://getbootstrap.com/dist/css/bootstrap.min.css">
	</head>
	<div style="border-style:solid; width: 320px;height: 568px; position: absolute; background-color:'''+config[8]+'''; overflow-x: hidden;">	
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
	

<form class="form-horizontal" method="POST" action="process_config.py" style="margin-left:15px; margin-top:35px;">
<center style="font-size:30px;color:#FFF;">Configuracion</center>
<hr><center>
  <label class="control-label" for="nombre"><center>Nombre</label>  

	<input id="nombre" name="nombre" type="text" placeholder="Nombre" value="''' + config[0] + '''" class="form-control input-md" required=""> 

<hr>

<label class="control-label" for="dificuldad"><center>Dificultad</label><br>
	  
    <label class="radio-inline" for="dificuldad-0">
      <input type="radio" name="dificuldad" id="dificuldad-0" value="1" '''+ str(seleccionado(1,dificuldad)) +'''>
      Facil (8 jugadas)
    </label> <br>
    <label class="radio-inline" for="dificuldad-1">
      <input type="radio" name="dificuldad" id="dificuldad-1" value="2" '''+ str(seleccionado(2,dificuldad)) +'''>
      Medio (7 jugadas)
    </label> <br>
    <label class="radio-inline" for="dificuldad-2">
      <input type="radio" name="dificuldad" id="dificuldad-2" value="3" ''' + str(seleccionado(3,dificuldad)) +'''>
      Dificil (6 jugadas)
    </label>

	
<hr>

  <label class="control-label" for="pocision"><center>Posicion </label>
<br><br>
    <label class="radio-inline" for="pocision-0">
      <input type="radio" name="pocision" id="pocision-0" value="1" '''+ str(seleccionado(1,pocision)) +'''>
      Izquierda
    </label> <br>
    <label class="radio-inline" for="pocision-1">
      <input type="radio" name="pocision" id="pocision-1" value="2" '''+ str(seleccionado(2,pocision)) +''' >
      Derecha
    </label><br>

<hr>

  <label class="control-label" for="elementos">Elementos</label>
<br>
    <label class="radio-inline" for="elementos-0">
      <input type="radio" name="elementos" value="1" '''+ str(seleccionado(1,elementos)) +'''>
      Colores
    </label> <br>
    <label class="radio-inline" for="elementos-1">
      <input type="radio" name="elementos" value="2" '''+ str(seleccionado(2,elementos)) +'''>
      Numeros
    </label> <br>
    <label class="radio-inline" for="elementos-2">
      <input type="radio" name="elementos"  value="3" '''+ str(seleccionado(3,elementos)) +'''>
      Letras
    </label> <br>
    <label class="radio-inline" for="elementos-3">
      <input type="radio" name="elementos"  value="4" '''+ str(seleccionado(4,elementos)) +'''>
      Caracteres
    </label>

	<hr>

  <label class="control-label" for="reloj"><center>Reloj</label>
<br>
    <label class="radio-inline" for="reloj-0">
      <input type="radio" name="reloj" value="1" '''+ str(seleccionado(1,reloj)) +'''>
      Cronometro por jugada <br>
		<p style="float: left;margin-top: 7px;">Tiempo en Segundos: </p>
		<input name="tiempo_jugada" type="text" class="form-control input-md" style="width: 60px;float: right;" value="'''+str(tiempo_jugada)+'''"> 
    </label> 
	<br>
    <label class="radio-inline" for="reloj-1">
      <input type="radio" name="reloj"  value="2" '''+ str(seleccionado(2,reloj)) +'''>
      Cronometro por juego<br>
	  		<p style="float: left;margin-top: 7px;">Tiempo en Segundos: </p>
		<input name="tiempo_juego" type="text" class="form-control input-md" style="width: 60px;float: right;" value="'''+str(tiempo_juego)+'''">  
    </label> 
	<br>
    <label class="radio-inline" for="reloj-1">
      <input type="radio" name="reloj"  value="4" '''+ str(seleccionado(4,reloj)) +'''>
      Cronometro Juego Multinivel<br>
	  		<p style="float: left;margin-top: 7px;">Tiempo en Segundos: </p>
		<input name="tiempo_multinivel" type="text" class="form-control input-md" style="width: 60px;float: right;" value="'''+str(tiempo_multinivel)+'''">  
    </label> 
	<br>
    <label class="radio-inline" for="reloj-2">
      <input type="radio" name="reloj" value="3" '''+ str(seleccionado(3,reloj)) +'''>
      No
    </label>

<br><hr><br>	
	
	


  <label class="control-label" for="reloj"><center>Color de Fondo</label>
<br><br>
 <input type="color" name="fcolor" value="'''+config[8]+'''" style="width: 160px;">
 

<br><hr><br>	
 <center><input type="submit" class="btn btn-lg btn-primary"  value="Guardar"></center>
</fieldset>
</form>
	<br><br><br><br><br><center>
	<a class="btn btn-lg btn-warning" href="reestablecer.py">Restablecer Configuracion</a>

			
		</body>
	</html>		''')