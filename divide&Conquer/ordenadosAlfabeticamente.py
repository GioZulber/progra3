
# Algoritmo 1: estaOrdenadoAlfabeticamente(string)
"""
    La funcion recibe un string, esta toma los primeros 2 carecteres y los compara, si el primer caracter es menor o igual
    al segundo, entonces se llama recursivamente a la funcion con el string sin el primer caracter, si no, entonces se retorna
    False. Si la longitud del string es 1, entonces se retorna True.
"""
def estaOrdenadoAlfabeticamente(string): 
    
    if(len(string) == 1): return True    # Caso base  
    
    else: 
        if string[0] <= string[1]:  
            return estaOrdenadoAlfabeticamente(string[1:]) 
        else:
            return False 
        
print(estaOrdenadoAlfabeticamente("abc")) # True 

# Complejidad: O(n) donde n es la longitud de la cadena de caracteres.



    
