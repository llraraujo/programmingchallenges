


a, b, c = (map(int, input().split()))

numbers = [a, b, c]

numbersSorted = []

if a > b and b > c:
    numbersSorted.append(c)
    numbersSorted.append(b)
    numbersSorted.append(a)

elif b > a and  a > c:
    numbersSorted.append(c)
    numbersSorted.append(a)
    numbersSorted.append(b)

elif c > b and  b > a:
    numbersSorted.append(a)
    numbersSorted.append(b)
    numbersSorted.append(c)

elif a > c and c > b:
    numbersSorted.append(b)
    numbersSorted.append(c)
    numbersSorted.append(a)

elif b > c and c > a:
    numbersSorted.append(a)
    numbersSorted.append(c)
    numbersSorted.append(b)

elif c > a and a > b:
    numbersSorted.append(b)
    numbersSorted.append(a)
    numbersSorted.append(c)


for i in range(0, len(numbersSorted)):
    print(numbersSorted[i])

print()

for i in range(0, len(numbers)):
    print(numbers[i])
