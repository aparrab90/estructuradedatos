# Define las estructuras de datos
lista = []
pila = []
cola = []

# Función para mostrar el menú
def mostrar_menu():
    print("Menú:")
    print("1. Operar con la Lista")
    print("2. Operar con la Pila")
    print("3. Operar con la Cola")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

# Función para operar con la Lista
def operar_con_lista():
    while True:
        print("\nOperaciones con Lista:")
        print("1. Agregar elemento")
        print("2. Eliminar elemento")
        print("3. Mostrar la lista")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            elemento = input("Ingresa el elemento a agregar: ")
            lista.append(elemento)
        elif opcion == "2":
            if lista:
                elemento_eliminado = lista.pop()
                print(f"Elemento eliminado: {elemento_eliminado}")
            else:
                print("La lista está vacía.")
        elif opcion == "3":
            print("Lista:", lista)
        elif opcion == "4":
            break

# Función para operar con la Pila
def operar_con_pila():
    while True:
        print("\nOperaciones con Pila:")
        print("1. Apilar elemento")
        print("2. Desapilar elemento")
        print("3. Mostrar la pila")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            elemento = input("Ingresa el elemento a apilar: ")
            pila.append(elemento)
        elif opcion == "2":
            if pila:
                elemento_desapilado = pila.pop()
                print(f"Elemento desapilado: {elemento_desapilado}")
            else:
                print("La pila está vacía.")
        elif opcion == "3":
            print("Pila:", pila)
        elif opcion == "4":
            break

# Función para operar con la Cola
def operar_con_cola():
    while True:
        print("\nOperaciones con Cola:")
        print("1. Encolar elemento")
        print("2. Desencolar elemento")
        print("3. Mostrar la cola")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            elemento = input("Ingresa el elemento a encolar: ")
            cola.append(elemento)
        elif opcion == "2":
            if cola:
                elemento_desencolado = cola.pop(0)
                print(f"Elemento desencolado: {elemento_desencolado}")
            else:
                print("La cola está vacía.")
        elif opcion == "3":
            print("Cola:", cola)
        elif opcion == "4":
            break

# Función principal
def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            operar_con_lista()
        elif opcion == "2":
            operar_con_pila()
        elif opcion == "3":
            operar_con_cola()
        elif opcion == "4":
            print("¡Hasta luego chao!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
