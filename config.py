import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",          # Pon la contraseña de tu MySQL si tiene
        database="colegio_elite"
    )