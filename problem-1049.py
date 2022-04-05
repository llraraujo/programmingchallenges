
primeira_palavra = input().strip()
segunda_palavra = input().strip()
terceira_palavra = input().strip()

ave = {'carnivoro': 'aguia', 'onivoro': 'pomba'}

mamifero = {'herbivoro': 'vaca', 'onivoro': 'homem'}

inseto = {'herbivoro': 'lagarta', 'hematofago': 'pulga'}

anelideo = {'onivoro': 'minhoca', 'hematofago': 'sanguessuga'}


if primeira_palavra == 'vertebrado':
    if segunda_palavra == 'ave':
        print(f'{ave[terceira_palavra]}')

    elif segunda_palavra == 'mamifero':
        print(f'{mamifero[terceira_palavra]}')

elif primeira_palavra == 'invertebrado':
    if segunda_palavra == 'inseto':
        print(f'{inseto[terceira_palavra]}')

    elif segunda_palavra == 'anelideo':
        print(f'{anelideo[terceira_palavra]}')
