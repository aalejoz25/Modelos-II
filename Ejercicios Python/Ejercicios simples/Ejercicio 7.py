"""Escribir un programa que calcule el volumen de una esfera de radio = r
volumen de la esfera = 4/3 * PI * radio^3"""
import math

radio = float(input("Digite el radio de la esfera: "))

volumen = (4/3)*(math.pi)*pow(radio,3)

print("El volumen de la esfera es: ", volumen)
