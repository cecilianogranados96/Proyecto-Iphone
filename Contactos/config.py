#!../python35/python.exe
print ("Content-type: text/html\n")
from vectores import * 
print('''
<html>
<head>
	<link rel="stylesheet" href="../css/main.css">
</head>
<body>
<div class="demo" style= "width: 320px;height: 568px;">
  <div class="app">
    <div class="top-bar">
      <h1 class="top-bar-title">Ayuda</h1>
      <a href="contacto.py" class="top-bar-link left icon-back">Atras</a>
      <a href="../index.py"  target="_parent" class="top-bar-link right">Salir</a>
    </div>
    <nav class="top-bar-sub tabs tabs-three">
      <a href="manual.py" class="tabs-link">Ayuda</a>
		<a href="config.py" class="tabs-link active">Configuracion</a>
      <a href="acerca.py" class="tabs-link">Acerca de</a>

    </nav>
    <div class="content">

	<a href="nuevo_adi.py" >
	<img src="../css/more.png"  style="width: 23px; margin-left:96px;margin-top: 13px; position:absolute">
	<p class="color" style="position: absolute;margin-left: 125px;margin-top: 13px;">Nuevo Campo</p> 
	</a>
	<hr style="    margin-top: 45px;">
	
	
      <table style="margin-top: 12px; margin-left:20px; margin-bottom: -37px;width: 95%;height:80%; " class='table' >
		<tr>
		<td>
		<b>Campo
		<td>
		<td>
		<b>Accion
		<td>
		</tr>
''')

import operator
adicionales_orden = sorted(adicionales.items(), key=operator.itemgetter(0))
j=0		
while j <= (len(adicionales_orden)-1):
	if (adicionales_orden[j][0] != ""):
		print('''<tr>
		<td>
		<p class="color">'''+adicionales_orden[j][0].capitalize()+'''<p>
		<td>
		<td>
		<a href="eliminar_adi.py?dato='''+adicionales_orden[j][0]+'''" class="sep" style="color: red;" >Eliminar<a>
		<td>
		</tr>''')
	j += 1	
print('''</table>
	  
	</div>
</div>

</body>
</html>
''');
