preco = float(input('Qual o preço do produto? R$'))
desconto = float(input('Qual o desconto do produto? '))
novo = preco - (preco * desconto / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}.'.format(preco, desconto, novo))
