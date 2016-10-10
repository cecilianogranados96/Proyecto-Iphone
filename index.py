#!../python35/python.exe
print ("Content-type: text/html\n")
print('''
<html>
<head>
<link href="css/iphone5.css" rel="stylesheet" type="text/css"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<script>
			function cambiar_url(url) {
				document.getElementById('frame_contenido').src = url;
				iframe()
			}
		</script>

</head>
<body>
	<div id="main">
		<div id="iphone5">
			<div id="iphone-border">
				<div id="power-button"></div>
				<div id="voice-toogle"></div>
				<div id="voice-plus"></div>
				<div id="voice-minus"></div>
				<div id="home-button"></div>
				<div id="dynamic"></div>
				<div id="phone-camera"></div>
				<div id="iphone-panel">
					<div id="iphone-display">
						<div id="headline">
							<div id="net"></div>
							<span>TEC</span>
							<div id="wifi">
								<div class="dot"></div>
							</div>
							<div id="headline-time"></div>
							<div id="battery"></div>
						</div>
						<div id="headline2" style="display:none;">
							<div id="net"></div>
							<span>TEC</span>
							<div id="wifi">
								<div class="dot"></div>
							</div>
							<div id="headline-time"></div>
							<div id="battery"></div>
						</div>
						
						<div id="phone-header">
							<p id="phone-time"></p>
							<p id="phone-date"></p>
						</div>
						<div id="phone-footer">					
							<div id="slider">
								<div id="slider-handler">
									<span></span>
									<span></span>
								</div>	
								<h2>Desliza para desbloquear</h2>
							</div>
						</div>
						
				<div id="contactos" style="display: none;">
					<iframe src="" id="frame_contenido" scrolling="no" ></iframe>
				</div>
						
						
						<div id="icons-container">
							<div class="app-icon">
								<div id="message" >
									<div id="bulb"></div>
									<div id="tail"></div>
								</div>
								<span class="icon-title">Mensajes</span>
							</div>
							<div class="app-icon">
								<div id="calendar">
									<p id="weekday" ></p>
									<p id="date"></p>
								</div>
								<span class="icon-title">Calendario</span>
							</div>
							<div class="app-icon">
								<div id="photos">
									<div id="round1"></div>
									<div id="round2"></div>
									<div id="round3"></div>
									<div id="round4"></div>
									<div id="round5"></div>
									<div id="round6"></div>
									<div id="round7"></div>
									<div id="round8"></div>
								</div>
								<span class="icon-title">Fotos</span>
							</div>
							<div class="app-icon">
								<div id="camera">
									<div id="camera-top1"></div>
									<div id="camera-top2"></div>
									<div id="camera-top3"></div>
									<div class="hack"></div>
									<div id="camera-mid"></div>
									<div class="center-round"></div>
									<div id="camera-bottom"></div>
								</div>
								<span class="icon-title">Camara</span>
							</div>
							<div class="app-icon">
								<div id="weather">
									<div id="sun"></div>
									<div id="cloud">
										<div id="left-round"></div>
										<div id="mid-round"></div>
										<div id="right-round"></div>
										<div id="block"></div>
									</div>
								</div>
								<span class="icon-title">Tiempo</span>
							</div>
							<div class="app-icon">
								<div id="clock">
									<div id="clock-plate"></div>
									<ul>
										<li><span>12</span></li>
										<li><span>1</span></li>
										<li><span>2</span></li>
										<li><span>3</span></li>
										<li><span>4</span></li>
										<li><span>5</span></li>
										<li><span>6</span></li>
										<li><span>7</span></li>
										<li><span>8</span></li>
										<li><span>9</span></li>
										<li><span>10</span></li>
										<li><span>11</span></li>
									</ul>
									<div id="hour"></div>
									<div id="minute"></div>
									<div id="second"></div>
									<div class="dot"></div>
								</div>
								<span class="icon-title">Reloj</span>
							</div>
							<div class="app-icon">
								<div id="map">
									<div id="map-left-up"></div>
									<div id="map-right-up"><div class="hack"></div></div>
									<div id="map-left-down">
										<div class="hack"></div>
										<div id="crown"><span class="hack"></span></div>
										<div id="road">
											<span id="road-left"><span></span></span>
											<span id="road-right"><span></span></span>
										</div>
									</div>
									<div id="map-right-mid"></div>
									<div id="map-right-down"></div>
								</div>
								<span class="icon-title">Mapa</span>
							</div>
							<div class="app-icon">
								<div id="video">
									<div id="up">
										<ul>
											<li><span></span><span></span></li>
											<li><span></span><span></span></li>
											<li><span></span><span></span></li>
											<li><span></span><span></span></li>
										</ul>
									</div>
									<div id="down"></div>
								</div>
								<span class="icon-title">Video</span>
							</div>
							<div class="app-icon">
								<div id="notes">
									<hr/>
									<hr/>
									<hr/>
									<hr/>
								</div>
								<span class="icon-title">Notas</span>
							</div>
							<div class="app-icon">
								<div id="reminders">
									<div class="dot"><hr/></div>
									<div class="dot"><hr/></div>
									<div class="dot"><hr/></div>
									<div class="dot"><hr/></div>
									<div class="dot"><hr/></div>
								</div>
								<span class="icon-title">Recordatorios</span>
							</div>
							<div class="app-icon">
								<div id="stocks">
									<ul id="curve">
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
									</ul>
									<ul id="separate-line">
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
									</ul>
									<div class="dot"></div>
								</div>
								<span class="icon-title">Bolsa</span>
							</div>
							<div class="app-icon">
								<div id="gamecenter">
									<div id="bubble1"></div>
									<div id="bubble2"></div>
									<div id="bubble3"></div>
									<div id="bubble4"></div>
								</div>
								<span class="icon-title">Game Center</span>
							</div>

							<div class="app-icon">
								<div id="appstore">
									<div id="a-symbol"></div>
									<div id="pen1"></div>
									<div id="pen2"><div class="hack"></div></div>
								</div>
								<span class="icon-title">App Store</span>
							</div>
							<div class="app-icon">
								<div id="passbook">
									<div id="half-round"></div>
									<div class="plane">
										<div class="wing"></div>
									</div>
									<div id="recoder">
										<div class="round"></div>
										<div class="round"></div>
									</div>
									<div id="cup-box">
										<div id="cup"></div>
									</div>
									<ul>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
										<li></li>
									</ul>
								</div>
								<span class="icon-title">Wallet</span>
							</div>
							<div class="app-icon">
								<div id="compass">
									<div class="center-round"></div>
									<ul>
									</ul>
									<ol>
										<li>W</li>
										<li>N</li>
										<li>E</li>
										<li>S</li>
									</ol>
									<div id="arrow"></div>
								</div>
								<span class="icon-title">Brujula</span>
							</div>
							
							<div class="app-icon">
								<img src="css/master.png" class="contacto" id="contacto" onclick="cambiar_url('MasterMind/index.html');" >
								<span class="icon-title">MasterMind</span>
							</div>
							
							
			
						</div>
						<div id="dock">
							<div class="app-icon">
								<div id="phone">
									<div id="receiver">
										<span id="part1"></span>
										<span id="part2"></span>
									</div>
								</div>
								<span class="icon-title">Telefono</span>
							</div>
							
							
							<div class="app-icon">
								<img onclick="cambiar_url('Contactos/contacto.py');" src="css/contactos.png" class="contacto" id="contacto">
								<span class="icon-title">Contactos</span>
							</div>
							
							
							
							<div class="app-icon">
								<div id="safari">
									<div class="center-round">
										<ul></ul>
									</div>
								</div>
								<span class="icon-title">Safari</span>
							</div>
							<div class="app-icon">
								<div id="music">
									<div></div>
									<div></div>
									<div></div>
									<div></div>
									<div></div>
								</div>
								<span class="icon-title">Musica</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div id="description">
	<center>
	<img src="css/logo.jpg" width="198px"><br><br>
	
			<h1>Proyecto # 2 de Taller de programacion</h1>
			<p>
				
					Jose Andres Ceciliano Granados<br>
					2016087245<br>
				<br><br>
				<b>Descripcion:</b> Simulacion de un telefono celular, en el area de agenda telefonica
				utilizando python como lenguaje manejador de datos y una interfaz web como recurso principal.
				
			</p><br><br>
			<p>Desliza el recuadro o preciona el boton de Home para desbloquear el iphone, luego la funcion principal es la agenda de contacto y el juego MasterMind, sin embargo nota las funciones de reloj en movimiento (icono)</p>
		</div>
	</div>
</body>
<script type="text/javascript" src="js/jquery-2.0.2.min.js"></script>
<script type="text/javascript" src="js/jquery-ui-1.10.4.custom.min.js"></script>
<script type="text/javascript" src="js/iphone5.js"></script>
</html> ''')
