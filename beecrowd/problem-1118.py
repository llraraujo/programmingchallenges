
notas = 0
count = 0
opt = 1


def media(n1, n2):
    return (n1 + n2)/2


def is_valid(n):
    if n < 0 or n > 10:
        return False
    return True


while True:
    nota = float(input())

    while not is_valid(nota):
        print('nota invalida')
        nota = float(input())

    a = nota

    nota = float(input())

    while not is_valid(nota):
        print('nota invalida')
        nota = float(input())

    b = nota

    print(f'media = {media(a, b):.2f}')
    print('novo calculo (1-sim 2-nao)')
    opt = int(input())
    while opt < 1 or opt > 2:
        print('novo calculo (1-sim 2-nao)')
        opt = int(input())
    if opt == 2:
        break
