#!../python35/python.exe
print ("Content-type: text/html\n")
from funciones import * 
config = configuraciones()
pocision = posicion();
dificultad = ["F<br>A<br>C<br>I<br>L","M<br>E<br>D<br>I<br>O","D<br>I<br>F<br>I<br>C<br>I<br>L"]
r = list(random())
borrar_datos_ateriores = open('datos/actual.dat', 'w')
random = r[0]+","+r[1]+","+r[2]+","+r[3]
import cgi
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
nombre = form.getfirst("nombre");
if (int(config[1]) == 1):
	jugadas = 8
if (int(config[1]) == 2):
	jugadas = 7
if (int(config[1]) == 3):
	jugadas = 6
print('''<html>
	<head>
		<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>		
		<script type="text/javascript" src="http://code.jquery.com/ui/1.8.18/jquery-ui.min.js"></script>
		<link type="text/css" rel="stylesheet" href="juego.css">
		<link type="text/css" rel="stylesheet" href="http://getbootstrap.com/dist/css/bootstrap.min.css">
		<script type='text/javascript'>//<![CDATA[''')
if int(config[4]) != 3:
	if int(config[4]) == 1:
		tiempo = int(config[5])
	else: 
		tiempo = int(config[6])
	print('''
			time = '''+str(tiempo)+'''
		var hours = Math.floor( time / 3600 );  
		var minutes = Math.floor( (time % 3600) / 60 );
		var seconds = time % 60;
		minutes = minutes < 10 ? '0' + minutes : minutes;
		seconds = seconds < 10 ? '0' + seconds : seconds;
		$("#segundos").html(seconds);
		$("#minutos").html(minutes);
		$("#horas").html(hours); 
			console.log('''+random+''')
			$(window).load(function(){
				;(function($,undefined){
					$('.item').draggable({
						cancel: "a.ui-icon", 
						revert: true, 
						helper: "clone", 
						cursor: "move"
						, revertDuration: 0 
					});
					var $container
					$('.container').droppable({
						accept: "#items .item",
						activeClass: "ui-state-highlight",
						update : updatePostOrder,
						drop: function( event, ui ) {
							var $item = ui.draggable.clone();
							$(this).addClass('has-drop').append($item);
							$("#items, #containers").disableSelection();
							updatePostOrder();
						}
					});
				})(jQuery);
				Array.prototype.clean = function(deleteValue) {
					for (var i = 0; i < this.length; i++) {
						if (this[i] == deleteValue) {         
							this.splice(i, 1);
							i--;
						}
					}
					return this;
				};
				function updatePostOrder() { 
					var arr = [];
					$('#v1').val($(".1 div").last().attr('id'));
					$('#v2').val($(".2 div").last().attr('id'));
					$('#v3').val($(".3 div").last().attr('id'));
					$('#v4').val($(".4 div").last().attr('id'));

				}''')
	print('''

		''')
print('''	});//]]> 
			var arr2 = 1;
			se = 0
			function contador(){ 
				document.getElementById('iniciar').disabled = true;
				document.getElementById('calcular').disabled = false;
				document.getElementById('fin').disabled = false;
				se = se + 1
				setTimeout("contador()",1000);
				return se
			}
			function iniciar(){
				$.post("proceso.py", {dificultad: "'''+dificultad[int(config[1])-1]+'''",tiempo: se,input: $('#v1').val()+","+$('#v2').val()+","+$('#v3').val()+","+$('#v4').val() ,num : arr2,orden_real: "'''+random+'''", nombre: "'''+nombre+'''" }, function(htmlexterno){
					arr2 += 1;
					if (arr2 <= '''+str(jugadas)+'''){
						$("#resultado").html( htmlexterno + + "<br>" + $("#resultado").html() + "<br><br>");
						$('#v1').val('');
						$('#v2').val('');
						$('#v3').val('');
						$('#v4').val('');
						$("#containers .item").remove();
						
						reiniciar();
					}else{
						$("#resultado").html( htmlexterno + + "<br>" + $("#resultado").html() + "<br><br>");
						window.location="perdio.py";
					}

				});
			}

	var Handle_Mi_Timer = null;
    function Iniciar_Timer() {
		$("#segundos").html(seconds);
		$("#minutos").html(minutes);
		$("#horas").html(hours);
		Handle_Mi_Timer = window.setInterval('Mi_Timer()', 1000); 
	}
    function Detener_Timer() {
		$("#segundos").html(seconds);
		$("#minutos").html(minutes);
		$("#horas").html(hours);
        if(Handle_Mi_Timer!=null) {
            window.clearInterval(Handle_Mi_Timer);
            Handle_Mi_Timer = null;
        }
	
    }

    function Mi_Timer() {
	toSecond= $("#segundos").html()-1;
	if(toSecond<0)
	{
		toSecond=59;
		toMinute= $("#minutos").html()-1;
	}
	else{
		toMinute = $("#minutos").html();
	}
	$("#segundos").html(toSecond);
	if(toMinute<0)
	{
		toMinute=59;
		toHour=$("#horas").html()-1;
	}else{
		toHour = $("#horas").html();
	}
	$("#minutos").html(toMinute);
	$("#horas").html(toHour);
	if(toHour == 0 && toMinute == 0 && toSecond == 0)
	{ ''')

if int(config[4]) == 1:
	print('''iniciar();''')
else: 
	if int(config[4]) == 2:
		print('''window.location="perdio.py";''')

print('''	Detener_Timer();
			Iniciar_Timer();
	}
}
function reiniciar(){
			Detener_Timer();
			Iniciar_Timer();
}

''')
print('''
</script>		
	</head>
	<body>
		<div style="width: 320px;height: 568px; position: absolute; background-color:#8fccaf;    background-color: #8fccaf;background-image: url(../css/master_logo.png); background-repeat: no-repeat;background-position: 56px 144px; ">

			<div class="'''+pocision[0]+'''">
				<table id="containers" style="width: 100%; margin-top:6px; ">
					<tr>
						<td style="font-size: 30px;">
							N
						</td>
						<td>
							<div class="c container 1" id="1"></div>
						</td>
						<td>
							<div class="c container 2" id="2"></div>
						</td>
						<td>
							<div class="c container 3" id="3"></div>
						</td>
						<td>
							<div class="c container 4" id="4"></div>
						</td>
					</tr>
				</table>
				<div id="resultado" style="line-height: 0;width: 250px;" ></div>
			</div>
			<div id="items" class="'''+pocision[1]+'''">
			''')
for x in range (1,7):
	ruta = "datos/elementos/"+ config[3] + "/" + str(x) + ".png"			
	print('''<div id="'''+str(x)+'''" class="'''+str(x)+''' item" style="background:url('''+ruta+''')no-repeat;background-size:contain;"></div>''')
print('''
			<center><p style="margin:20px ;font-size: x-large;font-style: italic;">'''+dificultad[int(config[1])-1]+'''</p>
			</div>
			<!--#################### Controles #####################-->
			<div style="margin-top:450;position:absolute;" class="'''+pocision[2]+'''">
					<table style="width: 260px;">
						<tr>
							<td> 
								<input type="button" id="iniciar" class="ini btn btn-lg btn-success" value="Iniciar" onclick="Iniciar_Timer();contador()" size="30">
							</td>
							<td> 
								<input type="button" id="fin" class="fin btn btn-lg btn-danger" value="Fin" onclick="return confirmar()" size="30" disabled>
							</td>
							
							<td> 
								<input type="button" id="calcular" class="cal btn btn-lg btn-primary" value="Calcular" onclick="iniciar()" size="30" disabled>
							</td>
							
							<tr>
							</table>''')
##TEMA DEL RELOJ
if int(config[4]) != 3:
	print('''
							<table style="margin-top:9px;margin-left:10px;    width: 250px; ">
											<tr>
												<td>
													<center><b>Hora</center>
												</td>
												<td>
													<center><b>Minuto</center>
												</td>
												<td>
													<center><b>Segundo</center>
												</td>

											</tr>
											<tr>
												<td>
													<center><b><div id="horas" class="horas">00</div></center>
												</td>
												<td>
													<center><b><div id="minutos" class="minutos">00</div></center>
												</td>
												<td>
													<center><b><div id="segundos" class="segundos" >00</div> </center>
												</td>
					
											</tr>
										</table>
''')
print('''				
					</div>
						<script>
function confirmar()
{
	if(confirm('Que desea terminar el juego?'))
		window.location='index.html';
	else
		return false;
}
</script>	<br><br><br>
					<input type="text" id="v1" name="v1" value="None" size="2" hidden>
					<input type="text" id="v2" name="v2" value="None" size="2" hidden>
					<input type="text" id="v3" name="v3" value="None" size="2" hidden>
					<input type="text" id="v4" name="v4" value="None" size="2" hidden>
				</body>
			</html>	''')