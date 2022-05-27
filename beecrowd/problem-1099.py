
def soma_impares(n1, n2):
    soma = 0
    for i in range(n1 + 1, n2):

        if i % 2 != 0:
            soma += i

    return soma



n_testes = int(input())

for _ in range(n_testes):
    a, b = map(int, input().split())
    if a > b:
        aux = b
        b = a
        a = aux
    print(soma_impares(a, b))
