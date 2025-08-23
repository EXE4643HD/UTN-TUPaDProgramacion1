# 1) Escribir un programa que solicite la edad del usuario. Si el 
# usuario es mayor de 18 años,deberá mostrar un mensaje en 
# pantalla que diga “Es mayor de edad”
edad=int(input("Introduzca su edad: "))
if edad >= 18:
    print("Usted es Mayor de edad")
else:
    print("Usted es Menor de edad")

print()
print()
# 2) Escribir un programa que solicite su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un 
# mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.
nota=int(input("Introduzca su nota: "))
if nota >= 6:
    print("Usted esta Aprobado")
else:
    print("Usted esta Desaprobado")
    
print()
print()
# 3) Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla 
# el mensaje "Ha ingresado un número par"; en caso contrario,
# imprimir por pantalla "Por favor, ingrese un número par".
num=int(input("Introduzca un numero: "))
resultado= num % 2
if resultado == 0:
    print(f"El numero {num} es Par")
else:
    print(f"El numero {num} es Impar")
    num=int(input("Por favor introduzca un numero Par: "))
    resultado= num % 2
    print(f"El numero {num} es Par")

print()
print()
# 4) Escribir un programa que solicite al usuario su edad e 
# imprima por pantalla a cuál de las siguientes categorías 
# pertenece:
# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años.
edad=int(input("Introduzca su edad: "))
if edad <= 12:
    print("Ustes es un/a Niño/a")
elif edad >= 12 and edad <= 18:
    print("Usted es un/a Adolecente")
elif edad >= 18 and edad <= 30:
    print("Usted es un/a Adulto/a joven")
elif edad >= 30 and edad <= 100:
    print("Usted es un/a Adolecente mayor")

print()
print()
#5) Escribir un programa que permita introducir contraseñas de 
# entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada,
# imprimir por en pantalla el mensaje "Ha ingresado una contraseña
# correcta"; en caso contrario, imprimir por pantalla 
# "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"
contra=input("Introduzca una contraseña: ")
supercontra=len(contra)
if supercontra <= 7:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
elif supercontra >=8 or supercontra >=14:
    print("Ha ingresado una contraseña correcta")

print()
print()
# 6)La moda (mode), la mediana (median) y la media (mean) son 
# parámetros estadísticos que se pueden utilizar para predecir 
# la forma de una distribución normal a partir del siguiente 
# criterio:
# Sesgo positivo o a la derecha: cuando la media es mayor que 
# la mediana y, a su vez, la mediana es mayor que la moda.
# Sesgo negativo o a la izquierda: cuando la media es menor que 
# la mediana y, a su vez, la mediana es menor que la moda.
# Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que
# tome la lista numeros_aleatorios, calcule su moda, su mediana y
# su media y las compare para determinar si hay sesgo positivo,
# negativo o no hay sesgo. Imprimir el resultado por pantalla.
from statistics import mode, median, mean
import random
mi_lista=[random.randint(1, 100) for i in range(10)]
media=mean(mi_lista)
mediana=median(mi_lista)
moda=mode(mi_lista)
if media > mediana > moda:
    print("Es un Sesgo positivo")
elif media < mediana < moda:
    print("Es un Sesgo negativo")
elif media == mediana == moda:
    print("Sin Sesgo")

print()
print()
# 7) Escribir un programa que solicite una frase o palabra al 
# usuario. Si el string ingresado termina con vocal, añadir un 
# signo de exclamación al final e imprimir el string resultante 
# por pantalla; en caso contrario, dejar el string tal cual lo 
# ingresó el usuario e imprimirlo por pantalla.
palabra=str=str(input("Introduzca una palabra: "))
palabra_final=palabra[-1]
if palabra_final == "a" or palabra_final == "e" or palabra_final == "i" or palabra_final == "o" or palabra_final == "u":
    print(f"{palabra}!")
else:
    print(palabra)

print()
print()
# 8) Escribir un programa que solicite al usuario que ingrese su 
# nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas.Ejem: PEDRO.
# 2. Si quiere su nombre en minúsculas. Ejem: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula.Ejem: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la
# opción seleccionada por el usuario e imprimir el resultado por 
# pantalla.
nombre=str=str(input("Introduzca su nombre: "))
nombre_mayuscula=nombre.upper()
nombre_minuscula=nombre.lower()
nombre_InicialMayus=nombre.title()
print("Si quiere su nombre todo mayuscula, introduzca el 1")
print("Si quiere su nombre todo mayuscula, introduzca el 2")
num=int=int(input("Si quiere que su nombre tenga solo la primera letra mayuscula, introduzca el 3: "))
if num == 1:
    print(nombre_mayuscula)
elif num == 2:
    print(nombre_minuscula)
elif num == 3:
    print(nombre_InicialMayus)

print()
print()
# 9) Escribir un programa que pida al usuario la magnitud de un 
# terremoto, clasifique la magnitud en una de las siguientes 
# categorías según la escala de Richter e imprima el resultado
#por pantalla:
# Menor que 3: "Muy leve" (imperceptible).
# Mayor o igual que 3 y menor que 4: "Leve"(ligeramente perceptible).
# Mayor o igual que 4 y menor que 5: "Moderado" 
# (sentido por personas, pero generalmente no causa daños).
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños 
# en estructuras débiles).
# Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar 
# daños significativos).
# Mayor o igual que 7: "Extremo" (puede causar graves daños a 
# gran escala).
escala=int=int(input("Introduzca la magnitud del temblor: "))
if escala < 3:
    print("Temblor Muy Leve")
elif escala >= 3 and escala < 4:
    print("Temblor Leve")
elif escala >= 4 and escala < 5:
    print("Temblor Moderado")
elif escala >= 5 and escala < 6:
    print("Temblor Fuerte")
elif escala >= 6 and escala < 7:
    print("Temblor Muy Fuerte")
elif escala > 7:
    print("Temblor Extremo")

print()
print()
# 10) Escribir un programa que pregunte al usuario en cuál 
# hemisferio se encuentra (N/S), qué mes del año es y qué día es.
# El programa deberá utilizar esa información para imprimir por 
# pantalla si el usuario se encuentra en otoño, invierno, 
# primavera o verano.
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