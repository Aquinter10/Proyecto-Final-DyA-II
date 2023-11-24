import checker as ch
import sudokureader as sd
import solver as sv
import math
import time
import sudokugenerator as sg
def main():
    print(f"Escoge una opcion: \n1. Validar un Sudoku.\n2. Resolver un Sudoku \n3. Generar un Sudoku")
    choice=int(input())
    if choice==1:
        sudoku= input("Ingrese el sudoku: ")
        z=sd.lecSud(sudoku)
        print( ch.check(z))
    if choice == 2:
        sudoku = input("Ingrese el sudoku: ")
        inicio= time.time()
        z = sd.lecSud(sudoku)
        n=sd.getNsize(sudoku)
        if n==0:
            print("SUDOKU INVALIDO")
            return
        charsize= int(math.log(n ** 2, 10) + 1)
        lista_numeros = list(range(len(z)+1))
        lista = list(map(lambda x: sd.reDefNum(x, charsize), lista_numeros))

        letras_posibles = lista[1:]
        letra_vacia = lista[0]
        print(letras_posibles)
        print(letra_vacia)
        if sv.resolver_sudoku(z, letras_posibles,letra_vacia):
            print("\nSolución:")
            sv.imprimir_tablero(z)
        else:
            sv.imprimir_tablero(z)
            print("No hay Solucion")
        end=time.time()
        print(end-inicio)

    if choice == 3:
        print(sg.retornarSudokuString())

main()
