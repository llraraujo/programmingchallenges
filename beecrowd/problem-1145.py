x, y = map(int, input().split())

for num in range(1, y + 1):
    if num == y:
        print(f'{num}')
        break
    elif num % x == 0:
        print(f'{num}')
    else:
        print(f'{num}', end=' ')
