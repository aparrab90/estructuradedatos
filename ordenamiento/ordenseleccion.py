def selection_sort(arr):
    n = len(arr)
    print("Tamaño lista", n)
    
    for i in range(n):
        # Supongamos que el elemento actual es el mínimo
        min_index = i
        
        # Buscar el mínimo en el resto del array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Intercambiar el elemento actual con el mínimo encontrado
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Ejemplo de uso
lista = [64, 25, 12, 22, 11,4,4,5,5,6,66,65,5,88,52,245,55,5,5,22,2,5,56,6,3]
selection_sort(lista)
print("--")
print("Lista ordenada:", lista)
