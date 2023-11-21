import os


def mostrar_menu_principal():
    print("Menu Principal")
    print("1.  Operaciones con Arreglos")
    print("2.  Operaciones con Cadena")
    print("3.  Operaciones con Lista")
    print("4.  Salir del Programa")
    opcion = input("Ingrese una Opción: ")
    return opcion

def submenu_arreglo():
    while True:
        print("**************Menu de Operaciones con Arreglo**********")
        print("1 Agregar un elemento")
        print("2 Eliminar un Elemento")
        print("3 Volver al menu principal")
        opcion = input("Ingrese una Opción: ")
        if opcion == '1':
            print("Elemento agregado")
        elif opcion =='2':
            print("Elemento eliminado")
        elif opcion=='3':
        #os. system()
            break


def submenu_cadena():
    while True:
        print("///////////////////Menu de Operaciones con Cadena/////////////////////")
        print("1 Evento con Cadena 1")
        print("2 Evento con Cadena 1")
        print("3 Volver al menu principal")
        opcion = input("Ingrese una Opción: ")
        if opcion == '1':
            print("Evento con cadena exitoso 1")

        elif opcion =='2':
            print("Evento con cadena exitoso 2")
        elif opcion=='3':
        #os. system()
            break

def main():
    while True:
        opcion = mostrar_menu_principal()
        if opcion == '1':
            submenu_arreglo()
        elif opcion == '2':
            submenu_cadena()
        elif opcion =='4':
            print("Excelente mañana")
            break
        

if __name__ == "__main__":
    main()