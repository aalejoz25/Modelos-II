"""Escriba un programa que calcule el factorial de un numero usando recursividad."""

x = int(input("Digite un numero entero: "))

def factorialrec(n):
    if (n==0):
        return 1
    else:
        return n*factorialrec(n-1)


factorial= factorialrec(x)
print("El factorial de",x,"es",factorial)
