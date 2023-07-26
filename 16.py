#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;




a = float(input("Digite um valor: "))
if a > 0: 
    b = float(input("Digite um valor: "))
    c = float(input("Digite um valor: "))
else:
    print("VALOR INCORRETO! ")




delta = (b**2) - 4 *(a)*(c)

if delta < 0:
    print("A equacao nao possui raizes reais. ")
    print("O programa sera encerrado! ")
if delta == 0:
    print("A equacao possui apenas uma raiz real!")
if delta > 0:
    print("A equacao possui duas raiz reais!")
