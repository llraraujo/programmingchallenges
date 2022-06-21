n1 = int(input())
n2 = int(input())

if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux

for num in range(n1 + 1, n2):
    if num % 5 == 2 or num % 5 == 3:
        print(num)
