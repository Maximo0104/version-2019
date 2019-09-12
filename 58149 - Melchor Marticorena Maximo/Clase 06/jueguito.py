from generador import generador, generador_mejor
buscado = generador (1,100000)
lista = []
adivino = False
while adivino == False:
    print ("Ingrese un numero entre 1 y 100000")
    numero = int (input())
    if numero == buscado:
        print ("Ganaste animal!")
        adivino = True
    if numero < buscado:
        print ("El numero es mas grande gil")
    if numero > buscado:
        print ("El numero es mas chico bobo")
    if adivino == False:
        numero2 = generador_mejor(1,100000, lista)
        lista.append(numero2)
        if numero2 == buscado:
            print ("Gano la PC")
            adivino = True