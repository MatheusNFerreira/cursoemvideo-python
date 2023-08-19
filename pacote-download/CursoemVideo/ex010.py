real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 5.32
print('Com R${} você pode comprar US${:.2f}.'.format(real, dolar))
