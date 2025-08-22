import mysql.connector

def crear_conexion():
    """Crea y retorna una conexión a la base de datos"""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",       
        password="",      
        database="biblioteca"
    )
    return conn
