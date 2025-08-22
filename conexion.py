import mysql.connector

def crear_conexion():
    """Crea y retorna una conexión a la base de datos"""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",       # Tu usuario de MySQL/phpMyAdmin
        password="",       # Tu contraseña (si no tienes, déjalo vacío)
        database="biblioteca"
    )
    return conn
