
qtd_pessoas_na_fila = int(input())

fila = list(map(int, input().split()))

qtd_sairam = int(input())

fora_da_fila = list(map(int, input().split()))

for i in range(0, qtd_sairam):
    fila.remove(fora_da_fila[i])

final = str(fila).replace(",", "")
print(final[1:len(final)-1:])
