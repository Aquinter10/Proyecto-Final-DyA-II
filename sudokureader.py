# Este modulo esta encargado de la lectura de un sudoku en su forma de String.
import math

# Esta funcion determina el valor de N leyendo la longitud de la cadena. Si la longitud no coincide
# con ningun valor valido de N entonces se devuelve 0 y el sudoku esta mal hecho.
def getNsize(sudoku_string):
    n = 1
    while True:
        size = int(math.log(n**2, 10)+1)
        if len(sudoku_string) == (n**4)*size:
            return n

        else:
            n += 1
        if n > len(sudoku_string):
            return 0


# Funcion para leer un sudoku a partir de un string y generar su respectiva matriz.
def lecSud(sud):
    n= getNsize(sud)
    if n==0:
        return []
    charzise = int(math.log(n ** 2, 10) + 1)
    newsud=[]
    counter=0
    for i in range(n**2):
        newsud.append([])
    for i in newsud:
        for j in range(n**2):
            i.append(sud[counter*charzise:(counter+1)*charzise])
            counter+=1
    return newsud

# Funcion para convertir un sudoku a un string.
def drawsud(sudoku):
    sudoku_string=""
    for i in sudoku:
        for j in i:
            sudoku_string+=j
    return sudoku_string


def reDefNum(num, charzise):
    num = str(num)
    if num != "0":
        while len(num) != charzise:
            num = "0" + num
        return num
    else:
        num = "-"
        for _ in range(charzise - 1):
            num = num + "-"
        return num

