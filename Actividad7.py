num1=int(input("Introduzca un numero: "))
num2=int(input("Introduzca un numero: "))

if num1==0:
    num1=int(input("Introduzca un numero que no sea 0: "))

if num2==0:
    num2=int(input("Introduzca un numero que no sea 0: "))

suma= num1 + num2
resta= num1 - num2
multi= num1 * num2
divi= num1 / num2
print (f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multi de {num1} y {num2} es: {multi}")
print(f"La divi de {num1} y {num2} es: {divi}")