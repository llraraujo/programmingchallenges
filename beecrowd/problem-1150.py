x = int(input())
z = int(input())

while z <= x:
    z = int(input())

soma = 0
count = 0
for num in range(x, 999999999):
    soma += num
    count += 1
    if soma > z:
        break

print(count)
