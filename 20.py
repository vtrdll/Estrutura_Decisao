#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.



nota1 = int(input("Digite a sua PRIMEIRA nota: "))
nota2 = int(input("Digite a sua SEGUNDA nota: "))
nota3 = int(input("Digite a sua TERCEIRA nota: "))


media =  nota1 + nota2 + nota3 / (3)

if media >= 7:
    print("%.1f APROVADO! "%media)


elif media < 7:
    print("%.1f REPROVADO! "%media)

elif media == 10:
    print("%.1f APROVADO COM DISTINCAO! "%media)
    
