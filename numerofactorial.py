num = int(input("Ingrese un número: "))
if num < 0:
    print("El número no puede ser negativo.")
else:
    factorial = 1 
    inferior = 1
    while inferior<=num:
        factorial *= inferior 
        inferior += 1
print("El factorial de", num, "es", factorial) 
