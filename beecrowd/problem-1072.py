
qtd_testes = int(input())

dentro = 0

fora = 0

while qtd_testes > 0:
    qtd_testes -= 1

    x = int(input())
    if x in range(10, 21):
        dentro += 1
    else:
        fora += 1


print(f'{dentro} in\n{fora} out')