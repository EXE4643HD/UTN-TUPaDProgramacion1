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