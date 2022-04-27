coelhos = 0
ratos = 0
sapos = 0

qtd_testes = int(input())

for _ in range(0, qtd_testes):
    qtd_cobaia, tipo_cobaia = input().split()
    if tipo_cobaia == 'C':
        coelhos += int(qtd_cobaia)
    elif tipo_cobaia == 'R':
        ratos += int(qtd_cobaia)
    elif tipo_cobaia == 'S':
        sapos += int(qtd_cobaia)

total_de_cobaias = coelhos + ratos + sapos
percentual_coelhos = (coelhos/total_de_cobaias) * 100
percentual_ratos = (ratos/total_de_cobaias) * 100
percentual_sapos = (sapos/total_de_cobaias) * 100

print(f'Total: {total_de_cobaias} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {percentual_coelhos:.2f} %')
print(f'Percentual de ratos: {percentual_ratos:.2f} %')
print(f'Percentual de sapos: {percentual_sapos:.2f} %')
