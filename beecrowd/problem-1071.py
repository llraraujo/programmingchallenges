number1 = int(input())

number2 = int(input())

soma = 0

for num in range(number2 + 1, number1):
    if num % 2 != 0:
        soma += num

print(f'{soma}')
