dividendo = int(input("digite el dividendo: "))
divisor = int(input("digite el divisor: "))

def div (n,m):
    if m>n:
        return 0
    return div((n-m),m)+1

print (div(dividendo,divisor))

input()
