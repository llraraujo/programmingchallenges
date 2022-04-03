start, end = map(int, input().split())


count = 0

if start == end:
    print('O JOGO DUROU 24 HORA(S)')

else:
    while start != end:
        count += 1
        start += 1
        if start == 24:
            start = 0

    print(f'O JOGO DUROU {count} HORA(S)')





