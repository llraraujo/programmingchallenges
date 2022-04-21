
qtd_casas, qtd_encomendas = map(int, input().split())

casas = tuple(map(int, input().split()))

encomendas = tuple(map(int, input().split()))

tempo = 0
casa_anterior = 0

for pacote in encomendas:
    tempo += abs(casas.index(pacote) - casa_anterior)
    casa_anterior = casas.index(pacote)

print(f'{tempo}')
