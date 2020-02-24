"""Escribir un programa que calcule la potencia de un numero usando recursividad."""

b = int(input("Digite la base: "))
e = int(input("Digite el exponente: "))

def potenciarec (base, exponente):
    if (exponente == 0):
        return 1
    else:
        return base*potenciarec(base,exponente-1)

resultado = potenciarec(b,e)

print(resultado)
