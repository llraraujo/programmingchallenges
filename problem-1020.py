
dias = int(input())
mes = 0
ano = 0


if dias >= 30:
    aux = dias
    while aux >= 30:
        mes += 1
        if mes >= 12:
            ano += 1
            mes -= 12
        aux = dias - mes*30 - ano*365
    dias = aux
    



    
    
print(f'{ano} ano(s)\n{mes} mes(es)\n{dias} dia(s)')