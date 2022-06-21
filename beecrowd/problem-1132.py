n1 = int(input())
n2 = int(input())

if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux

soma = 0
for num in range(n1, n2 + 1):
    if num % 13 != 0:
        soma += num


print(soma)
