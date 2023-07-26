#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
#O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.



deposito = float(input("Digite o valor que deseja depositar: "))#256

centena =  deposito //100 # 2 
print("%i notas de 100 "%centena)


sub = centena * 100 #200
dezena = deposito - sub #56

notas_10 = (dezena % 50) // 10
notas_50 = dezena // 50

print("%i notas de R$ 10,00" %notas_10)

print("%i notas de R$ 50,00" %notas_50)








dezena2 = dezena // 10 #5

sub1 = dezena2 * 10 #50

unidade =  dezena - sub1 #6



notas_1 = unidade % 5
notas_5 = unidade // 5


print("%i notas de R$ 1,00" %notas_1)
print("%i notas de R$ 5,00" %notas_5)
    





