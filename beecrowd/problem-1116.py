
qtd_testes = int(input())

for _ in range(qtd_testes):
    x, y = map(int, input().split())
    try:
        print(f'{x/y:.1f}')
    except ZeroDivisionError:
        print('divisao impossivel')
