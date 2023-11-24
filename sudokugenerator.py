import random
import sudokureader as sd
def imprimir_sudoku(sudoku):
    for fila in sudoku:
        print(" ".join(map(str, fila)))

def generar_sudoku_aleatorio():
    simbolos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    sudoku = [["-" for _ in range(9)] for _ in range(9)]

    def es_valido(fila, columna, simbolo):

        if simbolo in sudoku[fila] or simbolo in [sudoku[i][columna] for i in range(9)]:
            return False


        bloque_fila_inicio, bloque_columna_inicio = 3 * (fila // 3), 3 * (columna // 3)
        bloque = [sudoku[i][bloque_columna_inicio:bloque_columna_inicio + 3] for i in range(bloque_fila_inicio, bloque_fila_inicio + 3)]
        if simbolo in [s for sublist in bloque for s in sublist]:
            return False

        return True

    for fila in range(9):
        for columna in range(9):
            simbolos_posibles = list(simbolos)
            random.shuffle(simbolos_posibles)

            for simbolo in simbolos_posibles:
                if es_valido(fila, columna, simbolo):
                    sudoku[fila][columna] = simbolo
                    break

    return sudoku

def retornarSudokuString():
    sudoku_aleatorio = generar_sudoku_aleatorio()


    pct=1
    n=9
    for _ in range(int(n*n*pct)):
        sudoku_aleatorio[random.randint(0, n-1)][random.randint(0, n-1)]="-"

    new=sd.drawsud(sudoku_aleatorio)
    return new

