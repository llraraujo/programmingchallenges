

def reajuste(valor, percentual):
    novo_salario = valor * (1 + percentual/100)
    reajuste_ganho = valor * (percentual/100)
    return novo_salario, reajuste_ganho, percentual


salario = float(input())

if salario <= 400:
    novo_salario, reajuste_ganho, percentual = reajuste(salario, 15)
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste_ganho:.2f}\nEm percentual: {percentual} %')
elif 400 < salario <= 800.00:
    novo_salario, reajuste_ganho, percentual = reajuste(salario, 12)
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste_ganho:.2f}\nEm percentual: {percentual} %')
elif 800 < salario <= 1200.00:
    novo_salario, reajuste_ganho, percentual = reajuste(salario, 10)
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste_ganho:.2f}\nEm percentual: {percentual} %')
elif 1200 < salario <= 2000.00:
    novo_salario, reajuste_ganho, percentual = reajuste(salario, 7)
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste_ganho:.2f}\nEm percentual: {percentual} %')
elif salario > 2000:
    novo_salario, reajuste_ganho, percentual = reajuste(salario, 4)
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste_ganho:.2f}\nEm percentual: {percentual} %')
