from conexion import crear_conexion

# Crear la conexión global y cursor
conn = crear_conexion()
cursor = conn.cursor()

def agregar_libro(titulo, autor, anio):
    sql = "INSERT INTO libros (titulo, autor, anio) VALUES (%s, %s, %s)"
    valores = (titulo, autor, anio)
    cursor.execute(sql, valores)
    conn.commit()
    print("✅ Libro agregado con éxito.")

def listar_libros():
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    for libro in libros:
        print(f"ID: {libro[0]} | Título: {libro[1]} | Autor: {libro[2]} | Año: {libro[3]}")

def actualizar_libro(id_libro, nuevo_titulo, nuevo_autor, nuevo_anio):
    sql = "UPDATE libros SET titulo=%s, autor=%s, anio=%s WHERE id=%s"
    valores = (nuevo_titulo, nuevo_autor, nuevo_anio, id_libro)
    cursor.execute(sql, valores)
    conn.commit()
    print("✅ Libro actualizado con éxito.")

def eliminar_libro(id_libro):
    sql = "DELETE FROM libros WHERE id=%s"
    cursor.execute(sql, (id_libro,))
    conn.commit()
    print("✅ Libro eliminado con éxito.")
