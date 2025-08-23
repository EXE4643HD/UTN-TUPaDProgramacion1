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