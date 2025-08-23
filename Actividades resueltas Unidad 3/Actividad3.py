num=int(input("Introduzca un numero: "))
resultado= num % 2
if resultado == 0:
    print(f"El numero {num} es Par")
else:
    print(f"El numero {num} es Impar")
    num=int(input("Por favor introduzca un numero Par: "))
    resultado= num % 2
    print(f"El numero {num} es Par")
