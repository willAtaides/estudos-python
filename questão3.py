#3.	Faça um programa em Python que leia um número inteiro N menor que 1.000 e apresente todos os números ímpares de 1 a N, inclusive N 
n=int(input('Informe um número: '))
a=0
if n > 0 and n < 1000:
    while a <= n :
        if a % 2 == 1:
            print(a)
        a+=1