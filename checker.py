import  sudokureader as sd

def check(sudoku):
    def checkline(linea):
        return len(set(linea)) == n and '0' not in linea

    def getsquare(fila_inicio, columna_inicio):
        return [sudoku[i][j] for i in range(fila_inicio, fila_inicio + raiz_cuadrada) for j in range(columna_inicio, columna_inicio + raiz_cuadrada)]

    n = len(sudoku)
    raiz_cuadrada = int(n ** 0.5)


    if raiz_cuadrada * raiz_cuadrada != n:
        return False

    for i in range(n):
        if not checkline(sudoku[i]) or not checkline(sudoku[j][i] for j in range(n)):
            return False


    for i in range(0, n, raiz_cuadrada):
        for j in range(0, n, raiz_cuadrada):
            subgrid = getsquare(i, j)
            if not checkline(subgrid):
                return False

    return True

