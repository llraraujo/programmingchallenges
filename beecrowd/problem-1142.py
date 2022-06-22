qtd_linhas = int(input())

linha = ''
for i in range(1, 4*qtd_linhas + 1):
    if i % 4 == 0:
        print(linha + 'PUM')
        linha = ''
    else:
        linha += str(i) + ' '



