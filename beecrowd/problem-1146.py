

while True:
    num = int(input())
    if num == 0:
        break
    for i in range(1, num + 1):
        if i == num:
            print(f'{i}')
        else:
            print(f'{i}', end=' ')

