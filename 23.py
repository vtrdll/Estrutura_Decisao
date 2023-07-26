#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.



num = float(input("Digite um valor: "))


if num < 1:
   print("%.2f numero decimal" %num)
else:
    round(num)
    print("%i numero inteiro" %num)
    


