numero=int(input("Introduzca el numero que quiera saber la tabla de multiplicacion: "))
i=int(0)
resultado=int(0)
print (f"La tabla de multiplicacion del numero {numero} es:")
while i<=9:
    i=i+1
    resultado=numero * i
    print(f"{numero} * {i} = {resultado}")