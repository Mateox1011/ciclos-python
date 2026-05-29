cantidadestudiante=int("ingrese la cantidad de estudiantes ") 
contadorestudiantes=0
aprobados=0
reprobados=0
sumadefinitivas=0
while contadorestudiantes < cantidadestudiante:
    definitiva=int(input("ingrese la definitiva del estudiante "))
    if definitiva >= 3:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1
    sumadefinitivas=sumadefinitivas+definitiva
    contadorestudiantes=contadorestudiantes+1
promediodefinitivas=sumadefinitivas/cantidadestudiante
print("cantidad de estudiantes aprobados ", aprobados)
print("cantidad de estudiantes reprobados ", reprobados)
print("promedio de definitivas ", promediodefinitivas)