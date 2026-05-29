cantidadDeNumeros = int(input("Ingrese la cantidad de números: "))
for num in range(1, cantidadDeNumeros + 1):
    print(num, "   ", num * num, "   ", num + (num * num))