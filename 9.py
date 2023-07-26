#Faça um Programa que leia três números e mostre-os em ordem decrescente


lista = [] 
num1 = int(input("Digite o primeiro numero: "))
lista.append(num1)
num2 = int(input("Digite o segundo numero: "))
lista.append(num2)
num3 = int(input("Digite o terceiro numero: "))
lista.append(num3)
lista.sort()
lista.reverse()

print(lista)

