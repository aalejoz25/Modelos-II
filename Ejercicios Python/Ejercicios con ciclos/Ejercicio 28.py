"""Escribir un programa que visualice en pantalla los números pares entre 1 y 25."""
x= int(1)

for i in range(24):
    if(x%2==0):
        print(x)
    x += 1
