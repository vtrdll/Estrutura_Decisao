
#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))
if dia > 0 and dia < 31:
    print()

elif mes > 0 and mes < 12:
    print() 

else:
    print("DATA INVALIDA! ")

