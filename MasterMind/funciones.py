#!../python35/python.exe

def configuraciones():
	config = open("datos/config.dat","r")
	resultado = config.read().split(",")
	return resultado
def seleccionado(elemento, config):
        if elemento == int(config):
                return 'checked="checked"'

def posicion():
        config = configuraciones()
        if int(config[2]) == 1:
                return ['left','right','left']
        else:
                return ['right','left','right']

def resultado(valores,real):
        resultado = []
        for x in range (0,4):
                if valores[x] == real[x]:
                        resultado.append("black")
                else:
                        if valores[x] in real:
                                resultado.append("white")
                        else:
                                resultado.append("")
        #hay que hacer que se mesclen
        return resultado

def random(valor):
        if valor == 1:
                import random
                elementos = ['1', '2', '3', '4', '5', '6']
                r = open("datos/randoms.dat","a")
                lista = []
                infile = open('datos/randoms.dat', 'r')
                for line in infile:
                        linea = tuple(line.split(","))
                        lista.append(linea[0])
                x = 0
                n = random.choice(elementos)+random.choice(elementos)+random.choice(elementos)+random.choice(elementos)              
                while x <= len(lista):
                        if str(n) == str(lista[x]):
                                n = random.choice(elementos)+random.choice(elementos)+random.choice(elementos)+random.choice(elementos)
                                x -= 1
                        else:
                                resultado = r.write(n+',\n')
                                break;
                        x += 1
                
                numero = (lista[len(lista)-1])
                if len(lista) > 100:
                        infile = open('datos/randoms.dat', 'w')
                        infile.write('1234'+',\n')
                return(numero)
        else:
              infile = open('datos/randoms.dat', 'r')
              randon = []
              n = 0
              for x in infile:
                      randon.append(x)
                      n += 1 
              return(randon[n-2])


def juego_actual(orden):
        infile = open('datos/actual.dat', 'a')
        infile.write(orden+',\n')
        return False

def al_top(nombre,tiempo,real,dificuldad):
        infile = open('datos/actual.dat', 'r')
        lista = []
        lista2 = ""
        for line in infile:
                linea = tuple(line.split(","))
                lista.append(linea)        
        for j in lista:
                lista2 = lista2 + j[0]+"|"+j[1]+"|"+j[2]+"|"+j[3]+"/"
        arc = open('datos/mastertop10.dat', 'a')
        arc.write(nombre+','+str(tiempo)+','+real+','+dificuldad+','+lista2+',\n')
        
        return False        

def top(modo):
        arc = open('datos/mastertop10.dat', 'r')
        datos = modalidades_detalle()
        d = datos[modo]
        d.sort(key=lambda x:x[1],reverse= False)
        s = 0
        for line in d:
                s += 1
                #print(line)
                nombre = line[0].split(" ")
                print('''
		<tr>
			<td>
				<center>'''+str(s)+'''</center>
			</td>
			<td>
				<center>'''+nombre[0]+'''</center>
			</td>
			<td>
				<center>'''+str(line[1])+'''</center>
			</td>
			<td>
				<center><a href="top_detalle.py?id='''+str(line[3])+'''&modo='''+str(modo)+'''" class="btn btn-l btn-primary">Detalle</a></center>
			</td>
		</tr>''')
def top_detalle(ide):
        arc = open('datos/mastertop10.dat', 'r')
        s = 0
        for line in arc:
                if int(s) == int(ide):
                        datos = line.split(",")
                        return datos
                s += 1

def modalidades_detalle():
        arc = open('datos/mastertop10.dat', 'r')
        datos = []
        elementos = ['F<br>A<br>C<br>I<br>L','M<br>E<br>D<br>I<br>O','D<br>I<br>F<br>I<br>C<br>I<br>L']
        x = 0
        for line in arc:
                datos1 = line.split(",")
                datos.extend([[datos1[0],int(datos1[1]),datos1[6],x]])
                x += 1
        datos.sort(key=lambda x:x[2])
        facil = []
        medio = []
        dificil = []
        for z in datos:
                if z[2] == elementos[0]:
                        facil.append(z)
                if z[2] == elementos[1]:
                        medio.append(z)
                if z[2] == elementos[2]:
                        dificil.append(z)
        facil.sort(key=lambda x:x[1])
        medio.sort(key=lambda x:x[1])
        dificil.sort(key=lambda x:x[1])
        return(facil[:10],medio[:10],dificil[:10])

def juego_multi():
        config = open("datos/config.dat","r")
        datos = config.read().split(",")
        
        r = ""
        if (int(datos[1]) == 3 ):
                if int(datos[1]) == 2:
                        datos[1] = 3
                else:
                        datos[1] = 1 
        else:
                if int(datos[1]) == 1:
                        datos[1] = 2
                else:
                        datos[1] = 3

        config2 = open("datos/config.dat","w")
        config2.write(datos[0]+","+str(datos[1])+","+datos[2]+","+datos[3]+","+datos[4]+","+datos[5]+","+datos[6]+","+datos[7]+","+datos[8])

def carga():
        infile = open('datos/actual.dat', 'r')
        ar = ""
        for x in infile:
                s = x.split(",")
                ar = ar + "'"+s[0]+','+s[1]+','+s[2]+','+s[3]+"',"
        return(ar[0:-1])

def reestablecer():
        config2 = open("datos/config.dat","w")
        config2.write("Usuario,1,1,2,1,60,300,300,#8fccaf")

