#Faça um Programa que leia três números e mostre o maior deles.


num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))


if num1 > num2 and num1 > 3:
    print("o maior numero: ",num1)
elif num2 > num1 and num2 > num3:
    print("o maior numero: ",num2)
elif num3 >num1 and num3 >num2:
    print("o maior numero: ",num3 )
