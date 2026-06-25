qtd_itens = 0
total = 0
print('caixa aberto')

while True:
    print('aguardando')
    preco = float(input('digite o preco: '))

    if preco == 0:
        print('encerrando caixa')
        break
    
