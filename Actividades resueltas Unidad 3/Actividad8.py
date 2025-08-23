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