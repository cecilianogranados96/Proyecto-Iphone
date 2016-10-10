#!../python35/python.exe
print ("Content-type: text/html\n")
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
      <a  href="../index.py"  target="_parent" class="top-bar-link right">Salir</a>
    </div>
    <nav class="top-bar-sub tabs tabs-three">
      <a href="manual.py" class="tabs-link">Ayuda</a>
		  <a href="config.py" class="tabs-link">Configuracion</a>
      <a href="acerca.py" class="tabs-link active">Acerca de</a>
     
    </nav>
    <div class="content">
      <center>
	<img src="../css/logo.jpg" width="198px"><br><br>
	
			<h1>Proyecto # 1 de Taller de programacion</h1>
			<p>
					Jose Andres Ceciliano Granados<br>
					2016087245<br>
				<br><br>
				<b>Descripcion:</b> Simulacion de un telefono celular, en el area de agenda telefonica
				utilizando python como lenguaje manejador de datos y una interfaz web como recurso principal.
				
			</p><br><br>
			<p>Desliza el recuadro y desbloquea el iphone, luego la funcion principal es la agenda de contacto</p>
		</div>
	</div>
	</div>
</div>

</body>
</html>
''');