cantidaddeterminos = int(input("Ingrese la cantidad de términos: "))
termino=1
for contadornumeros in range(1, cantidaddeterminos):
    print(termino,",", end="")
    termino+= 2 
print(termino) 
