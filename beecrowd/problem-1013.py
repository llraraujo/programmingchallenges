

a, b, c = map(int, input().split())

maiorNumero = int((a + b + abs(a -b))/2)

if( maiorNumero > c):
    print(maiorNumero, 'eh o maior')
else:
    print(c,'eh o maior')