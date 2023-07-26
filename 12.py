#Faça um programa para o cálculo de uma folha de pagamento,
#sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o #FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
#O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%
#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#       Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00


hora = int(input("Digite quantas horas voce trabalha no mes: "))
ganho = float(input("Digite quanto voce ganha por hora: "))

salario = ganho * hora

#ate 1500 
ir5 =  5 / 100

#ate 2500
ir10 = 10 / 100

#acima 2500
ir20 = 20/ 100


inss = 10 / 100 


fgts = 11 / 100


if salario <= 900:
    print("ISENTO")
    
elif salario >900 and salario <= 1500:
        print("Salario bruto: R$ %.2f"%salario)
        desconto_ir = ir5 * salario
        print("(-) IR                    : R$ %.2f"%desconto_ir)
        
        desconto_inss = inss * salario
        print("(-) INSS                  : R$ %.2f"%desconto_inss)
        
        desconto_fgts = fgts * salario
        print("FGTS                      : R$ %.2f"%desconto_fgts)
        
        total_desconto = desconto_inss + desconto_ir
        print("Total de descontos        : R$ %.2f"%total_desconto)

        salario_liquido = salario - total_desconto
        print("Salario liquido           :R$ %.2f"%salario_liquido)

elif salario > 1500 and salario <=2500:
        print("Salario bruto: R$ %.2f"%salario)
        desconto_ir = ir10 * salario
        print("(-) IR                    : R$ %.2f"%desconto_ir)
        
        desconto_inss = inss * salario
        print("(-) INSS                  : R$ %.2f"%desconto_inss)
        
        desconto_fgts = fgts * salario
        print("FGTS                      : R$ %.2f"%desconto_fgts)
        
        total_desconto = desconto_inss + desconto_ir
        print("Total de descontos        : R$ %.2f"%total_desconto)

        salario_liquido = salario - total_desconto
        print("Salario liquido           :R$ %.2f"%salario_liquido)

elif salario > 2500:
        print("Salario bruto: R$ %.2f"%salario)
        desconto_ir = ir20 * salario
        print("(-) IR                    : R$ %.2f"%desconto_ir)
        
        desconto_inss = inss * salario
        print("(-) INSS                  : R$ %.2f"%desconto_inss)
        
        desconto_fgts = fgts * salario
        print("FGTS                      : R$ %.2f"%desconto_fgts)
        
        total_desconto = desconto_inss + desconto_ir
        print("Total de descontos        : R$ %.2f"%total_desconto)

        salario_liquido = salario - total_desconto
        print("Salario liquido           :R$ %.2f"%salario_liquido)

    



