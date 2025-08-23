palabra=str=str(input("Introduzca una palabra: "))
palabra_final=palabra[-1]
if palabra_final == "a" or palabra_final == "e" or palabra_final == "i" or palabra_final == "o" or palabra_final == "u":
    print(f"{palabra}!")
else:
    print(palabra)