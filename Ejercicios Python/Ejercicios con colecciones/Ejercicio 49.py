"""Escribir un programa que determine la posición
de una matriz de 3x3 en la que se encuentra el valor
máximo de una serie de números generados aleatoriamente."""

import random
 
d=3
matriz=[[0 for x in range(d)] for y in range(d)]
for i in range (0,d):
    for j in range (0,d):
        matriz[i][j]=int(random.randint(0,1500))
print(matriz)


mayor = matriz[i][j]

for i in range(len(matriz)):
    for j in range (len(matriz[i])):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]

print(mayor)
