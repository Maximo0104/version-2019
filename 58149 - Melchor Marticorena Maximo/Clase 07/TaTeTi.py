from tablero import draw_tablero,full,validate,win
tablero = []
for i in range (0,9):
    tablero.append(" ")
draw_tablero(tablero)
while not win(tablero) and not full(tablero):
    print ("Turno del jugador X")
    valido = False
    while not valido:
        print ("Ingrese una posicion del 1 al 9 (X)")
        posicion = int(input())
        valido = validate (tablero,posicion)
        if not valido:
            print ("Error de posicion")
    tablero [posicion -1] = "X"
    draw_tablero(tablero)
    gano = win (tablero)
    if gano:
        print ("Gano X")
    else:
        print ("Turno del jugador O")
        valido = False
        while not valido:
            print ("Ingrese una posicion del 1 al 9 (O)")
            posicion = int(input())
            valido = validate (tablero,posicion)
        if not valido:
            print ("Error de posicion")
        tablero [posicion -1] = "O"
        draw_tablero(tablero)
        gano = win (tablero)
        if gano:
            print ("Gano O")
    if full(tablero) or not win(tablero):
        print ("Nadie gano")
