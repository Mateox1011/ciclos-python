num=int(input("Ingrese un número: "))
contador=0
copia=num
while copia > 0:
    digito=copia%10
    contador+=1
    suma+=digito**contador
    if suma == num:
        print(num, "es un número Armstrong.")
    else:
        print(num, "no es un número Armstrong.")

        