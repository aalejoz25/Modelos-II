dividendo = int(input("Digite el dividendo: "))
divisor = int(input("Digite el divisor: "))


def div (n,d):
    resultado = int(0)
    if d>n:
        return 0
    else:
        while n>=d:            
            n -=d
            resultado += 1
    return resultado
    
            
print (div(dividendo,divisor))
