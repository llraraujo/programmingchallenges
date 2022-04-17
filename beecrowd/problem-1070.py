
num = int(input())

count = 0

while count < 6:
    if num % 2 != 0:
        print(f'{num}')
        count += 1
    num += 1
