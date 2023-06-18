# 1. Almacenar los datos de los alumnos en una estructura de datos de manera tal que permita:
alumnos = {}
materias = {}
notas = {}
def leer_archivo(ruta):
    '''Función que lee un archivo'''
    archivo = open(ruta,"r")
    for line in archivo:
        print(line)
    archivo.close()

def agregar_linea(ruta, nueva_linea):
    archivo = open(ruta,"a")
    archivo.write(nueva_linea)
    archivo.close()

def modificar_linea(ruta, numero, nueva_linea):
    archivo=open(ruta,"r")
    lineas =archivo.readlines()
    archivo.close()
    if numero <= len(lineas)-1:
        lineas[numero-1]= nueva_linea
    else:
        print("El numero de lines esta fuera de rango")
    archivo=open(ruta,"w")
    archivo.writelines(lineas)
    archivo.close()
    
#  a. Agregar alumnos
def agrega_alumno():
    '''Función que agrega un alumno a un diccionario - lista'''
    dni = input("Ingresar DNI del alumno: ")
    nombre = input("Ingresar nombre del alumno: ")
    apellido= input("Ingresar apellido del alumno: ")
    direccion= input("Ingresar direccion del alumno: ")
    alumnos[dni] = [nombre, apellido, direccion]
    return alumnos
    
#  b. Modificar datos Personales de los alumnos
def modifica_alumno(dni, alumnos):
    '''Función que modifica los datos de un alumno''' 
    for key in alumnos.keys():
        if key == dni:
            dato = input("""Ingrese inicial de lo que desea modificar
            N - nombre
            A - apellido
            D - direccion""")
            if dato == "N":
                nombre = input("Ingrese el nombre: ")
                alumnos[dni][0] = nombre
            elif dato == "A":
                apellido = input("ingrese el apellido: ")
                alumnos[dni][1] = apellido
            elif dato == "D":
                direccion = input("ingrese la direccion:")
                alumnos[dni][2] = direccion
            else: 
                print("Esa Opcion no existe!")
    return alumnos
            
#  c. Eliminar alumnos
def elimina_alumno(dni, alumnos):
    '''Función que elimina un alumno de una lista'''
    alumnos.pop(dni, "Alumno no encontrado")
    return alumnos

#   2. Almacenar datos de la cursada de materias para cada alumno a fin de:
#   a. Cargar materias
def carga_materia():
    '''Función que agrega una materia nueva'''
    nombre1 = input("Ingrese el nombre de la materia 1: ")
    materias["Materia1"] = nombre1
    nombre2 = input("Ingrese el nombre de la materia 2: ")
    materias["Materia2"] = nombre2
    

#   b. Cargar notas por materia
def carga_notas(notas):
    '''Función que carga notas por materia'''
    print("\tCarga de Materia 1")
    materia1_nota1 = float(input("Ingresa 1ra nota: "))
    materia1_nota2 = float(input("Ingresa 2da nota: "))
    notas["Materia1"] = [materia1_nota1, materia1_nota2]
    print("\tCarga de Materia 2")
    materia2_nota1 = float(input("Ingresa 1ra nota: "))
    materia2_nota2 = float(input("Ingresa 2da nota: "))
    notas["Materia2"] = [materia2_nota1, materia2_nota2]
    return notas

#   c. Modificar notas por materia
def modifica_notas(nombre, notas):
    '''Función que modifica las notas por materia'''
    numero = int(input("Ingese qué nota va a modificar (1 o 2): "))
    for clave in notas.keys():
        if clave == nombre:
            if numero == 1:
                nota1 = float(input("Ingrese la nueva nota 1: "))
                notas[nombre][0] = nota1
            elif numero == 2:
                nota2 = float(input("Ingrese la nueva nota 2: "))
                notas[nombre][1] = nota2
            else:
                print("Número fuera de rango!")
    print(notas)

#   d. Calcular el promedio de notas por materia
def calcula_promedio(notas):
    '''Función que calcula el promedio de las notas por materia'''
    notas["Materia1-Promedio"] = 0
    notas["Materia2-Promedio"] = 0
    for clave in notas.keys():
        total = 0
        if clave == 'Materia1' or clave == 'Materia2':
            lista_notas = notas.get(clave)
            for elemento in lista_notas:
                total += elemento
            promedio = round(total/2, 2)
            if clave == 'Materia1':
                notas["Materia1-Promedio"] = promedio
            elif clave == 'Materia2':
                notas["Materia2-Promedio"] = promedio
    return notas
        
#   e. Establecer la situación del alumno por materia (Regular/ No regular)
 
 
#   3. Insertar datos al archivo Alumnos.txt
#    4. Modificar Datos del Archivo Alumnos.txt (datos Personales de alumnos /notas de las materias/ Situación de la materia)

leer_archivo("Alumnos.txt")

while True:
    print("""Opciones: 
    1- Agregar alumno
    2- Modificar alumno
    3- Eliminar alumno
    4- Cargar materias
    5- Cargar notas por materia
    6- Modificar notas por materia
    7- Calcular el promedio de notas por materia
    8- Establecer la condicion de regularidad del alumno por materia
    0- Fin""") 

    op = input("Seleccione una opcion: ")
    if op == "1":
        agrega_alumno()
        print(alumnos)
    elif op == "2":
        dni = input("Ingrese el dni del alumno que quiere buscar: ")
        modifica_alumno(dni, alumnos)
        print(alumnos)
    elif op == "3":
        dni = input("Ingrese el dni del alumno que quiere eliminar: ")
        elimina_alumno(dni, alumnos)
        print(alumnos)    
    elif op == "4":
        carga_materia()
        print(materias)
    elif op == "5":
        carga_notas(notas)
        print(notas)
    elif op == "6":
        nombre = input("ingrese el nombre de la materia que quiere modificar: ")
        carga_notas(nombre, notas)
        print(notas)
    elif op == "7":
        print("Promedio: ", calcula_promedio(notas))
    elif op == "0":
        break