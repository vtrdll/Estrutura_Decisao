#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#preço do litro do álcool é R$ 1,90

#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro
#preço do litro da gasolina é R$ 2,50


#escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#calcule e imprima o valor a ser pago pelo cliente 


combustivel = input("Voce vai utilizar A-alcool ou G-gasolina: ")
litros = int(input("Quantos litros voce precisa? "))



if combustivel == 'G':
    print("preço do litro da gasolina é R$ 2,50")
    print()
    if litros == 20:
        desconto = 20 * (4/100)
        desconto *=20
        pagar = 20 * 2.5
        print("Valor sem desconto: R$ %.2f" %pagar)
        print("Valor desconto: R$ %.2f" %desconto)
        pagar -=desconto
        print("Valor total: R$ %.2f" %pagar)

    if litros > 20:
        desconto = 20 * (6/100)
        desconto *=20
        pagar = 20 * 2.5
        print("Valor sem desconto: R$ %.2f" %pagar)
        print("Valor desconto: R$ %.2f" %desconto)
        pagar -=desconto
        print("Valor total: R$ %.2f" %pagar)


if combustivel == 'A':
    print("preço do litro do álcool é R$ 1,90")
    print()
    if litros == 20:
        desconto = 20 * (3/100)
        desconto *=20
        pagar = 20 * 1.9
        print("Valor sem desconto: R$ %.2f" %pagar)
        print("Valor desconto: R$ %.2f" %desconto)
        pagar -=desconto
        print("Valor total: R$ %.2f" %pagar)

    if litros > 20:
        desconto = 20 * (5/100)
        desconto *= 20
        pagar = 20 * 1.9
        print("Valor sem desconto: R$ %.2f" %pagar)
        print("Valor desconto: R$ %.2f" %desconto)
        pagar -=desconto
        print("Valor total: R$ %.2f" %pagar)

    
        
        
        


    



