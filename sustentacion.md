# Proyecto Final
### Explicacion del siguiente algoritmo.

El codigo ubicado en el Main cuenta a su vez con cuatro modulos externos de procesamiento.

checker.py
Este modulo esta encargado de la validación de un sudoku, el checker automáticamente detecta cual es la longitud y base N del sudoku, luego revisa por símbolos repetidos. El programa no esta limitado a sudokus de strings de números ya que el procesamiento se hace para símbolos en general. Ingresar un sudoku vació o incompleto arrojara False.

sudokureader.py
Este modulo se encarga de la lectura y escritura de sudokus. La función ```lecsud()``` recibe de parametro un string de longitud n y analiza cual es la base del sudoku junto con la longitud de sus cadenas. Luego retorna una matriz cuadrada. La función ```drawsud()``` recibe una matriz y la convierte en un string.

sudokugenerator.py
Aqui se generan sudokus de base 3. Primero se genera un sudoku aleatorio completamente lleno. Luego se hacen ```n*n *pct ```eliminaciones aleatorias de casillas. Finalmente se transcribe el sudoku a su forma de string y se retorna.

solver.py
Este modulo se encarga de resolver sudokus mediante backtracking. Para resolver un sudoku se debe definir cuales son los símbolos con los que trabaja y cual símbolo representa un espacio vacío. Debido a esto, la resolución de sudokus no esta limitada a números.

main.py
Aqui se ejecuta el programa, el usuario tiene tres opciones para elegir.
1. **Validar un sudoku**: Aquí el modulo checker analiza un string para determinar si es un sudoku valido.
2. **Resolver un sudoku**: Se ingresa un string, este es leido por el modulo del reader. Se procede a calcular la base N y la cantidad de simbolos que tiene. Se ingresan los numeros a una lista y se redefinen a strings. Luego se define el simbolo vacio y se envian todos los parametros al solver. El solver determina si hay o no una solucion e imprime el sudoku.
3. **Generar un sudoku**: Se genera un string que representa un Sudoku de base 3.



**Analisis del problema**
Dada la falta de heuristicas se puede determinar que en el peor de los casos el algoritmo de resolucion recorrera todas las rutas posibles hasta llegar a la correcta, la cual seria la ultima. Para bases de 5 hacia arriba el programa es demasiado lento para ser considerado.
> Alejandro Quintero M.

