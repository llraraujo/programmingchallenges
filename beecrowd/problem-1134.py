
alcool = 0
gasolina = 0
diesel = 0

while True:
    opt = int(input())
    if opt == 4:
        break
    elif opt == 1:
        alcool += 1
    elif opt == 2:
        gasolina += 1
    elif opt == 3:
        diesel += 1

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
