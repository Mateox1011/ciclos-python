votosandroid = 0
votosios = 0 
print("prataformas disponibles: ")
print("A. Android")
print("I. iOS")
opcion = input("Ingrese su voto: ")
while opcion != ("A" or "a") and opcion != ("I" or "i"): 
    print("Opción no válida. Por favor, ingrese A para Android o I para iOS.")
    opcion = input("Ingrese su voto: ") 
if opcion == "A":
    votosandroid += 1
else:
    votosios += 1 
print("desea hacer otro voto (s) (n)")
respuesta = input("Ingrese su respuesta: ") 
while respuesta == "s" or respuesta == "S":
    opcion = input("Ingrese su voto: ")
    while opcion != ("A" or "a") and opcion != ("I" or "i"): 
        print("Opción no válida. Por favor, ingrese A para Android o I para iOS.")
        opcion = input("Ingrese su voto: ") 
    if opcion == "A":
        votosandroid += 1
    else:
        votosios += 1 
    print("desea hacer otro voto (s) (n)")
    respuesta = input("Ingrese su respuesta: ")