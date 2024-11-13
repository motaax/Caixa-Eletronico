saldo = 1000

print('Bem-vindo ao Caixa Eletrônico. Saldo atual: R$1000')

while True:
    retirada = float(input("Digite o valor que deseja retirar ou '0' para encerrar: "))
    if retirada == 0:
        print('Operação finalizada.')
        break
    elif retirada > saldo:
        print('Saldo insuficiente. Tente um valor menor.')
    else:
        saldo -= retirada
        print(f'Retirada realizada. Saldo atual: R${saldo:.2f}')

print()
print(f'Saldo final: R${saldo:.2f}')