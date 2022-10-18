#4.	Faça um programa em Python que leia um conjunto indeterminado de dados, contendo cada um a idade de um indivíduo, e calcule e imprima a média de idades do grupo. O último dado, que não entrará no cálculo da média deve ser um valor negativo.

arm=0
quant=0
perg=int(input('informe a idade\n se desejar parar, informe um número negativo!\n Idade: '))
while perg > 0 :
    arm=arm+perg  
    quant=quant+1
    perg=int(input('informe a idade\n se desejar parar, informe um número negativo!\n Idade:'))
media= arm/quant
print("a média de idade do grupo é igual:",media)