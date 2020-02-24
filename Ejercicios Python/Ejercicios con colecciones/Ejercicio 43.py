"""Escribir un programa que llene una lista con los veinte
primeros números pares y calcule su suma."""

numeros=[]
suma = 0
p=0

for i in range(500):            
    numeros.append(p)
    p += 2
    if (len(numeros)==20):
        break
    

for num in numeros:
    suma = suma + num

print("Lista: ",numeros)
print("Suma de sus elementos: ",suma)




            
            

        
        
            
            
        
    
