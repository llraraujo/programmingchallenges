
salario = float(input())

imposto = 0.0

if 0.0 < salario <= 2000.0:
    print('Isento')
else:
    if 2000.0 < salario <= 3000.0:
        salario -= 2000
        imposto = salario * 0.08

    elif 3000.0 < salario <= 4500.0:
        salario -= 2000
        if salario >= 1000:
            imposto = 1000 * 0.08
            salario -= 1000

        imposto += salario * 0.18

    elif 4500.0 < salario:
        salario -= 2000
        if salario >= 1000:
            imposto += 1000 * 0.08
            salario -= 1000

        if salario >= 1500:
            imposto += 1500 * 0.18
            salario -= 1500

        imposto += salario * 0.28

    print(f'R$ {imposto:.2f}')
