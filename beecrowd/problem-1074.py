def isOdd_or_isEeven(number):
    if not number % 2 == 0:
        return 'ODD'
    else:
        return 'EVEN'


def isPositive_or_isNegative(number):
    if number > 0:
        return 'POSITIVE'
    else:
        return 'NEGATIVE'


loop_length = int(input())

numbers = []

while loop_length > 0:
    loop_length -= 1
    numbers.append(int(input()))


for num in numbers:
    if num == 0:
        print('NULL')
    else:
        print(f'{isOdd_or_isEeven(num)} {isPositive_or_isNegative(num)}')
