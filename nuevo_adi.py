#!../python35/python.exe
print ("Content-type: text/html\n")
from funciones import * 
from vectores import * 
try: 
	import cgi
	import cgitb; cgitb.enable()
	form = cgi.FieldStorage()
	campo = form.getfirst("campo")
	tipo = form.getfirst("tipo")
	in_ad(campo,tipo)
	print('''<body><script type="text/javascript">alert("Insertado con exito!")</script><script type="text/javascript">window.location="config.py";</script></body>''')
except:
	print('''
<html>
<head>
	<link rel="stylesheet" href="css/main.css">
	<style>

ul li{
  color: #AAAAAA;
  display: block;
  position: relative;
  float: left;
}
.btn {
  background: #2087fc;
  background-image: -webkit-linear-gradient(top, #2087fc, #2087fc);
  background-image: -moz-linear-gradient(top, #2087fc, #2087fc);
  background-image: -ms-linear-gradient(top, #2087fc, #2087fc);
  background-image: -o-linear-gradient(top, #2087fc, #2087fc);
  background-image: linear-gradient(to bottom, #2087fc, #2087fc);
  -webkit-border-radius: 28;
  -moz-border-radius: 28;
  border-radius: 28px;
  font-family: Arial;
  color: #ffffff;
  font-size: 13px;
  padding: 10px 20px 10px 20px;
  text-decoration: none;
}
ul li input[type=radio]{
  position: absolute;
  visibility: hidden;
}

ul li label{
  display: block;
  position: relative;

  padding: 25px 25px 25px 80px;
  margin: 10px auto;

  z-index: 9;
  cursor: pointer;
  -webkit-transition: all 0.25s linear;
}

ul li:hover label{
	color: #FFFFFF;
}

ul li .check{
  display: block;
  position: absolute;
  border: 5px solid #AAAAAA;
  border-radius: 100%;
  height: 25px;
  width: 25px;
  top: 30px;
  left: 20px;
	z-index: 5;
	transition: border .25s linear;
	-webkit-transition: border .25s linear;
}

ul li:hover .check {
  border: 5px solid #FFFFFF;
}

ul li .check::before {
  display: block;
  position: absolute;
	content: '';
  border-radius: 100%;
  height: 15px;
  width: 15px;
  top: 5px;
	left: 5px;
  margin: auto;
	transition: background 0.25s linear;
	-webkit-transition: background 0.25s linear;
}

input[type=radio]:checked ~ .check {
  border: 5px solid #0DFF92;
}

input[type=radio]:checked ~ .check::before{
  background: #0DFF92;
}

input[type=radio]:checked ~ label{
  color: #0DFF92;
}
</style>
</head>
<body>
<div class="demo" style= "width: 320px;height: 550px;">
  <div class="app">
    <div class="top-bar">
      <h1 class="top-bar-title">Ayuda</h1>
      <a href="contacto.py" class="top-bar-link left icon-back">Atras</a>
      <a href="index.py"  target="_parent" class="top-bar-link right">Salir</a>
    </div>
    <nav class="top-bar-sub tabs tabs-three">
      <a href="manual.py" class="tabs-link">Ayuda</a>
		<a href="config.py" class="tabs-link active">Configuracion</a>
      <a href="acerca.py" class="tabs-link">Acerca de</a>

    </nav>
    <div class="content">
	<center style="margin-top:15px;font-size: x-large;">Nuevo Campo</center>
	<form action="nuevo_adi.py" id="form-id" enctype="multipart/form-data"  method="post"  >
				<table style="margin-top: 12px;    margin-bottom: -37px;">
					<tr>
						<td>
							<center>
					
	
	<input class="input1" type="text" name="campo" class="form-text-input" placeholder="Nombre del campo" requerid>
			
          
      <div class="container">
	
	
<ul>
  <li>
    <input type="radio" id="f-option" name="tipo" value="input">
    <label for="f-option">Texto</label>
    <div class="check"></div>
  </li>
  
  <li>
    <input type="radio" id="s-option" name="tipo" value="date">
    <label for="s-option">Fecha</label>
    <div class="check"><div class="inside"></div></div>
  </li>
</ul>


<center><input type="submit" value="Guardar" class="btn">

						
						</td>
					</tr>
				</table>	
				<br>
				</form>	
	</div>
</div>

</body>
</html>
''');


