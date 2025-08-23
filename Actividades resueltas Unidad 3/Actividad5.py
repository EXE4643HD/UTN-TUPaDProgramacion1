contra=input("Introduzca una contraseña: ")
supercontra=len(contra)
if supercontra <= 7:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
elif supercontra >=8 or supercontra >=14:
    print("Ha ingresado una contraseña correcta")