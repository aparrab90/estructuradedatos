def mostrar_menu():
    print("Menú:")
    print("1. Arreglo")
    print("2. Registro")
    print("3. Ordenamiento")
    print("4. Salir")
# Función para la opción 1
def opcion1():
    print("Has seleccionado la Opción 1")
    print("Asi funciona el arreglo")
    arreglob = [
    [1,2,3],
    [4,5,6],
    ]

    print(arreglob[1][2])

# Función para la opción 2
def opcion2():
    print("Has seleccionado la Opción 2")
    empleado= {}
    empleado["id"] = int(input("Ingrese Id: "))
    empleado["Nombre"] = input("Ingrese Nombre: ")
    for key, value in empleado.items():
        print(f"{key} : {value}")

# Función para la opción 3
def opcion3():
    print("Has seleccionado la Opción 3")

# Función principal del programa
def main():
    while True:
        mostrar_menu()
        seleccion = input("Selecciona una opción por favor: ")

        if seleccion == "1":
            opcion1()
        elif seleccion == "2":
            opcion2()
        elif seleccion == "3":
            opcion3()
        elif seleccion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
