novo_valor = 0
valor = input('Adicione suas moedas (valores possíveis: 1, 2 ou 5): ')  
valor_int = int(valor) 

while valor_int < 6:
    if valor_int == 6:
        break 
    else: 
         print('Saldo insuficiente')
         novo_valor = input('Adicione mais moedas:  ') 
         valor_int = int(novo_valor) + valor_int
         print('Você  tem {} moedas. '.format(valor_int)) 
         

##saldo_total = print('Saldo total {} reais.'.format(valor_int))
saldo_total = valor_int


if saldo_total == 6:
    print('Comprar doce A ou adicionar mais moedas?')
    compra = input('Digite A para comprar o doce A e digite N para adiconar mais moedas')
    if compra == 'A':
        print('Doce A comprado. Sem troco. Bom apetite!')
    if compra == 'N' and saldo_total >= 6:
        novo_valor = int(input('Adicione mais moedas:  ')) 
        saldo_total = saldo_total + novo_valor 
        print(saldo_total)
        
'''if saldo_total > 6:
    print('Comprar doce A ou adicionar mais moedas?')
    compra = input('Digite A para comprar o doce A e digite N para adiconar mais moedas')
    if compra == 'A':
        print('Doce A comprado. Bom apetite!')
    if compra == 'N':
        novo_valor = int(input('Adicione mais moedas:  ')) 
        valor_int = novo_valor + valor_int
    '''


