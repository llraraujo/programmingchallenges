numero_de_linhas = int(input())

for num in range(1, numero_de_linhas + 1):
    num2 = num**2
    num3 = num**3
    print(f'{num} {num2} {num3}')
    print(f'{num} {num2 + 1} {num3 + 1}')
