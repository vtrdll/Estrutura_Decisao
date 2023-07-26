#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


numero = int(input("Digite um numero maior que 1000: ")) #326

centena = numero // 100 
subtracao = centena * 100 #aqui estamos criando a centena
if centena > 1:
    print("centenas",centena)
else:
    print("centena" ,centena)


subtracao1 = numero - subtracao #estamos extraindo a dezena 
dezena = subtracao1 //10
if dezena > 1:
    print("dezenas ",dezena)
else:
    print("dezena ",dezena)




subtracao2 =  dezena * 10
unidade = subtracao1 - subtracao2 #estamos extraindo a unidade
if unidade > 1:
    print("unidades",unidade)
else:
    print("unidade",unidade)




