base = float(input("digite la base: "))
exponente = int(input("digite el exponente: "))


def pot (b,e):
    resultado = float(1.0)
    for i in range (e):        
        resultado = resultado * b
    return resultado

print (pot(base,exponente))
        
input() 
