qtd_itens = 0
total = 0
print('caixa aberto')

while True:
    print('aguardando')
    preco = float(input('digite o preco: '))

    if preco == 0:
        print('encerrando caixa')
        break

    total += preco
    qtd_itens += 1
    print(f'total atual: {total:.2f}')

print(f'total final: {total:.2f}')
print(f'quantidade itens: {qtd_itens}')
pagar = float(input('digite valor pago: '))
troco = pagar - total

if troco < 0:
    print("pagamento insuficiente")
else:
    print(f'troco: {troco:.2f}')

