

#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
 #                     Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
 #

#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.#
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.



quantidade_morango = int(input("Digite a quantidade em KG de MORANGOS: "))
quantidade_maca = int(input("Digite a quantidade em KG de maca: "))

if quantidade_morango < 5:
    preco = quantidade_morango * 2.5
else:
    preco = quantidade_morango * 2.2


if quantidade_maca < 5:
    preco = quantidade_maca * 1.8
else:
    preco = quantidade_maca * 1.5


print()
if quantidade_morango + quantidade_maca >= 8 or preco >= 25:
    desconto = 10/100
    desconto = desconto * preco
    preco_final = preco - desconto
    print("VALOR: R$ %.2f" %preco)
    print()
    print("Voce ira pagar COM DESCONTO: R$ %.2f" %preco_final )
else:
    print("Voce ira pagar SEM DESCONTO: R$ %.2f "%preco)
    

