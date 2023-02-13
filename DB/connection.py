import mysql.connector
from mysql.connector import Error

"""
    Clase que realiza la conexión a la base de datos y las operaciones CRUD (Create, Read, Update, Delete)
"""


class DAO():    # Objeto de Acceso a Datos (Data Access Object)

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'Josue_MyAdmin',
                db = 'universidad'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    
    def listar_cursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY materia ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))


    def registrar_curso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO curso (codigo, materia, nota) VALUES ('{0}', '{1}', {2})"
                cursor.execute(sql.format(curso[0], curso[1], curso[2]))
                self.conexion.commit()
                print("¡Curso registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))


    def actualizar(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE curso SET materia = '{0}', nota = {1} WHERE codigo = '{2}'"
                cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print("¡Curso actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))


    def eliminar_curso(self, codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM curso WHERE codigo = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("¡Curso eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))


