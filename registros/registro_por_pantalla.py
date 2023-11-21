empleado= {}

empleado["id"] = int(input("Ingrese Id: "))
empleado["Nombre"] = input("Ingrese Nombre: ")

for key, value in empleado.items():
    print(f"{key} : {value}")
