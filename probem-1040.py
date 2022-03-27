
nota1, nota2, nota3, nota4 = map(float,input().split())

peso1, peso2, peso3, peso4 = (2, 3, 4, 1)


media = (nota1*peso1 + nota2*peso2 + nota3*peso3 + nota4*peso4)/(peso1 + peso2 + peso3 + peso4)

print(f'Media: {media:.1f}')
if media  < 5.0: 
    print("Aluno reprovado.")

elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    notaDoExame = float(input())
    novaMedia = (media + notaDoExame)/2
    print(f'Nota do exame: {notaDoExame:.1f}')

    if novaMedia >= 5.0:
        print("Aluno aprovado.")
        print(f'Media final: {novaMedia:.1f}')
    else:
        print("Aluno reprovado.")
else:
    print("Aluno aprovado.")
