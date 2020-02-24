"""Escribir un programa que genere las tablas de multiplicar
de un número introducido por el teclado."""

x = int(input("Digite un numero entero: "))

print("Tabla de multiplicar de ",x,": ")

for i in [0,1,2,3,4,5,6,7,8,9]:
    print(x*i)
