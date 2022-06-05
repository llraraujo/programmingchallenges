count = 0
notas = 0

while count != 2:
    nota = float(input())
    if nota < 0 or nota > 10:
        print('nota invalida')
    else:
        notas += nota
        count += 1

media = notas/2

print(f'media = {media:.2f}')
