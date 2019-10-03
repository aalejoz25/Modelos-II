def listaOrden(list):
    if(list==[]):
        return True
    if(list[1::]==[]):
        return True
    if((list[:1]<=list[1:2])&listaOrden(list[1::])):
            return True
    return False

a=[1,2,3,4,5,6,7,8,9,10]
b=[5,4,1,2,3,33,15,8]
print(listaOrden(a))
print(listaOrden(b))
