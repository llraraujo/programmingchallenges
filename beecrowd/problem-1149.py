numbers = list(map(int, input().split()))

a = numbers[0]
b = -1

for i in range(1, len(numbers)):
    if numbers[i] > 0:
        b = numbers[i]
        break


while b <= 0:
    b = int(input())

total = 0
for i in range(b):
    total += i + a
print(total)
