
numeros = []

qtd_pares = 0

qtd_impares = 0

qtd_negativos = 0

qtd_positivos = 0

for i in range(0, 5):
    numeros.append(int(input()))
    if numeros[i] % 2 == 0:
        qtd_pares += 1
        if numeros[i] > 0:
            qtd_positivos += 1
        elif numeros[i] < 0:
            qtd_negativos += 1
    elif numeros[i] % 2 != 0:
        qtd_impares += 1
        if numeros[i] > 0:
            qtd_positivos += 1
        elif numeros[i] < 0:
            qtd_negativos += 1


print(f'{qtd_pares} valor(es) par(es)')
print(f'{qtd_impares} valor(es) impar(es)')
print(f'{qtd_positivos} valor(es) positivo(s)')
print(f'{qtd_negativos} valor(es) negativo(s)')
