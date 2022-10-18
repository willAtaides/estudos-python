#2.	Faça um programa que leia os 3 lados de um triangulo e determine se ele é um triangulo retângulo. Para isto utilize a fórmula do item anterior nesta checagem.

a=int(input('informe o cateto a: '))
b=int(input('informe o cateto b: '))
c=int(input('informe o cateto c: '))

if a > b and a>c:
    hipo = a
    catad = b
    catop = c
elif b > a and b>c:
    hipo = b
    catad = a
    catop = c
else:
    hipo = c
    catad = a
    catop = b

if hipo**2 == (catad**2 + catop**2):
    print('Os lados %d, %d e %d formam um triângulo retângulo!'%(a,b,c))

else:
    print('Os lados %d, %d, %d não formam um triângulo retângulo!'%(a,b,c))


