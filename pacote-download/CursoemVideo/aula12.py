nome = str(input('Qual é o seu nome? '))
if nome == 'Matheus':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Ana':
    print('Que nominho comum, tem muitas pessoas com esse nome no Brasil...')
elif nome in 'Ana Paula':
    print('Que nome Lindo!!! <3')
else:
    print('Seu nome é bem normal...')
print('Tenha um bom dia {}'.format(nome))