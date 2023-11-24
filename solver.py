import sudokureader as sd
def imprimir_tablero(tablero):
    n = len(tablero)
    for i in range(n):
        for j in range(n):
            print(tablero[i][j], end=" ")
        print()

def es_letra_valida(tablero, fila, columna, letra):
    n = len(tablero)

    for i in range(n):
        if tablero[fila][i] == letra or tablero[i][columna] == letra:
            return False

    cuadrante_size = int(n**0.5)
    start_row, start_col = cuadrante_size * (fila // cuadrante_size), cuadrante_size * (columna // cuadrante_size)
    for i in range(start_row, start_row + cuadrante_size):
        for j in range(start_col, start_col + cuadrante_size):
            if tablero[i][j] == letra:
                return False

    return True

def resolver_sudoku(tablero, letras, letra_vacia):
    n = len(tablero)


    for i in range(n):
        for j in range(n):
            if tablero[i][j]==letra_vacia:
                for letra in letras:
                    if es_letra_valida(tablero, i, j, letra):

                        tablero[i][j] = letra
                        if resolver_sudoku(tablero, letras,letra_vacia):
                            return True

                        tablero[i][j] = letra_vacia

                return False


    return True


