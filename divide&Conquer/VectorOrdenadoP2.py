"""
    Dado un vectoir de N numeros naturales ordenados crecientemente,
    determinar si un numero dado X pertenece al vector.
"""

"""
    Estrategia:
        Primero divido el array en 2 partes, si el elemento en la mitad del array
        es igual a X, entonces retorno True, si no, si el elemento en la mitad del array
        es menor a X, entonces llamo recursivamente a la funcion con la mitad derecha del array,
        si no, llamo recursivamente a la funcion con la mitad izquierda del array.
        Si la longitud del array es 0, entonces retorno False.
        Si la longitud del array es 1, entonces retorno True si el unico elemento del array es igual a X,

        Teorema Maestro:
        A = 1, B = 2, C = 0
        n^C = 1
        A = B^C
        O(log(n))
""" 


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def estaEnVectorOrdenado(arr, x): # Costo: O(log(n))
        
        if(len(arr) == 0): return False
        
        if(len(arr) == 1): return arr[0] == x
        
        if(arr[len(arr)//2] == x): return True
        
        if(arr[len(arr)//2] < x): return estaEnVectorOrdenado(arr[len(arr)//2:], x)
        
        return estaEnVectorOrdenado(arr[:len(arr)//2], x)
    
    
def busquedaBinaria(arr, x): # Costo: O(log(n))
    izq = 0
    der = len(arr) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if arr[centro] == x:
            pos = centro
        elif arr[centro] < x:
            izq = centro + 1
        else:
            der = centro - 1
    return pos


print(estaEnVectorOrdenado(arr, 5)) # True
print(busquedaBinaria(arr, 5)) # 4
print(estaEnVectorOrdenado(arr, 11)) # False
print(busquedaBinaria(arr, 11)) # -1
