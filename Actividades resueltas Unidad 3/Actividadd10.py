hemisferio=str=str(input("Introduzca el hemisferio donde pertenece, S para Hemisferio Sur y N para Hemisferio Norte: "))
mes=int(input("Introduzca el mes (1-12) en el que esta: "))
dia=int(input("Introduzca el dia (1-31) en el que esta: "))
if hemisferio == "N" or hemisferio == "n":
    if(mes == 12 and dia >=21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        estacion="Invierno"
    elif (mes == 3 and dia >=21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        estacion="Primavera"
    elif (mes == 6 and dia >=21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        estacion="Verano"
    elif (mes == 9 and dia >=21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        estacion="Otoño"
elif hemisferio == "S" or hemisferio == "s":
    if (mes == 12 and dia >=21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        estacion="Verano"
    elif (mes == 3 and dia >=21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        estacion="Otoño"
    elif (mes == 6 and dia >=21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        estacion="Invierno"
    elif (mes == 9 and dia >=21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        estacion="Primavera"

if hemisferio == "N" or hemisferio == "n":
    print(f"Usted esta en Hemisferio Norte, mes {mes}, dia {dia} y la estacion del año es: {estacion}")
elif hemisferio == "S" or hemisferio == "s":
    print(f"Usted esta en Hemisferio Sur, mes {mes}, dia {dia} y la estacion del año es: {estacion}")
