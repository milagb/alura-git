valor_int = 0
novo_valor_somado = 0

while valor_int < 6:
    valor = input('Adicione suas moedas (entre 0 e 15): ')    
    valor_int = int(valor)
    if novo_valor_somado == 6:
        break 
    else: 
         print('Saldo insuficiente')
         novo_valor = int(input('Adicione mais moedas:  ')) + valor_int
         novo_valor_somado = novo_valor + novo_valor_somado
         print('Você  tem {} moedas. '.format(novo_valor_somado))    

doce_a = input('Digite S para comprar o doce A: ')
    
    
    


