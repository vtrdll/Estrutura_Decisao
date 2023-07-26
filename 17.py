#Faça um Programa que peça um número correspondente a
#um determinado ano e em seguida informe se este ano é ou não bissexto.


ano = int(input("Digite um ano: "))

teste = ano % 2
if teste > 0:
    print("NÃO É BISSEXTO")
else:
    print("É BISSEXTO")
