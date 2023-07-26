#Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


lista = ['0-invalido','1- Segunda','2- Terca','3- Quarta','4- Quinta','5- Sexta','6- Sabado','7- Domingo']

dia= int(input("Digite um numero da semana: "))
print(lista[dia])

