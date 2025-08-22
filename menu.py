from crud import agregar_libro, listar_libros, actualizar_libro, eliminar_libro, conn

def limpiar_pantalla():
    print("\n" * 5)

def menu():
    while True:
        limpiar_pantalla()
        print("\n=== Biblioteca Virtual ===")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = int(input("Año: "))
            agregar_libro(titulo, autor, anio)

        elif opcion == "2":
            listar_libros()
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            id_libro = int(input("ID del libro a actualizar: "))
            nuevo_titulo = input("Nuevo título: ")
            nuevo_autor = input("Nuevo autor: ")
            nuevo_anio = int(input("Nuevo año: "))
            actualizar_libro(id_libro, nuevo_titulo, nuevo_autor, nuevo_anio)

        elif opcion == "4":
            id_libro = int(input("ID del libro a eliminar: "))
            eliminar_libro(id_libro)

        elif opcion == "5":
            print("\nSaliendo del programa... ¡Hasta pronto!")
            conn.close()
            break

        else:
            print("\nOpción no válida, intente nuevamente.")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu()
