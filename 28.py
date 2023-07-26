#Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
#Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
#Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
#contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.





tipo_carne = input("Qual tipo de carne deseja:   \n1) File Duplo \n2)Alcatra \n3)Picanha \n:")
kilos = int(input("Quantos kilos: "))
forma_pag = input("Voce ira pagar no cartao ? ")

#tipo de carne FILE DUPLO
if tipo_carne == '1' and kilos <=5:
    preco = kilos * 4.9
    if forma_pag == 'sim':#com desconto
        desconto = preco * (5/100)
        preco_desc = preco - desconto
        print("tipo de carne selecionado  :File Duplo  ")
        print("Forma de pagamento         :Cartao Tabajara! ")
        print("Quantidade de carne        :%i KILOS "%kilos)
        print()
        print("Preco Total:              R$ %.2f"%preco)
        print("Valor Desconto:           R$ %.2f" %desconto)
        print("Valor a pagar:            R$ %.2f" %preco_desc)

    if form_pag =='nao': #sem desconto
        print("tipo de carne selecionado  :File Duplo  ")
        print("Quantidade de carne        :%i KILOS "%kilos)
        print()
        print("Valor a pagar              :R$ %.2f"%preco)
       

if tipo_carne == '1' and kilos > 5:
    preco = kilos *5.8
    if forma_pag == 'sim':
        desconto = preco * (5/100)
        preco_desc = preco - desconto
        print("tipo de carne selecionado  :File Duplo  ")
        print("Forma de pagamento         :Cartao Tabajara! ")
        print("Quantidade de carne        :%i KILOS "%kilos)
        print()
        print("Preco Total:              R$ %.2f"%preco)
        print("Valor Desconto:           R$ %.2f" %desconto)
        print("Valor a pagar:            R$ %.2f" %preco_desc)
        
    if form_pag =='nao':
        print("tipo de carne selecionado  :File Duplo  ")
        print("Quantidade de carne        :%i KILOS "%kilos)
        print()
        print("Valor a pagar              :R$ %.2f"%preco)



       

        
        
    #ALCATRA <5KG
if tipo_carne == '2' and kilos <=5:
    preco = kilos * 5.9
    if forma_pag == 'sim':#com desconto
        desconto = preco * (5/100)
        preco_desc = preco - desconto
        print("tipo de carne selecionado  :ALCATRA  ")
        print("Forma de pagamento         :Cartao Tabajara! ")
        print("Quantidade de carne        :%i KILOS "%kilos)
        print()
        print("Preco Total:              R$ %.2f"%preco)
        print("Valor Desconto:           R$ %.2f" %desconto)
        print("Valor a pagar:            R$ %.2f" %preco_desc)

    if forma_pag =='nao': #sem desconto
        print("tipo de carne selecionado  :ALCATRA  ")
        print("Quantidade de carne        :%i KILOS "%kilos)
        print()
        print("Valor a pagar              :R$ %.2f"%preco)
       
    #ALCATRA >5KG
if tipo_carne == '2' and kilos > 5:
    preco = kilos *6.8
    if forma_pag == 'sim':
        desconto = preco * (5/100)
        preco_desc = preco - desconto
        print("tipo de carne selecionado  :ALCATRA  ")
        print("Forma de pagamento         :Cartao Tabajara! ")
        print("Quantidade de carne        :%i KILOS "%kilos)
        print()
        print("Preco Total:              R$ %.2f"%preco)
        print("Valor Desconto:           R$ %.2f" %desconto)
        print("Valor a pagar:            R$ %.2f" %preco_desc)
        
    if forma_pag =='nao':
        print("tipo de carne selecionado  :ALCATRA  ")
        print("Quantidade de carne        :%i KILOS "%kilos)
        print()
        print("Valor a pagar              :R$ %.2f"%preco)















    #PICANHA <5KG
if tipo_carne == '3' and kilos <=5:
    preco = kilos * 6.9
    if forma_pag == 'sim':#com desconto
        desconto = preco * (5/100)
        preco_desc = preco - desconto
        print("tipo de carne selecionado  :PICANHA  ")
        print("Forma de pagamento         :Cartao Tabajara! ")
        print("Quantidade de carne        :%i KILOS "%kilos)
        print()
        print("Preco Total:              R$ %.2f"%preco)
        print("Valor Desconto:           R$ %.2f" %desconto)
        print("Valor a pagar:            R$ %.2f" %preco_desc)

    if form_pag =='nao': #sem desconto
        print("tipo de carne selecionado  :PICANHA  ")
        print("Quantidade de carne        :%i KILOS "%kilos)
        print()
        print("Valor a pagar              :R$ %.2f"%preco)
       
    #PICANHA >5KG
if tipo_carne == '3' and kilos > 5:
    preco = kilos *7.8
    if forma_pag == 'sim':
        desconto = preco * (5/100)
        preco_desc = preco - desconto
        print("tipo de carne selecionado  :PICANHA  ")
        print("Forma de pagamento         :Cartao Tabajara! ")
        print("Quantidade de carne        :%i KILOS "%kilos)
        print()
        print("Preco Total:              R$ %.2f"%preco)
        print("Valor Desconto:           R$ %.2f" %desconto)
        print("Valor a pagar:            R$ %.2f" %preco_desc)
        
    if form_pag =='nao':
        print("tipo de carne selecionado  :PICANHA  ")
        print("Quantidade de carne        :%i KILOS "%kilos)
        print()
        print("Valor a pagar              :R$ %.2f"%preco)



