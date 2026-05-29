seguir = "S"

while seguir == "S" or seguir == "s":
    tabla = 0
    while tabla < 1 or tabla > 20:
        tabla = int(input("¿Con cuál tabla desea jugar? (1-20): "))
        if tabla < 1 or tabla > 20:
            print("Número inválido. Intente de nuevo.")
    aciertos = 0
    desaciertos = 0
    for contadorFilas in range(1, 11):
        producto = tabla * contadorFilas
        respuesta = int(input(f"Escriba el resultado de {tabla} x {contadorFilas}: "))
        if respuesta == producto:
            print("Felicitaciones")
            aciertos += 1
        else:
            print("Lo siento, ese no es el resultado")
            print("La respuesta correcta es:", producto)
            desaciertos += 1
    print("Aciertos:", aciertos)
    print("Desaciertos:", desaciertos)
    if aciertos <= 5:
        print("Desempeño: Insuficiente")
    elif aciertos <= 7:
        print("Desempeño: Aceptable")
    elif aciertos <= 9:
        print("Desempeño: Sobresaliente")
    else:
        print("Desempeño: Excelente")
    while True:
        seguir = input("¿Desea volver a jugar [S] o [N]?: ")
        if seguir in ["S", "s", "N", "n"]:
            break