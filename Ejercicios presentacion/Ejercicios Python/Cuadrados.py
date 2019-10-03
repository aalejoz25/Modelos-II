def cuadrados(list):
    if(list==[]):
        return []
    list[0]=list[0]*list[0]
    return [list[0]]+cuadrados(list[1::])

lista1 = [9,8,5,3,1];
print(cuadrados(lista1))
