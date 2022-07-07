def factorial(n, prod=1):
    if n == 1:
        return 1 * prod
    prod *= n
    return factorial(n-1, prod)


n = int(input())

print(f'{factorial(n)}')
