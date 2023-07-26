#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" +
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#Caso contrário, ele será classificado como "Inocente".



lista = []
pergunta1 = input("Telefonou para a vitima? ")
if pergunta1 == 'sim':
    lista.append('sim')
pergunta2 = input("Esteve no local do crime? ")
if pergunta2 == 'sim':
    lista.append('sim')
pergunta3 = input("Mora perto da vitima? ")
if pergunta3 == 'sim':
    lista.append('sim')
pergunta4 = input("Devia para a vitima? ")
if pergunta4 == 'sim':
    lista.append('sim')
pergunta5 = input("Ja trabalhou com a vitima? ")
if pergunta5 == 'sim':
    lista.append('sim')

veredito = len(lista)
print()
if veredito == 2:
    print("SUSPEITA")
if veredito == 3 or veredito == 4:
    print("CUMPLICE")
if veredito == 5:
    print("ASSASINO")
