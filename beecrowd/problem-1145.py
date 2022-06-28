x, y = map(int, input().split())

for num in range(1, y + 1):
    print(f'{num}', end=' ')
    if num % x == 0 and num != y:
        print()
    if num == y:
        break
