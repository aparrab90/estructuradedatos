def insercion_sort(arr):
    for i in range (1, len(arr)):
        key = arr[i]
        j=i-1

        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        

        arr[j+1]=key

lista = [12,11,13,5,6,1,80,100,-200]
insercion_sort(lista)
print("Lista ordenada: ", lista)

# [12,11,13,5,6]
#key = 11
#key <j  11<12
#[11,12,13,5,6]
#5<13
#[11,12,5,13,6]
#5<12
#[11,5,12,13,6]
#5<11
#[5,11,12,13,6]
#6<13
#[5,11,12,6,13]
#6<12
#[5,11,6,12,13]
#6<5
#[5,6,11,12,13]