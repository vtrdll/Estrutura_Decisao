#Faça um programa que pergunte o preço de três produtos e
#informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


preco1 = float(input("Digite o valor do primeiro produto R$ "))
preco2 = float(input("Digite o valor do segundo produto R$ "))
preco3 = float(input("Digite o valor do terceiro produto R$ "))


if preco1 < preco2 and preco1 < preco3:
    print("O produto mais barato sera: R$ %.2f"%preco1 )
elif preco2 < preco1 and preco2 < preco3:
    print("O produto mais barato sera: R$ %.2f"%preco2)
elif preco3 < preco2 and preco3 < preco1:
    print("O produto mais barato sera: R$ %.2f "%preco3)
