#funcion division
def div (n,d):
    resultado = int(0)
    if d>n:
        return 0
    else:
        while n>=d:            
            n -=d
            resultado += 1
    return resultado         

#funcion fibonacci
def Fiboit(n):
    i = int (0)
    j = int (1)
    for k in range (n):
        m = i+j
        i = j
        j = m
    return j

#funcion potencia
def pot (b,e):
    resultado = float(1.0)
    for i in range (e):        
        resultado = resultado * b
    return resultado


if __name__ == "__main__":
    dividendo = int(input("Digite el dividendo: "))
    divisor = int(input("Digite el divisor: "))
    print (div(dividendo,divisor))
    num = int(input("digite una posicion de la sucesion de fibonacci: "))
    print (Fiboit(num))
    base = float(input("digite la base: "))
    exponente = int(input("digite el exponente: "))
    print (pot(base,exponente))

    
        
