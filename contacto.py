#!../python35/python.exe
# -*- coding: utf-8 -*-
print ("Content-type: text/html\n")
from funciones import * 
print('''
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
  <link rel="stylesheet" href="css/main.css">
  <script type="text/javascript" src="js/jquery-2.0.2.min.js"></script>
</head>
<div class="demo" style= "width: 320px;height: 550px;">
  <div class="app">
    <div class="top-bar">
	  <a href="acerca.py" class="top-bar-link left icon-only icon-menu">Menu</a>
      <h1 class="top-bar-title">Contactos</h1>
      <a href="nuevo.py" class="top-bar-link right icon-only icon-plus">New</a>
    </div>

    <div class="content">
	
		<div class="buscar">
	  <form class="search-bar">
        <input type="search" class="search-bar-input" id="search" placeholder="Buscar">
      </form>
	  </div >

		
		<table style="margin: 12px;">
		<tr>
		<td>
		<img src="../proyecto/css/profile.png" class="img">
		</td>
		<td style="position: absolute;margin-left:20px;margin-top: 6px;">
		<b style="font-weight: bold;">Jose Andres Ceciliano...</b>
		<br>
		<p>Mi tarjeta<p>
		</td>
		</tr>
		</table>
		<ul class="list list-contacts" id="myMenu">
''')
	  
contactos()
	

print('''  
	  </ul>
    </div>
  </div>

</div>

</body>

<script type='text/javascript'>
$(function() {
	$.expr[':'].Contains = function(x, y, z){
			return jQuery(x).text().toLowerCase().indexOf(z[3].toLowerCase())>=0;
	};
    $( '#search' ).keyup( function() {
        var matches = $( 'ul#myMenu' ).find( ':Contains('+ $( this ).val() +') ' );
        $( 'li', 'ul#myMenu' ).not( matches ).slideUp();
        matches.slideDown();    
    });
}); 
</script>
	
</html>

''');
