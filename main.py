# 1. Almacenar los datos de los alumnos en una estructura de datos de manera tal que permita:
alumnos = []  # Creo una lista para agregar cada alumno (diccionario).


def mostrar_alumnos(alumnos):
    """Función que muestra todos los alumnos registrados"""
    print("\tLISTA DE ALUMNOS REGISTRADOS")
    if not alumnos:
        print("\n\t** REGISTRO VACÍO **")
    else:
        for indice, alumno in enumerate(alumnos, start=1):
            dni = alumno.get("DNI")
            nombre = alumno.get("Nombre")
            apellido = alumno.get("Apellido")
            domicilio = alumno.get("Domicilio")
            materia1 = alumno.get("Materia1")
            m1_nota1 = alumno.get("Materia1-Nota1")
            m1_nota2 = alumno.get("Materia1-Nota2")
            m1_promedio = alumno.get("Materia1-Promedio")
            m1_situacion = alumno.get("Materia1-Situacion")
            materia2 = alumno.get("Materia2")
            m2_nota1 = alumno.get("Materia2-Nota1")
            m2_nota2 = alumno.get("Materia2-Nota2")
            m2_promedio = alumno.get("Materia2-Promedio")
            m2_situacion = alumno.get("Materia2-Situacion")
            print(f"\n\tAlumno N° {indice}: DNI {dni}. {apellido}, {nombre}")
            print(f"Domicilio: {domicilio}")
            print(
                f"Materia {materia1}, nota 1: {m1_nota1} y nota 2: {m1_nota2}. Promedio: {m1_promedio}. Situación:{m1_situacion}"
            )
            print(
                f"Materia {materia2}, nota 1: {m2_nota1} y nota 2: {m2_nota2}. Promedio: {m2_promedio}. Situación:{m2_situacion}"
            )


def mostrar_individual(dni):
    m1_nota1, m1_nota2, m2_nota1, m2_nota2 = 0.0, 0.0, 0.0, 0.0
    m1_promedio, m2_promedio = 0.0, 0.0
    materia1, materia2, m1_situacion, m2_situacion = "", "", "", ""
    for alumno in alumnos:
        if dni in alumno.values():
            materia1 = alumno.get("Materia1")
            m1_nota1 = alumno.get("Materia1-Nota1")
            m1_nota2 = alumno.get("Materia1-Nota2")
            m1_promedio = alumno.get("Materia1-Promedio")
            m1_situacion = alumno.get("Materia1-Situacion")
            materia2 = alumno.get("Materia2")
            m2_nota1 = alumno.get("Materia2-Nota1")
            m2_nota2 = alumno.get("Materia2-Nota2")
            m2_promedio = alumno.get("Materia2-Promedio")
            m2_situacion = alumno.get("Materia2-Situacion")
    return f"\n* Alumno DNI {dni}\n{materia1}=> 1: {m1_nota1} y 2: {m1_nota2}\n\tPromedio: {m1_promedio}\n\tCondición: {m1_situacion}\n{materia2}=> 1: {m2_nota1} y 2: {m2_nota2}\n\tPromedio: {m2_promedio}\n\tCondición: {m2_situacion}\n"


#  a. Agregar alumnos
def agrega_alumno():
    """Función que registra a un alumno con sus datos personales básicos a un diccionario:
    DNI, nombre, apellido y domicilio.
    Se agregan con valores por defecto las claves restantes"""
    print("\n\tREGISTRO de ALUMNO")
    alumno = {
        "DNI": 000,
        "Nombre": "",
        "Apellido": "",
        "Domicilio": "",
        "Materia1": "",
        "Materia1-Nota1": 0.0,
        "Materia1-Nota2": 0.0,
        "Materia1-Promedio": 0.0,
        "Materia1-Situacion": "",
        "Materia2": "",
        "Materia2-Nota1": 0.0,
        "Materia2-Nota2": 0.0,
        "Materia2-Promedio": 0.0,
        "Materia2-Situacion": "",
    }
    try:
        dni = int(input("Ingrese DNI: "))
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        domicilio = input("Domicilio: ")

        alumno["DNI"] = dni
        alumno["Nombre"] = nombre
        alumno["Apellido"] = apellido
        alumno["Domicilio"] = domicilio

        alumnos.append(alumno)
        return f"\n** {apellido}, {nombre}. DNI {dni}. Con domicilio en {domicilio} **\n¡Cargado exitosamente!"
    except ValueError:
        return "Revise lo que está intentando ingresar. Cochino!"


#  b. Modificar datos Personales de los alumnos
def modifica_alumno(alumnos):
    """Función que modifica los datos de un alumno"""
    print("\n\tMODIFICAR ALUMNO")
    if not alumnos:
        return "** NADA PARA MODIFICAR. REGISTRO VACIO **"
    else:
        try:
            dni = int(input("DNI del alumno: "))
            for alumno in alumnos:
                if dni in alumno.values():
                    print("\n\tSe modificarán los datos de", alumno.get("DNI"))
                    print(
                        """Ingrese la letra correspondiente a lo que desea modificar
                        N - Nombre
                        A - Apellido
                        D - Domicilio"""
                    )
                    dato = input("Su elección: ")
                    if dato == "N":
                        nombre = input("Ingrese el nuevo nombre: ")
                        alumno["Nombre"] = nombre
                    elif dato == "A":
                        apellido = input("Ingrese el nuevo apellido: ")
                        alumno["Apellido"] = apellido
                    elif dato == "D":
                        domicilio = input("Ingrese el nuevo domicilio: ")
                        alumno["Domicilio"] = domicilio
                    else:
                        print("¡Esa opción no existe!")
                    return f"\n** El alumno con DNI {dni}, fue modificado con éxito! **"
                else:
                    return "El DNI que busca no está registrado o no existe."
        except ValueError:
            return "Por favor, verifique su ingreso."


#  c. Eliminar alumnos
def elimina_alumno(alumnos):
    """Función que elimina un alumno de una lista en base a su DNI"""
    print("\n\tELIMINAR ALUMNO")
    if not alumnos:
        return "** NADA PARA ELIMINAR. REGISTRO VACIO **"
    else:
        try:
            dni = int(input("DNI del alumno que quiere eliminar: "))
            for alumno in alumnos:  # Recorro la lista de diccionarios
                if dni in alumno.values():
                    print("Eliminando...")
                    alumnos.remove(alumno)
                    return f"** El alumno con DNI {dni}, fue eliminado del registro exitosamente. **"
                else:
                    return "El DNI que busca no está registrado o no existe"
        except ValueError:
            return "VALOR INCORRECTO. Por favor, verifique su ingreso."


#   2. Almacenar datos de la cursada de materias para cada alumno a fin de:
#   a. Cargar materias
def carga_materia(alumnos):
    """Función que agrega una materia nueva para un alumno en particular"""
    print("\n\tCARGA DE MATERIAS POR ALUMNO")
    if not alumnos:
        return " **REGISTRO VACIO. Necesita agregar un alumno primero**"
    else:
        try:
            dni = int(input("DNI del alumno: "))
            for alumno in alumnos:
                if dni in alumno.values():
                    print(f"\n\tMaterias del alumno con DNI {dni}")
                    nombre1 = input("Nombre de la materia 1: ")
                    nombre2 = input("Nombre de la materia 2: ")
                    alumno["Materia1"] = nombre1
                    alumno["Materia2"] = nombre2
                    return f"\n** {nombre1} y {nombre2} cargados correctamente para DNI {dni} **"
                else:
                    return "El DNI que busca no está registrado o no existe"
        except ValueError:
            return "VALOR INCORRECTO. Verifique su ingreso"


#   b. Cargar notas por materia
#   d. Calcular el promedio de notas por materia
#   e. Establecer la situación del alumno por materia (Regular/ No regular)
def carga_notas(alumnos):
    """Función que carga notas por materia, en base al DNI del alumno"""
    print("\tCARGA DE NOTAS POR MATERIA")
    if not alumnos:
        return " **REGISTRO VACIO. Necesita agregar un alumno primero**"
    else:
        try:
            dni = int(input("DNI del alumno: "))
            for alumno in alumnos:
                if dni in alumno.values():
                    print("\n\tCargando notas para alumno con DNI", dni)
                    print("* Notas de", alumno.get("Materia1"))
                    materia1_nota1 = float(input("Ingresa 1ra nota: "))
                    materia1_nota2 = float(input("Ingresa 2da nota: "))

                    # Se establece condición para Materia 1 (¿Regular o No Regular?)
                    if materia1_nota1 < 4.0 or materia1_nota2 < 4.0:
                        alumno["Materia1-Situacion"] = "No Regular"
                    else:
                        alumno["Materia1-Situacion"] = "Regular"

                    # Se calcula el promedio en base a las dos notas de la Materia 1
                    alumno["Materia1-Nota1"] = materia1_nota1
                    alumno["Materia1-Nota2"] = materia1_nota2
                    materia1_promedio = round((materia1_nota1 + materia1_nota2) / 2, 2)
                    alumno["Materia1-Promedio"] = materia1_promedio
                    print()
                    print("* Notas de", alumno.get("Materia2"))
                    materia2_nota1 = float(input("Ingresa 1ra nota: "))
                    materia2_nota2 = float(input("Ingresa 2da nota: "))

                    # Se establece condición para Materia 2 (¿Regular o No Regular?)
                    if materia2_nota1 < 4.0 or materia2_nota2 < 4.0:
                        alumno["Materia2-Situacion"] = "No Regular"
                    else:
                        alumno["Materia2-Situacion"] = "Regular"

                    # Se calcula el promedio en base a las dos notas de la Materia 2
                    alumno["Materia2-Nota1"] = materia2_nota1
                    alumno["Materia2-Nota2"] = materia2_nota2
                    materia2_promedio = round((materia2_nota1 + materia2_nota2) / 2, 2)
                    alumno["Materia2-Promedio"] = materia2_promedio

                    return mostrar_individual(dni)
                else:
                    return "El DNI que busca no está registrado"
        except ValueError:
            return "Valor incorrecto. Verifique su ingreso"


#   c. Modificar notas por materia
def modifica_notas(alumnos):
    """Función que modifica las notas por materia"""
    print("\tMODIFICAR NOTAS POR MATERIA")
    if not alumnos:
        return " **REGISTRO VACIO. Necesita agregar un alumno primero**"
    else:
        try:
            dni = int(input("Ingrese el DNI del alumno: "))
            for alumno in alumnos:
                if dni in alumno.values():
                    print("\n* ¿Qué materia desea modificar? Ingrese 1 ó 2")
                    print("1 ->", alumno.get("Materia1"))
                    print("2 ->", alumno.get("Materia2"))
                    numero_materia = int(input("Su elección: "))
                    # ¿Elegiste "Materia1"?
                    if numero_materia == 1:
                        print(
                            "* ¿Qué notas de",
                            alumno.get("Materia1"),
                            "desea modificar?",
                        )
                        print("1 -> 1ra nota:", alumno.get("Materia1-Nota1"))
                        print("2 -> 2da nota:", alumno.get("Materia1-Nota2"))
                        numero_nota = int(input("Su elección: "))
                        # "Nota1" o "Nota2"?
                        if numero_nota == 1:
                            alumno["Materia1-Nota1"] = float(
                                input("Ingrese la nueva nota: ")
                            )
                        elif numero_nota == 2:
                            alumno["Materia1-Nota2"] = float(
                                input("Ingrese la nueva nota: ")
                            )
                        else:
                            print("Número fuera de rango!")
                        # Evalúa condición del alumno para la Materia 1 en base al cambio de notas
                        nota1 = alumno.get("Materia1-Nota1")
                        nota2 = alumno.get("Materia1-Nota2")
                        if nota1 < 4.0 or nota2 < 4.0:
                            alumno["Materia1-Situacion"] = "No Regular"
                        else:
                            alumno["Materia1-Situacion"] = "Regular"
                        # Calcula el promedio para la Materia 1
                        promedio = round((nota1 + nota2) / 2, 2)
                        alumno["Materia1-Promedio"] = promedio
                    # Pero si la opción es "Materia2"
                    elif numero_materia == 2:
                        print(
                            "* ¿Qué notas de",
                            alumno.get("Materia2"),
                            "desea modificar?",
                        )
                        print("1 -> 1ra nota:", alumno.get("Materia2-Nota1"))
                        print("2 -> 2da nota:", alumno.get("Materia2-Nota2"))
                        numero_nota = int(input("Su elección: "))
                        # Evalúa si es "Nota1" o "Nota2"
                        if numero_nota == 1:
                            alumno["Materia2-Nota1"] = float(
                                input("Ingrese la nueva nota 1: ")
                            )
                        elif numero_nota == 2:
                            alumno["Materia2-Nota2"] = float(
                                input("Ingrese la nueva nota 2: ")
                            )
                        else:
                            print("Número fuera de rango!")
                        # Evalúa la condición del alumno para la Materia 2
                        nota1 = alumno.get("Materia2-Nota1")
                        nota2 = alumno.get("Materia2-Nota2")
                        if nota1 < 4.0 or nota2 < 4.0:
                            alumno["Materia2-Situacion"] = "No Regular"
                        else:
                            alumno["Materia2-Situacion"] = "Regular"
                        # Calcula el promedio de la Materia 2
                        promedio = round((nota1 + nota2) / 2, 2)
                        alumno["Materia2-Promedio"] = promedio
                    else:
                        return "Número fuera de rango!"
                    return "\n", mostrar_individual(dni)
                elif not dni in alumno.values():
                    return "El DNI que busca no está registrado"
        except ValueError:
            return "Valor incorrecto. Verifique su ingreso."


# Leer el contenido del archivo Alumnos.txt
def leer_archivo(ruta):
    """Función que lee el archivo Alumnos.txt"""
    try:
        print("\n\tCONTENIDO DEL ARCHIVO", ruta)
        with open(ruta, "r") as archivo:
            for contador, linea in enumerate(archivo, start=1):
                print(contador, linea)
    except FileNotFoundError:
        print("No existe el archivo o directorio")


#   3. Insertar datos al archivo Alumnos.txt
def agregar_linea(ruta):
    """Función que agrega líneas a un archivo"""
    print(f"\nAGREGANDO NUEVOS DATOS AL ARCHIVO {ruta}...")
    with open(ruta, "a") as archivo:
        for alumno in alumnos:
            nueva_linea = "\t".join(map(str, alumno.values())) + "\n"
            archivo.write(nueva_linea)
    print("Datos agregados exitosamente al archivo", ruta)


#    4. Modificar Datos del Archivo Alumnos.txt (datos Personales de alumnos /notas de las materias/ Situación de la materia)
def modificar_linea(ruta):
    """Función que modifica una línea particular de un archivo"""
    print("\n\tMODIFICAR ARCHIVO (por línea)")
    print("Verifique qué línea desea modificar")
    leer_archivo(ruta)
    # Le pido al usuario el número de línea (te va a dar de 1 a N)
    try:
        numero = int(input("La línea N°: "))
        with open(ruta, "r") as archivo:
            # Almacena en variable "lineas" N número de líneas.
            lineas = archivo.readlines()
            if numero <= len(lineas):
                try:
                    dni = int(input("DNI N°: "))
                    nombre = input("Nombre: ")
                    apellido = input("Apellido: ")
                    domicilio = input("Domicilio: ")
                    materia1 = input("Materia 1: ")
                    materia1_nota1 = float(input("1ra nota: "))
                    materia1_nota2 = float(input("2ra nota: "))
                    materia1_promedio = round((materia1_nota1 + materia1_nota2) / 2, 2)
                    if materia1_nota1 < 4.0 or materia1_nota2 < 4.0:
                        materia1_situacion = "No Regular"
                    else:
                        materia1_situacion = "Regular"
                    materia2 = input("Materia 2: ")
                    materia2_nota1 = float(input("1ra nota: "))
                    materia2_nota2 = float(input("2ra nota: "))
                    materia2_promedio = round((materia2_nota1 + materia2_nota2) / 2, 2)
                    if materia2_nota1 < 4.0 or materia2_nota2 < 4.0:
                        materia2_situacion = "No Regular"
                    else:
                        materia2_situacion = "Regular"

                    nueva_linea = [
                        dni,
                        nombre,
                        apellido,
                        domicilio,
                        materia1,
                        materia1_nota1,
                        materia1_nota2,
                        materia1_promedio,
                        materia1_situacion,
                        materia2,
                        materia2_nota1,
                        materia2_nota2,
                        materia2_promedio,
                        materia2_situacion,
                    ]
                    string_linea = "\t".join(map(str, nueva_linea)) + "\n"
                    lineas[numero - 1] = string_linea
                except ValueError:
                    print("Valor incorrecto. Verifique su ingreso.")
            else:
                print("El número de líneas está fuera de rango")
        with open(ruta, "w") as archivo:
            archivo.writelines(lineas)
    except ValueError:
        print("Valor incorrecto. Verifique su ingreso")


while True:
    print(
        """\n
\t ====================
\t|| MENÚ DE OPCIONES ||
\t ====================
1- Área de ALUMNOS
2- Área de ASIGNATURAS
3- Manejo de ARCHIVOS
4- Mostrar REGISTRO COMPLETO
0- SALIR del programa
    """
    )
    op_menu = int(input("Su elección: "))
    if op_menu == 1:
        while True:
            print(
                """
\t ===================
\t|| ÁREA DE ALUMNOS ||
\t ===================
1- Registrar alumno
2- Modificar alumno
3- Eliminar alumno
4- Mostrar listado de alumnos
0- Salir a Menú Principal
                """
            )
            op_alumno = int(input("Su elección: "))
            if op_alumno == 1:
                print(agrega_alumno())
            elif op_alumno == 2:
                print(modifica_alumno(alumnos))
            elif op_alumno == 3:
                print(elimina_alumno(alumnos))
            elif op_alumno == 4:
                mostrar_alumnos(alumnos)
            elif op_alumno == 0:
                break
            else:
                print("Opción fuera de rango.")
    elif op_menu == 2:
        while True:
            print(
                """
\t =======================
\t|| ÁREA DE ASIGNATURAS ||
\t =======================
1- Cargar materias (por alumno)
2- Cargar notas por cada materia (por alumno)
3- Modificar notas
0- Salir a Menú Principal
                """
            )
            op_asig = int(input("Su elección: "))
            if op_asig == 1:
                print(carga_materia(alumnos))
            elif op_asig == 2:
                print(carga_notas(alumnos))
            elif op_asig == 3:
                print(modifica_notas(alumnos))
            elif op_asig == 0:
                break
            else:
                print("Opción fuera de rango.")
    elif op_menu == 3:
        while True:
            print(
                """
\t =======================
\t|| GESTIÓN de ARCHIVOS ||
\t =======================
1- Ver archivo
2- Insertar datos a un archivo
3- Modificar datos de archivo
0- Salir a Menú Principal
                """
            )
            op_archivo = int(input("Su elección: "))
            if op_archivo == 1:
                leer_archivo("Alumnos.txt")
            elif op_archivo == 2:
                agregar_linea("Alumnos.txt")
            elif op_archivo == 3:
                modificar_linea("Alumnos.txt")
            elif op_archivo == 0:
                break
            else:
                print("Opción fuera de rango.")
    elif op_menu == 4:
        mostrar_alumnos(alumnos)
    elif op_menu == 0:
        break
    else:
        print("Opción fuera de rango.")
