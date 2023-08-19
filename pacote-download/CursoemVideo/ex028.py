from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "pensar"
#print('Pensei no número {}'.format(computador))
print('-=-' * 20)
print('Tente adivinhar em qual número eu pensei entre 0 à 5...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # O jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(computador, jogador))
