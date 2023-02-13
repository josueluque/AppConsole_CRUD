def listar_cursos(cursos):
    """Dado una lista de cursos se imprime por consola la lista de cursos existentes

    Args:
        cursos (list): lista con tuplas de cursos

    Returns:
        None
    
    """
    print("\nCursos: \n")
    contador = 1
    for curso in cursos:
        datos = "{0}. Código: {1} | Materia: {2} | Nota: {3}"
        print(datos.format(contador, curso[0], curso[1], curso[2]))
        contador += 1


def datos_registro():
    """Retorna datos introducidos por el usuario para el registro de un nuevo curso

    Args:
        None

    Returns:
        tuple: Una tupla con el código, nombre y nota del nuevo curso
    
    """
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo = input("\nIngrese código (0 para volver al menu): ")
        if len(codigo) == 6:
            codigoCorrecto = True
        elif codigo == "0":
            break
        else:
            print("Código incorrecto: Debe tener 6 dígitos.")


    if codigoCorrecto:
        nombre, nota = editar_datos()
        curso = (codigo, nombre, nota)
    else:
        curso = None

    return curso


def editar_datos():
    """Retorna datos introducidos por el usuario

    Args:
        None

    Returns:
        strings: nombre y nota
    
    """
    
    nombre = input("Ingrese nombre: ")

    notaCorrecta = False
    while(not notaCorrecta):
        nota = input("Ingrese nota: ")
        if nota.isnumeric():
            if (11 > int(nota) > 0):
                notaCorrecta = True
                nota = int(nota)
            else:
                print("La nota debe ser mayor a 0 y menor o igual a 10.")
        else:
            print("Nota incorrecta: Debe ser un número únicamente.")

    return nombre, nota


def datos_de_actualizacion(cursos):
    """Dado una lista de cursos se retorna los datos para la modifiación del curso indicado

    Args:
        cursos (list): lista con tuplas de cursos

    Returns:
        tuple: código indicado, nombre y nota para la actualización del curso, si no existe el código se devuelve None
    """
    
    listar_cursos(cursos)

    existeCodigo = False
    codigoEditar = input("\nIngrese el código del curso a editar: ")

    for cur in cursos:
        if cur[0] == int(codigoEditar):
            existeCodigo = True
            break
    
    if existeCodigo:
        nombre, nota = editar_datos()
        curso = (codigoEditar, nombre, nota)
    else:
        curso = None

    return curso


def datos_de_eliminacion(cursos):
    """Dado una lista de cursos retorna el código del curso a eliminar

    Args:
        cursos (list): lista con tuplas de cursos

    Returns:
        str: código de curso a ser eliminado y de no ser encuentrado en la base de datos retorna un string vacio
    """

    listar_cursos(cursos)    
    existeCodigo = False
    codigoEliminar = input("\nIngrese el codigo del curso a eliminar: ")

    for cur in cursos:
        if cur[0] == int(codigoEliminar):
            existeCodigo = True
            break
    
    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar

