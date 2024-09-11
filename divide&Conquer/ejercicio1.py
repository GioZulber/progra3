"""
    Ejercicio 1: Me dan una lista de enteros con infinitos valores, estos son coordenadas en el plano cartesiano, x e y,
    donde buscamos encontrar el valor de x cuando y es igual a 0.
    
    Vamos a buscar primero que nada un intervalo donde se pueda realizar una busqueda binaria, para esto vamos a buscar
    el valor de y cuando sea positivo y negativo, si encontramos un valor de y positivo y uno negativo, entonces podemos
    realizar una busqueda binaria en ese intervalo ya que sabemos que en ese intervalo hay un valor de y = 0. Si no se
    encuentra un valor de y positivo y uno negativo, entonces no se puede realizar una busqueda binaria y se debe continuar 
    buscado en el inicio 2**k donde k es un valor que se incrementa en 1 cada vez que no se encuentra un valor de y positivo
    y uno negativo.
"""


    