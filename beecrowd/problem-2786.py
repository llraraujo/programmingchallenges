L = int(input())
C = int(input())

tipo1 = 0
tipo2 = 0

if L * C == 1:
    tipo1 += 1
    print(tipo1)
    print(tipo2)

else:
    tipo1 = L * C + (C - 1) * (L - 1)
    tipo2 = (C - 1)*2 + (L - 1) * 2
    print(tipo1)
    print(tipo2)

