
a, b, c = map(float, input().split())

numbers = [a, b, c]
numbers.sort()

a, b, c = numbers[2], numbers[1], numbers[0]


if a >= (b + c):
    print('NAO FORMA TRIANGULO')
elif a**2 == (b**2 + c**2):
    print('TRIANGULO RETANGULO')
elif a**2 > (b**2 + c**2):
    print('TRIANGULO OBTUSANGULO')
elif a**2 < (b**2 + c**2):
    print('TRIANGULO ACUTANGULO')


if a == b == c:
    print('TRIANGULO EQUILATERO')
elif a == b or a == c or b == c:
    print('TRIANGULO ISOSCELES')
