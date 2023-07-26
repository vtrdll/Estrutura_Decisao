#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.



salario = float(input("Digite o valor do seu salario R$ "))

aumento20 =20 / 100
aumento15 = 15 / 100
aumento10 = 10 / 100
aumento5 = 5/ 100

if salario < 280 or salario == 280:
    acressimo = aumento20 * salario
    salario_alterado = salario + acressimo
    print("salário antes do reajuste: R$ %.2f"%salario)
    print("percentual de aumento: %.2f "%aumento20)
    print("o valor do aumento: R$ %.2f" %acressimo)
    print("O novo salario, apos o aumento: R$ %.2f" %salario_alterado)
    
elif salario > 280 and salario <= 700:
    acressimo = aumento15 * salario
    salario_alterado = salario + acressimo
    print("salário antes do reajuste: R$ %.2f"%salario)
    print("percentual de aumento: %.2f "%aumento15)
    print("o valor do aumento: R$ %.2f" %acressimo)
    print("O novo salario, apos o aumento: R$ %.2f" %salario_alterado)
    
elif salario > 700 and salario <= 1500:
    acressimo  = aumento10 * salario 
    salario_alterado = salario + acressimo
    print("salário antes do reajuste: R$ %.2f"%salario)
    print("percentual de aumento: %.2f "%aumento10)
    print("o valor do aumento: R$ %.2f" %acressimo)
    print("O novo salario, apos o aumento: R$ %.2f" %salario_alterado)
    
elif salario > 1500:
    acressimo = aumento5 * salario
    salario_alterado = salario + acressimo
    print("salário antes do reajuste: R$ %.2f"%salario)
    print("percentual de aumento: %.2f "%aumento5)
    print("o valor do aumento: R$ %.2f" %acressimo)
    print("O novo salario, apos o aumento: R$ %.2f" %salario_alterado)
   
