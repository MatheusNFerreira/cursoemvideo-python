larg = float(input('A largura da parede: '))
alt = float(input('A Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua area é de {:.2f}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar sua parede, será necessário de {}l de tinta.'.format(tinta))
