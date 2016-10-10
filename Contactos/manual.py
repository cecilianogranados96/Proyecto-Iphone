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
      <a href="../index.py"  target="_parent" class="top-bar-link right">Salir</a>
    </div>
    <nav class="top-bar-sub tabs tabs-three">
      <a href="ayuda.py" class="tabs-link active">Ayuda</a>
		<a href="config.py" class="tabs-link">Configuracion</a>
      <a href="acerca.py" class="tabs-link">Acerca de</a>

    </nav>
    <div class="content" style="overflow-y: hidden;">
      
					<iframe src="manual.pdf" scrolling="no" style='width: 100%;
    height: 100%;' ></iframe>
			</div>
</div>

</body>
</html>
''');
