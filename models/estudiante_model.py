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
    def obtener_por_id(id):
        conexion = get_db_connection()
        cursor = conexion.cursor(dictionary=True)
        print(f"id modelo obtener id:{id}\n\n\n")
        print(f"tipo id modelo obtener id:{type(id)}\n\n\n")
        cursor.execute("SELECT * FROM estudiantes WHERE id_estudiante = %s", (id,))
        estudiante = cursor.fetchone()
        conexion.close()
        return estudiante

    @staticmethod
    def crear(nombre, apellido, email, fnac):
        conexion = get_db_connection()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO estudiantes (nombre, apellido, email, fecha_nacimiento) VALUES (%s, %s, %s, %s)",
            (nombre, apellido, email, fnac)
        )
        conexion.commit()
        conexion.close()

    @staticmethod
    def actualizar(id_estudiante, nombre, apellido, email, fnac ):
        conexion = get_db_connection()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE estudiantes SET nombre = %s, apellido = %s, email = %s, fecha_nacimiento = %s WHERE id_estudiante = %s",
            (nombre, apellido, email, fnac, id_estudiante)
        )
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id_estudiante):
        conexion = get_db_connection()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM estudiantes WHERE id_estudiante = %s", (id_estudiante,))
        conexion.commit()
        conexion.close()