def sum_interval(a, b):
    seq = ''
    soma = 0
    for num in range(a, b + 1):
        seq += str(num) + ' '
        soma += num

    return f'{seq}Sum={soma}'


while True:
    n1, n2 = map(int, input().split())
    if n1 <= 0 or n2 <= 0:
        break
    if n1 > n2:
        aux = n2
        n2 = n1
        n1 = aux
    print(sum_interval(n1, n2))
