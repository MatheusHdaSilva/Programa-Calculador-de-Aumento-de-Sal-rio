salario = float(input('Qual valor do salário:'))
if salario <= 1250:
  novo = salario + (salario * 15 / 100)
else:
  novo = salario + (salario * 10 / 100)
print('Quem Ganhava R$:{:.2f} passa a ganhar R$:{:.2f}'.format(salario, novo))