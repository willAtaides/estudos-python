#6.	Um posto de combustível deseja gerenciar a preferência de produto por seus clientes. Para isto é solicitado um programa em Python que leia o código do combustível escolhido segundo a tabela abaixo:

qg=0
qa=0
qd=0
perg = str(input("Você deseja participar da nossa pesquisa?  \n Sim - s ou Não - n :  "))
while perg == 's' or perg == 'S':
    resp=int(input('Escolha um número referente a sua preferência:\n Gasolina=1\n Àlcool=2\n Diesel=3 \n Fim-4\n Responda: '))
    if resp ==1:
        qg=qg+1
    elif resp == 2:
        qa=qa+1
    elif resp == 3:
        qd=qd+1
    elif resp == 4:
        perg = 'n'
    else:
        print("opção inválida")
print('Muito obrigado pela participação! Sua pesquisa é muito valiosa para nossa empresa.')
print('Resultado da pesquisa: \n Gasolina= (%d)\n Àlcool= (%d) \n Diesel= (%d)'%(qg,qa,qd))