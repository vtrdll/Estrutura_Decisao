#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).


num = int(input("Digite um numero: "))

num %= 2

if num == 0:
    print("Numero par")
else:
    print("numero impar")
