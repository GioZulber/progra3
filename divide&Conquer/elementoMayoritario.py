"""
    Dado un array A de num. enteros, calcular elemento mayoritario.
    Si se tiene un vector A de n enteros, un elemento X se denomina mayopritario
    de A si X aparece en el vector A mas de N/2 veces. 
    Considerar que no puede haber mas de un elemento mayoritario.
"""

# Estrategia:
"""
    Divido el array a la mitad hasta que la longitud del array sea 2, luego 
    comparo los elementos del array, si son iguales, entonces retorno ese elemento,
    como el elemento mayoritario, si no, retorno None.
    Luego lo que hago es comparar el elemento mayoritario de la mitad izquierda del array
    con el elemento mayoritario de la mitad derecha del array, si son iguales, entonces
    retorno ese elemento.
    Si uno de los elementos es None, entonces retorno el otro elemento.
    Si ninguno de los elementos es None, entonces cuento cuantas veces aparece el elemento
"""


"""
    Teorema Maestro:
    A = 2, B = 2, C = 0
    2 > 1 -> O(n^log(2,2)) = O(n)
"""

def mayoritario(arr, ini, fin):
    if ini - fin == -1: # Caso base, si la longitud del array es 2
        if arr[ini] == arr[fin]:
            return arr[ini]
        else:
            return None
    else:
        medio = (ini + fin) // 2
        izq = mayoritario(arr, ini, medio)
        der = mayoritario(arr, medio + 1, fin)
        if izq == der: # Puede ser None o un elemento
            return izq
        else:
            if izq == None:
                return der
            elif der == None:
                return izq
            else:
                return None

            
vector = [1,0,0,1,0,1,1,1]

print(mayoritario(vector, 0, len(vector) - 1)) # 1