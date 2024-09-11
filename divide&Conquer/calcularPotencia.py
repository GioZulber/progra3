"""
    Calcular a^n cuando n es una potencia de 2.
    Estrategia:
        Si n = 0, entonces a^n = 1
        Si n = 1, entonces a^n = a
        Si n es par, entonces a^n = (a^(n/2))^2 -> Esto se hace para simplificar las cuentas que debo 
        Si n es impar, entonces a^n = a*(a^(n-1)) -> 
        Lo pasas a par, lo resuelvo y luego lo multiplicas por a.
        Complejidad: O(log(n))
"""

def calcularPotencia(a, n):
    
    if n == 0: return 1
    
    if n == 1: return a
    
    if n % 2 == 0: return calcularPotencia(a, n//2) * calcularPotencia(a, n//2) # Divido n en 2 partes iguales, y luego multiplico el resultado de ambas partes.
    
    return a * calcularPotencia(a, n-1)


print(calcularPotencia(2, 10)) # 1024
print(calcularPotencia(3, 5)) # 243
print(calcularPotencia(5, 0)) # 1