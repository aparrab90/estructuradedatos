def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def main():
    while True:
        print("1. Ordenar una lista")
        print("2. Salir")
        choice = input("Elije una opción: ")

        if choice == "1":
            lista = input("Ingresa una lista de números separados por espacios: ")
            lista = [int(x) for x in lista.split()]
            insertion_sort(lista)
            print("Lista ordenada:", lista)
        elif choice == "2":
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
