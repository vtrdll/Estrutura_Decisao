#Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


turno = input("Digite o turno que voce estuda: M-matutino / V-Vespertino / N- Noturno: ")

if turno == 'M' or turno == 'Matutino':
    print("Bom dia!")
elif turno == 'V' or turno == 'Vespetino':
    print("Boa tarde!")
elif turno == 'N' or turno == 'Noturno':
    print("Boa noite!")
else:
    print("VALOR INVALIDO!")
