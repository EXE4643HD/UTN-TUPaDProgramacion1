edad=int(input("Introduzca su edad: "))
if edad <= 12:
    print("Ustes es un/a Niño/a")
elif edad >= 12 and edad <= 18:
    print("Usted es un/a Adolecente")
elif edad >= 18 and edad <= 30:
    print("Usted es un/a Adulto/a joven")
elif edad >= 30 and edad <= 100:
    print("Usted es un/a Adolecente mayor")