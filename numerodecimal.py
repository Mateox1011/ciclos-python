num=int(input("Ingrese un número: "))
if num > 0:
    copia=num
    contador=0
    suma=0
    while copia > 0:
        digito=copia%10
        suma+=digito
        contador+=1
        copia//=10 
    print("La cantidad de dígitos es:", contador)
    print("La suma de los dígitos es:", suma)    
else:
    print("El número debe ser positivo.")