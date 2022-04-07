horaInicial, minutoInicial, horaFinal, minutoFinal = map(int, input().split())

count = 0

if horaInicial == horaFinal and minutoInicial == minutoFinal:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')

else:
    while horaInicial != horaFinal:
        minutoInicial += 1
        count += 1
        if minutoInicial == 60:
            minutoInicial = 0
            horaInicial += 1
            if horaInicial == 24:
                horaInicial = 0

    while minutoInicial != minutoFinal:
        count += 1
        minutoInicial += 1

    horas = count // 60
    minutos = count % 60

    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')



