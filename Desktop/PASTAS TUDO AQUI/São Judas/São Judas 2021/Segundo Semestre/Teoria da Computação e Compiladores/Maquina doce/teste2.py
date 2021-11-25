novo_valor = 0
valor = input('Adicione suas moedas (valores possíveis: 1, 2 ou 5): ')  
valor_int = int(valor) 

if valor_int == 1:
    print('Saldo insuficiente')
    novo_valor = int(input('Adicione mais moedas:  ')) 
    valor_int = valor_int + novo_valor 
    print('Você  tem {} moedas. '.format(valor_int)) 
    
if valor_int == 2:
    print('Saldo insuficiente')
    novo_valor = int(input('Adicione mais moedas:  ')) 
    valor_int = valor_int + novo_valor 
    print('Você  tem {} moedas. '.format(valor_int))
    
if valor_int == 3:
    print('Saldo insuficiente')
    novo_valor = int(input('Adicione mais moedas:  ')) 
    valor_int = valor_int + novo_valor 
    print('Você  tem {} moedas. '.format(valor_int))
    
if valor_int == 4:
    print('Saldo insuficiente')
    novo_valor = int(input('Adicione mais moedas:  ')) 
    valor_int = valor_int + novo_valor 
    print('Você  tem {} moedas. '.format(valor_int))
    
if valor_int == 5:
    print('Saldo insuficiente')
    novo_valor = int(input('Adicione mais moedas:  ')) 
    valor_int = valor_int + novo_valor 
    print('Você  tem {} moedas. '.format(valor_int))
    
#compra DOCE A sem troco 
if valor_int == 6:
    compra_doceA = int(input('Gostaria de comprar o DOCE A? Sim: digite 1, Não: digite 0: '))
    if compra_doceA == 1:
        print('Doce A comprado. Sem troco. Bom apetite!')
        
    else:
        print('Saldo insuficiente')
        novo_valor = int(input('Adicione mais moedas:  ')) 
        valor_int = valor_int + novo_valor 
        print('Você  tem {} moedas. '.format(valor_int))

#compra DOCE B sem troco
if valor_int == 7:
        compra_doceA = int(input('Gostaria de comprar o DOCE A? Sim: digite 1, Não: digite 0: '))
        if compra_doceA == 1:
            print('Doce A comprado. Troco: R$ 1,00. Bom apetite!') 
        else:
            print('Você  tem {} moedas. '.format(valor_int))
            compra_doceB = int(input('Gostaria de comprar o DOCE B? Sim: digite 1, Não: digite 0: '))
            if compra_doceB == 1:
                 print('Doce B comprado. Sem troco. Bom apetite!')  
            else:
                print('Saldo insuficiente')
                novo_valor = int(input('Adicione mais moedas:  ')) 
                valor_int = valor_int + novo_valor 
                print('Você  tem {} moedas. '.format(valor_int))
        
if valor_int == 8:
    compra_doceA = int(input('Gostaria de comprar o DOCE A? Sim: digite 1, Não: digite 0: '))
    if compra_doceA == 1:
        print('Doce A comprado. Troco: R$ 2,00. Bom apetite!')
    else:
        print('Você  tem {} moedas. '.format(valor_int))
        compra_doceB = int(input('Gostaria de comprar o DOCE B? Sim: digite 1, Não: digite 0: '))
        if compra_doceB == 1:
            print('Doce A comprado. Troco: R$ 1,00. Bom apetite!')  
        else:
            print('Você  tem {} moedas. '.format(valor_int))
            compra_doceC = int(input('Gostaria de comprar o DOCE C? Sim: digite 1, Não: digite 0: '))
            if compra_doceC == 1:
                print('Doce C comprado. Sem troco. Bom apetite!')
            else:
                novo_valor = int(input('Adicione mais moedas:  ')) 
                valor_int = valor_int + novo_valor 
                print('Você  tem {} moedas. '.format(valor_int))
           

if valor_int == 9:
    compra_doceA = int(input('Gostaria de comprar o DOCE A? Sim: digite 1, Não: digite 0: '))
    if compra_doceA == 1:
        print('Doce A comprado. Troco: R$ 3,00. Bom apetite!')
    else:
        print('Você  tem {} moedas. '.format(valor_int))
        compra_doceB = int(input('Gostaria de comprar o DOCE B? Sim: digite 1, Não: digite 0: '))
        if compra_doceB == 1:
            print('Doce A comprado. Troco: R$ 2,00. Bom apetite!')  
        else:
            print('Você  tem {} moedas. '.format(valor_int))
            compra_doceC = int(input('Gostaria de comprar o DOCE C? Sim: digite 1, Não: digite 0: '))
            if compra_doceC == 1:
                print('Doce C comprado. Troco: R$ 1,00. Bom apetite!')
            else:
                novo_valor = int(input('Adicione mais moedas:  ')) 
                valor_int = valor_int + novo_valor 
                print('Você  tem {} moedas. '.format(valor_int))
                
if valor_int == 10:
    compra_doceA = int(input('Gostaria de comprar o DOCE A? Sim: digite 1, Não: digite 0: '))
    if compra_doceA == 1:
        print('Doce A comprado. Troco: R$ 4,00. Bom apetite!')
    else:
        print('Você  tem {} moedas. '.format(valor_int))
        compra_doceB = int(input('Gostaria de comprar o DOCE B? Sim: digite 1, Não: digite 0: '))
        if compra_doceB == 1:
            print('Doce A comprado. Troco: R$ 3,00. Bom apetite!')  
        else:
            print('Você  tem {} moedas. '.format(valor_int))
            compra_doceC = int(input('Gostaria de comprar o DOCE C? Sim: digite 1, Não: digite 0: '))
            if compra_doceC == 1:
                print('Doce C comprado. Troco: R$ 2,00. Bom apetite!')
            else:
                novo_valor = int(input('Adicione mais moedas:  ')) 
                valor_int = valor_int + novo_valor 
                print('Você  tem {} moedas. '.format(valor_int))
    

if valor_int == 11:
    compra_doceA = int(input('Gostaria de comprar o DOCE A? Sim: digite 1, Não: digite 0: '))
    if compra_doceA == 1:
        print('Doce A comprado. Troco: R$ 5,00. Bom apetite!')
    else:
        print('Você  tem {} moedas. '.format(valor_int))
        compra_doceB = int(input('Gostaria de comprar o DOCE B? Sim: digite 1, Não: digite 0: '))
        if compra_doceB == 1:
            print('Doce A comprado. Troco: R$ 4,00. Bom apetite!')  
        else:
            print('Você  tem {} moedas. '.format(valor_int))
            compra_doceC = int(input('Gostaria de comprar o DOCE C? Sim: digite 1, Não: digite 0: '))
            if compra_doceC == 1:
                print('Doce C comprado. Troco: R$ 3,00. Bom apetite!')
            else:
                novo_valor = int(input('Adicione mais moedas:  ')) 
                valor_int = valor_int + novo_valor 
                print('Você  tem {} moedas. '.format(valor_int))
 
if valor_int == 12:
    compra_doceA = int(input('Gostaria de comprar o DOCE A? Sim: digite 1, Não: digite 0: '))
    if compra_doceA == 1:
        print('Doce A comprado. Troco: R$ 6,00. Bom apetite!')
    else:
        print('Você  tem {} moedas. '.format(valor_int))
        compra_doceB = int(input('Gostaria de comprar o DOCE B? Sim: digite 1, Não: digite 0: '))
        if compra_doceB == 1:
            print('Doce A comprado. Troco: R$ 4,00. Bom apetite!')  
        else:
            print('Você  tem {} moedas. '.format(valor_int))
            compra_doceC = int(input('Gostaria de comprar o DOCE C? Sim: digite 1, Não: digite 0: '))
            if compra_doceC == 1:
                print('Doce C comprado. Troco: R$ 3,00. Bom apetite!')   
            else:
                novo_valor = int(input('Adicione mais moedas:  ')) 
                valor_int = valor_int + novo_valor 
                print('Você  tem {} moedas. '.format(valor_int))

if valor_int == 13:
    compra_doceA = int(input('Gostaria de comprar o DOCE A? Sim: digite 1, Não: digite 0: '))
    if compra_doceA == 1:
        print('Doce A comprado. Troco: R$ 7,00. Bom apetite!')
    else:
        print('Você  tem {} moedas. '.format(valor_int))
        compra_doceB = int(input('Gostaria de comprar o DOCE B? Sim: digite 1, Não: digite 0: '))
        if compra_doceB == 1:
            print('Doce A comprado. Troco: R$ 5,00. Bom apetite!')  
        else:
            print('Você  tem {} moedas. '.format(valor_int))
            compra_doceC = int(input('Gostaria de comprar o DOCE C? Sim: digite 1, Não: digite 0: '))
            if compra_doceC == 1:
                print('Doce C comprado. Troco: R$ 4,00. Bom apetite!') 
            else:
                novo_valor = int(input('Adicione mais moedas:  ')) 
                valor_int = valor_int + novo_valor 
                print('Você  tem {} moedas. '.format(valor_int))   


if valor_int == 14:
    compra_doceA = int(input('Gostaria de comprar o DOCE A? Sim: digite 1, Não: digite 0: '))
    if compra_doceA == 1:
        print('Doce A comprado. Troco: R$ 8,00. Bom apetite!')
    else:
        print('Você  tem {} moedas. '.format(valor_int))
        compra_doceB = int(input('Gostaria de comprar o DOCE B? Sim: digite 1, Não: digite 0: '))
        if compra_doceB == 1:
            print('Doce A comprado. Troco: R$ 6,00. Bom apetite!')  
        else:
            print('Você  tem {} moedas. '.format(valor_int))
            compra_doceC = int(input('Gostaria de comprar o DOCE C? Sim: digite 1, Não: digite 0: '))
            if compra_doceC == 1:
                print('Doce C comprado. Troco: R$ 5,00. Bom apetite!')  
            else:
                novo_valor = int(input('Adicione mais moedas:  ')) 
                valor_int = valor_int + novo_valor 
                print('Você  tem {} moedas. '.format(valor_int))

if valor_int == 15:
    compra_doceA = int(input('Gostaria de comprar o DOCE A? Sim: digite 1, Não: digite 0: '))
    if compra_doceA == 1:
        print('Doce A comprado. Troco: R$ 9,00. Bom apetite!')
    else:
        print('Você  tem {} moedas. '.format(valor_int))
        compra_doceB = int(input('Gostaria de comprar o DOCE B? Sim: digite 1, Não: digite 0: '))
        if compra_doceB == 1:
            print('Doce A comprado. Troco: R$ 7,00. Bom apetite!')  
        else:
            print('Você  tem {} moedas. '.format(valor_int))
            compra_doceC = int(input('Gostaria de comprar o DOCE C? Sim: digite 1, Não: digite 0: '))
            if compra_doceC == 1:
                print('Doce C comprado. Troco: R$ 6,00. Bom apetite!')   
            else:
                novo_valor = int(input('Adicione mais moedas:  ')) 
                valor_int = valor_int + novo_valor 
                print('Você  tem {} moedas. '.format(valor_int))            
                       
            


    