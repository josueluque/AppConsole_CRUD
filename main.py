from DB.connection import DAO
import functions


def menu_principal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("=========== Menu Principal ===========")
            print("1.- Listar cursos")
            print("2.- Registrar curso")
            print("3.- Actualizar curso")
            print("4.- Eliminar curso")
            print("5.- Salir")
            print("======================================")
            
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente..")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema :D!")
                break
            else:
                ejecutar_opcion(opcion)
                opcionCorrecta = True


def ejecutar_opcion(opcion):
    dao = DAO()

    if opcion == 1:
        lista_de_cursos(dao)

    elif opcion == 2:
        agregar_curso(dao)
    
    elif opcion == 3:
        actualizar_curso(dao)

    elif opcion == 4:
        eliminar_curso(dao)
        
    else:
        print("Opción no valida")  


def lista_de_cursos(dao):
    try:    
        cursos = dao.listar_cursos()
        if len(cursos) > 0:
            functions.listar_cursos(cursos)
        else:
            print("No se encontraron cursos...")
    except:
        print("Ocurrió un error...")


def agregar_curso(dao):
    try:
        curso = functions.datos_registro()
        if curso:
            dao.registrar_curso(curso)
        else:
            print("¡Registro cancelado con exito!\n")
    except:
        print("Ocurrió un error...")


def actualizar_curso(dao):
    try:
        cursos = dao.listar_cursos()
        if len(cursos) > 0:
            curso = functions.datos_de_actualizacion(cursos)
            if curso:
                dao.actualizar(curso)
            else:
                print("Código de curso a actualizar no encontrado...\n")
        else:
            print("No se encontraron cursos...")
    except:
        print("Ocurrió un error...")


def eliminar_curso(dao):
    try:
        cursos = dao.listar_cursos()
        if len(cursos) > 0:
            codigoEliminar = functions.datos_de_eliminacion(cursos)
            if not(codigoEliminar == ""):
                dao.eliminar_curso(codigoEliminar)
            else:
                print("Código de curso no encontrado...\n")
        else:
            print("No se encontraron cursos...")
    except:
        print("Ocurrió un error...")


if __name__ == "__main__":
    menu_principal()