
numeros = []

qtd_pares = 0

for i in range(0, 5):
    numeros.append(int(input()))
    if numeros[i] % 2 == 0:
        qtd_pares += 1


print(f'{qtd_pares} valores pares')
