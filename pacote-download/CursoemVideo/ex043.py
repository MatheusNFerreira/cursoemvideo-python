peso = float(input('Qual é o seu peso(Kg)? '))
altura = float(input('Qual é sua altura(m)? '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc), end='')
if imc < 18.5:
    print('. Está abaixo do peso normal.')
elif 18.5 <= imc < 25:
    print('. Está no peso ideal.')
elif 25 <= imc < 30:
    print('. Está com sobrepeso.')
elif 30 <= imc < 40:
    print('. Está obesidade.')
else:
    print('. Está com obesidade mórbida.')
