# 1. Almacenar los datos de los alumnos en una estructura de datos de manera tal que permita:
alumnos = []  # Creo una lista para agregar cada alumno (diccionario).

def leer_archivo(ruta):
    """Función que lee un archivo"""
    try:
        archivo = open(ruta, "r")
        for line in archivo:
            print(line)
        archivo.close()
    except FileNotFoundError:
        print("No existe el archivo o directorio")


leer_archivo("Alumnos.txt")


def agregar_linea(ruta, nueva_linea):
    """Función que agrega una línea a un archivo"""
    archivo = open(ruta, "a")
    archivo.write(nueva_linea)
    archivo.close()


def modificar_linea(ruta, numero, nueva_linea):
    """Función que modifica una línea de un archivo"""
    archivo = open(ruta, "r")
    lineas = archivo.readlines()
    archivo.close()
    if numero <= len(lineas) - 1:
        lineas[numero - 1] = nueva_linea
    else:
        print("El número de líneas esta fuera de rango")
    archivo = open(ruta, "w")
    archivo.writelines(lineas)
    archivo.close()


#  a. Agregar alumnos
def agrega_alumno():
    """Función que agrega un alumno a un diccionario.
    DNI, nombre, apellido y dirección"""
    alumno = {
        "DNI": 000,
        "Nombre": "",
        "Apellido": "",
        "Domicilio": "",
        "Materia1": "",
        "Materia1-Notas": [],
        "Materia1-Promedio": 0.0,
        "Materia1-Situacion": "",
        "Materia2": "",
        "Materia2-Notas": [],
        "Materia2-Promedio": 0.0,
        "Materia2-Situacion": "",
    }

    dni = int(input("Ingresar DNI del alumno: "))
    nombre = input("Ingresar nombre del alumno: ")
    apellido = input("Ingresar apellido del alumno: ")
    domicilio = input("Ingresar direccion del alumno: ")
    # VER = alumnos[dni] = [nombre, apellido, direccion]
    alumno["DNI"] = dni
    alumno["Nombre"] = nombre
    alumno["Apellido"] = apellido
    alumno["Domicilio"] = domicilio
    alumnos.append(alumno)
    return alumno


#  b. Modificar datos Personales de los alumnos
def modifica_alumno(dni, alumnos):
    """Función que modifica los datos de un alumno"""
    for alumno in alumnos:
        for valor in alumno.values():
            if valor == dni:
                print("\n\tModificar los datos de", alumno.get("DNI"))
                dato = input(
                    """Ingrese inicial de lo que desea modificar
                N - Nombre
                A - Apellido
                D - Domicilio"""
                )
                if dato == "N":
                    nombre = input("Ingrese el nuevo nombre: ")
                    alumno["Nombre"] = nombre
                elif dato == "A":
                    apellido = input("Ingrese el nuevo apellido: ")
                    alumno["Apellido"] = apellido
                elif dato == "D":
                    domicilio = input("Ingrese el nuevo domicilio:")
                    alumno["Domicilio"] = domicilio
                else:
                    print("¡Esa opción no existe!")
            return f"El alumno con DNI {dni}, fue modificado con éxito."


#  c. Eliminar alumnos
def elimina_alumno(dni, alumnos):
    """Función que elimina un alumno de una lista en base a su DNI"""
    for alumno in alumnos:  # Recorro la lista de diccionarios
        for valor in alumno.values():  # Recorro cada diccionario por sus claves
            if valor == dni:
                print("Eliminando...")
                alumnos.remove(alumno)
                return f"El alumno con DNI {dni}, fue eliminado del registro."
    


#   2. Almacenar datos de la cursada de materias para cada alumno a fin de:
#   a. Cargar materias
def carga_materia(dni, alumnos):
    """Función que agrega una materia nueva para un alumno"""
    for alumno in alumnos:
        for valor in alumno.values():
            if valor == dni:
                print("\n\tMaterias del alumno con DNI", alumno.get("DNI"))
                nombre1 = input("Ingrese el nombre de la materia 1: ")
                nombre2 = input("Ingrese el nombre de la materia 2: ")
                alumno["Materia1"] = nombre1
                alumno["Materia2"] = nombre2
    return alumnos


#   b. Cargar notas por materia
def carga_notas(dni, alumnos):
    """Función que carga notas por materia, en base al DNI del alumno"""
    for alumno in alumnos:
        for valor in alumno.values():
            if valor == dni:
                print("\n\tCargando notas para alumno con DNI", alumno.get("DNI"))
                print("* Notas de", alumno.get("Materia1"))
                materia1_nota1 = float(input("Ingresa 1ra nota: "))
                materia1_nota2 = float(input("Ingresa 2da nota: "))
                alumno["Materia1-Notas"] = [materia1_nota1, materia1_nota2]
                print()
                print("* Notas de", alumno.get("Materia2"))
                materia2_nota1 = float(input("Ingresa 1ra nota: "))
                materia2_nota2 = float(input("Ingresa 2da nota: "))
                alumno["Materia2-Notas"] = [materia2_nota1, materia2_nota2]
    return alumnos


#   c. Modificar notas por materia
def modifica_notas(dni, alumnos):
    """Función que modifica las notas por materia"""
    for alumno in alumnos:
        for value in alumno.values():
            if value == dni:
                print("\n* ¿Qué materia desea modificar? Ingrese 1 ó 2")
                print("1->", alumno.get("Materia1"))
                print("2->", alumno.get("Materia2"))
                numero_materia = int(input("Su elección: "))
                if numero_materia == 1:  # Corresponde a {"Materia1-Notas" = [0.0, 0.0]}
                    print(
                        "¿Qué notas de la materia",
                        alumno.get("Materia1"),
                        "desea modificar?",
                    )
                    print("1-> Para 1ra nota\n2-> Para 2da nota")
                    numero_nota = int(input("Su elección: "))
                    if numero_nota == 1:
                        nota1 = float(input("Ingrese la nueva nota 1: "))
                        alumno["Materia1-Notas"][0] = nota1
                    elif numero_nota == 2:
                        nota2 = float(input("Ingrese la nueva nota 2: "))
                        alumno["Materia1-Notas"][1] = nota2
                    else:
                        print("Número fuera de rango!")
                elif numero_materia == 2:  # {"Materia2-Notas" = [0.0, 0.0]}
                    print(
                        "¿Qué notas de la materia",
                        alumno.get("Materia2"),
                        "desea modificar?",
                    )
                    print("1-> Para 1ra nota\n2-> Para 2da nota")
                    numero_nota = int(input("Su elección: "))
                    if numero_nota == 1:
                        nota1 = float(input("Ingrese la nueva nota 1: "))
                        alumno["Materia2-Notas"][0] = nota1
                    elif numero_nota == 2:
                        nota2 = float(input("Ingrese la nueva nota 2: "))
                        alumno["Materia2-Notas"][1] = nota2
                    else:
                        print("Número fuera de rango!")
                else:
                    print("Número fuera de rango!")
    return alumnos


#   d. Calcular el promedio de notas por materia
def calcula_promedio(alumnos):
    """Función que calcula el promedio de las notas por materia para todos los alumnos"""
    for alumno in alumnos:
        for clave in alumno.keys():
            total = 0
            if clave == "Materia1-Promedio":
                lista_notas1 = alumno.get("Materia1-Notas")
                for elemento in lista_notas1:
                    total += elemento
                promedio1 = round(total / 2, 2)
                alumno["Materia1-Promedio"] = promedio1
            elif clave == "Materia2-Promedio":
                lista_notas2 = alumno.get("Materia2-Notas")
                for elemento in lista_notas2:
                    total += elemento
                promedio2 = round(total / 2, 2)
                alumno["Materia2-Promedio"] = promedio2
    return alumnos


#   e. Establecer la situación del alumno por materia (Regular/ No regular)
def situacion_alumno(alumnos):
    """Función que determina si el alumno por el que se consulta es REGULAR o NO REGULAR"""
    for alumno in alumnos:
        materia1 = alumno.get("Materia1-Notas")
        if materia1[0] < 4.0 or materia1[1] < 4.0:
            alumno["Materia1-Situacion"] = "No Regular"
        else:
            alumno["Materia1-Situacion"] = "Regular"
        materia2 = alumno.get("Materia2-Notas")
        if materia2[0] < 4.0 or materia2[1] < 4.0:
            alumno["Materia2-Situacion"] = "No Regular"
        else:
            alumno["Materia2-Situacion"] = "Regular"
    return alumnos


#   3. Insertar datos al archivo Alumnos.txt
#    4. Modificar Datos del Archivo Alumnos.txt (datos Personales de alumnos /notas de las materias/ Situación de la materia)


while True:
    print(
        """Opciones: 
    1- Agregar alumno
    2- Modificar alumno
    3- Eliminar alumno
    4- Mostrar lista de alumnos
    5- Cargar materias por alumno
    6- Cargar notas de las materias por alumno
    7- Modificar notas por materia
    8- Calcular el promedio de notas por materia
    9- Establecer la condicion de regularidad del alumno por materia
    0- Fin"""
    )

    op = input("Seleccione una opcion: ")
    if op == "1":
        print("\tREGISTRAR ALUMNO")
        agrega_alumno()
        print(alumnos)
    elif op == "2":
        print("\tMODIFICAR ALUMNO")
        dni = int(input("Ingrese el dni del alumno que quiere modificar: "))
        print(modifica_alumno(dni, alumnos))
    elif op == "3":
        print("\tELIMINAR ALUMNO")
        dni = int(input("Ingrese el dni del alumno que quiere eliminar: "))
        print(elimina_alumno(dni, alumnos))
    elif op == "4":
        print("\tLISTA DE ALUMNOS REGISTRADOS")
        for elemento in alumnos:
            print(elemento)
    elif op == "5":
        print("\tCARGA DE MATERIAS POR ALUMNO")
        dni = int(input("Ingrese el DNI del alumno: "))
        carga_materia(dni, alumnos)
    elif op == "6":
        print("\tCARGA DE NOTAS POR MATERIA")
        dni = int(input("Ingrese el DNI del alumno: "))
        carga_notas(dni, alumnos)
    elif op == "7":
        dni = int(input("Ingrese el DNI del alumno cuyas notas quiere modificar: "))
        modifica_notas(dni, alumnos)
    elif op == "8":
        print("\tCALCULAR PROMEDIO")
        print(calcula_promedio(alumnos))
    elif op == "9":
        print("\tSITUACIÓN DE LOS ALUMNOS")
        print(situacion_alumno(alumnos))
    elif op == "0":
        break
