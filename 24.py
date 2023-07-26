#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#1 par ou ímpar;
#2 positivo ou negativo;
#3 inteiro ou decimal.



num1 = float(input("digite um valor: "))
num2 = float(input("digite um valor: "))

operacao = input("QUAL OPERACAO DESEJA REALIZAR: \n1) par ou ímpar;  \n2) positivo ou negativo; \n3) inteiro ou decimal                  \n:    ")
print()
#PAR OU IMPAR
if operacao == '1':
    print("voce escolheu PAR ou IMPAR! ")
    print()
    par_num1 = num1 % 2
    par_num2 = num2 % 2
    if par_num1 >0:
            print(num1,"IMPAR")
    if par_num2 > 0:
            print(num2,"IMPAR")
    if par_num1 == 0: 
            print(num1,"PAR")
    if par_num1 == 0:
            print(num2,"PAR")


#POSITIVO OU NEGATIVO
if operacao == '2':
    print("Voce escolheu POSITIVO OU NEGATIVO! ")
    if num1 < 0:
        print(num1, "NEGATIVO")
    if num2 < 0:
        print(num2, "NEGATIVO")
        
    if num1 >= 0:
        print(num1, "POSITIVO")
    if num2 >= 0:
        print(num2, "POSITIVO")


#INTEIRO OU DECIMAL
if operacao == '3':
    print("Voce escolheu INTEIRO OU DECIMAL! ")
    print()
    if num1 % 1 == 0:
        print(num1,"INTEIRO")
    if num2 % 1 == 0:
        print(num2,"INTEIRO")
    if num1 % 1 >0 or num1 % 1 < 0:
        print(num1,"DECIMAL")
    if num2 % 1 >0 or num2 % 1 < 0:
        print(num2,"DECIMAL")
