qtd_tests = int(input())

medias = []

while qtd_tests > 0:
    qtd_tests -= 1
    notas = list(map(float, input().split()))
    media_ponderada = (notas[0]*2 + notas[1]*3 + notas[2]*5) / 10
    medias.append(media_ponderada)

for media in medias:
    print(f'{media:.1f}')
