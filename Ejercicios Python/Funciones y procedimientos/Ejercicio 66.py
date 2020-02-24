"""Escribir un programa que calcule el factorial de un numero leído desde el teclado usando
funciones"""

x=int(input("Digite un numero entero:"))

def factorial(n):
    resultado = 1
 
    for i in range(n):
        resultado *= (i + 1)
 
    return resultado

fact = factorial(x)
print("El factorial de",x,"es", fact)
