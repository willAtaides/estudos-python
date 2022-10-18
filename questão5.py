#5.	Faça um programa em Python que leia um número inteiro “N”, calcule e apresente todos os seus divisores. (Dica: use uma estrutura while para testar todos os possíveis divisores)

n=int(input('informe um número: '))
o=1
while o<=n:
    div= n % o
    if div == 0:
        print(o)
    o+=1