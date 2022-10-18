#1.	Faça um programa que calcule e apresente o valor da hipotenusa “c” de um triângulo retângulo, dado o valor de seus catetos “a” e “b”, segundo a fórmula:
import math
catad=int(input('informe o cateto ad: '))
catop=int(input('informe o cateto op: '))
hip= math.sqrt (catad**2 + catop**2)
print(hip)