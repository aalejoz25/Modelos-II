num = int(input("digite un numero entero: "))

def Fiboit(n):
    i = int (0)
    j = int (1)
    for k in range (n):
        m = i+j
        i = j
        j = m
    return j

print (Fiboit(num))

input ()
