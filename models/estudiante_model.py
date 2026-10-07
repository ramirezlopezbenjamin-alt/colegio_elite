from config import get_db_connection

class EstudianteModel:

    @staticmethod
    def obtener_todos():
        conexion = get_db_connection()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM estudiantes")
        estudiantes = cursor.fetchall()
        conexion.close()
        return estudiantes

    @staticmethod
    def obtener_por_id(id_estudiante):
        conexion = get_db_connection()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (id_estudiante,))
        estudiante = cursor.fetchone()
        conexion.close()
        return estudiante

    @staticmethod
    def crear(nombre, apellido, email):
        conexion = get_db_connection()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO estudiantes (nombre, apellido, email) VALUES (%s, %s, %s)",
            (nombre, apellido, email)
        )
        conexion.commit()
        conexion.close()

    @staticmethod
    def actualizar(id_estudiante, nombre, apellido, email):
        conexion = get_db_connection()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE estudiantes SET nombre = %s, apellido = %s, email = %s WHERE id = %s",
            (nombre, apellido, email, id_estudiante)
        )
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id_estudiante):
        conexion = get_db_connection()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM estudiantes WHERE id = %s", (id_estudiante,))
        conexion.commit()
        conexion.close()