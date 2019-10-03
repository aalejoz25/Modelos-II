b = int(input("Digite la base: "))
p = int(input("Digite la potencia: "))

def pot(n,m):
    if m==0:
        return 1
    if m==1:
        return n
    return pot(n,m-1)*n


print (pot(b,p)) 

input()
