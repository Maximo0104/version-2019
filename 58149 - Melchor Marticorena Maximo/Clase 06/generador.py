import random
def generador (minimo, maximo):
    return random.randint (minimo, maximo)
def generador_mejor (minimo, maximo, lista):
    encontrado = True
    while encontrado:
        aleatorio = random.randint (minimo, maximo)
        encontrado = False
        if aleatorio in lista:
            encontrado = True
        # se puede reemplazar las tres lineas anteriores por encontrado = aleatorio in lista
    return aleatorio