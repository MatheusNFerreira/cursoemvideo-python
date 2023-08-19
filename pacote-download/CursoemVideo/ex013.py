salario = float(input('Qual o salário do funcionário? R$'))
aumento = float(input('Quantos porcento de aumento será? '))
novo = salario + (salario * aumento / 100)
print('O salário anterior do funcionário é de R${:.2f}. Com o aumento de {}%, o salário atual é de R${:.2f}.'.format(salario, aumento, novo))