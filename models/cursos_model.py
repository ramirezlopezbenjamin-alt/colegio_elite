from config import get_connection

class CursoModel:

    @staticmethod
    def obtener_todos():
        conexion = get_connection()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cursos")
        cursos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return cursos

    @staticmethod
    def obtener_por_id(id_curso):
        conexion = get_connection()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cursos WHERE id_curso = %s", (id_curso,))
        curso = cursor.fetchone()
        cursor.close()
        conexion.close()
        return curso

    @staticmethod
    def crear(nombre_curso, nivel, id_sala):
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO cursos (nombre_curso, nivel, id_sala) VALUES (%s, %s, %s)",
            (nombre_curso, nivel, id_sala)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def actualizar(id_curso, nombre_curso, nivel, id_sala):
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE cursos SET nombre_curso = %s, nivel = %s, id_sala = %s WHERE id_curso = %s",
            (nombre_curso, nivel, id_sala, id_curso)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar(id_curso):
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM cursos WHERE id_curso = %s", (id_curso,))
        conexion.commit()
        cursor.close()
        conexion.close()