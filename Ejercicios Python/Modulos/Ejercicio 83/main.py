import Binario

x=input("Digite un numero binario: ")
y=input("Digite otro numero binario: ")

xDec = Binario.convertir_a_decimal(x)
yDec = Binario.convertir_a_decimal(y)

suma = Binario.sumar(xDec,yDec)
resta = Binario.restar(xDec,yDec)
producto = Binario.multiplicar(xDec,yDec)
division = Binario.dividir(xDec,yDec)

print("Resultado suma",Binario.convertir_a_binario(suma))
print("Resultado resta",Binario.convertir_a_binario(resta))
print("Resultado producto",Binario.convertir_a_binario(producto))
print("Resultado division",Binario.convertir_a_binario(division))




