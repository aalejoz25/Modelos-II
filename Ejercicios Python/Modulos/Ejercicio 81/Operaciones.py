resultado = 0

def suma (x,y):
    print(x+y)

def resta (x,y):
    print(x-y)

def multiplicacion (x,y):
    print(x*y)

def division (x,y):
    print(x/y)

def potencia (x,y):
    if (y == 0):
        return 1
    else:
        resultado = x*potencia(x,y-1)
        return resultado
