#Faça um Programa que peça os 3 lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;



lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite  a base: "))




if  lado3 == lado1 and lado3 == lado2:
    print("Triângulo Equilátero! ")
elif lado1 == lado2:
    print("Triângulo Isósceles! ")
else:
    print("Triângulo Escaleno! ")
    
    
