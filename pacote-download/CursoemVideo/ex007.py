n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2)/2
print('A nota final do aluno é {:.1f}' .format(m))
if m >= 6:
    print('Aprovado')
else:
    print('Reprovado')
