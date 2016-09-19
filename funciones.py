#!../python35/python.exe
def insertar(vector):
                vec = vector.split(",")
                f = open('datos/vector.txt','a')
                import csv
                reader = csv.reader(open('datos/vector.txt', 'r'))
                flag = True
                for index,row in enumerate(reader):
                    if(row[0] == vec[0] ):
                        flag = False
                if (flag and vec[0] != "None"):
                        f.write(str(vector) + '\n')
                        return True  
                else:
                    if (vec[0] != "None"):
                        print("<script>alert('Numero registrado anteriormente');</script>")
                    else:
                        print("<script>alert('Numero invalido');</script>")    
                f.close()

def eliminar(num):
                num = int(num)
                f = open("datos/vector.txt","r")
                lineas = f.readlines()
                f.close()
                f = open("datos/vector.txt","w")
                for linea in lineas:
                    datos = linea.split(",")
                    if int(datos[0]) != num:
                        f.write(linea)
                f.close()
                
def actualizar(vector):
                vec = vector.split(",")
                eliminar(vec[0])
                insertar(vector)
def leer(ide):
                lista = []
                infile = open('datos/vector.txt', 'r')
                for line in infile:
                        line2 = line.split(",")
                        if (int(line2[0]) == int(ide)):
                            return line2
                return False
                infile.close()
def convertir_lista():
        import csv
        with open('datos/vector.txt', 'r') as f:
            reader = csv.reader(f)
            lista = list(reader)
        return lista
def todo():
                lista = []
                infile = open('datos/vector.txt', 'r')
                for line in infile:
                        lista.append(line.split())       
                infile.close()
                return lista
            
def contactos():
                import operator
                lista = []
                infile = open('datos/vector.txt', 'r')
                for line in infile:
                        line = line.split(",")
                        lista.append([line[1] + " "+  line[2],line[0],line[3]])
                lista.sort()
                for x in lista:
                    if x[2] != "None":
                        img = x[2]
                    else:
                        img = "profile.png"
                    print('''<li class="list-row"><img class="imgcon" src="datos/imagenes/'''+img+'''"><a href="ver_contacto.py?num='''+x[1]+'''" class="list-link" class="nombre">'''+x[0]+'''</a></li>''')
                infile.close()
                
def adicionales():
                lista = []
                dic = {}
                infile = open('datos/dic.txt', 'r')
                for line in infile:
                        lista.append(line.split(","))       
                infile.close()
                for x in lista:
                    dato = x[0].split(":")
                    dic[dato[0]] = dato[1]
                
                return (dic)
            
def in_ad(clave,tipo):
                f = open('datos/dic.txt','a')
                f.write(clave+":"+ tipo+',\n')
                f.close()
                
def elimin_ad(clave):
                f = open("datos/dic.txt","r")
                lineas = f.readlines()
                f.close()
                f = open("datos/dic.txt","w")
                escribir =""
                for linea in lineas:
                    datos = linea.split(",")
                    datos = datos[0].split(":")
                    if (datos[0]) != clave:
                        escribir = escribir + linea
                        f.write(linea)
                    else:
                        f.write(":"+datos[1]+",\n")
                        escribir = escribir + ":"+datos[1] + ",\n"
                f.close()
                print(escribir)






                
