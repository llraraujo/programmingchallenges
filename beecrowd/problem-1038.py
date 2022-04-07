"""
    cada chave representa um produto do cardápio:
        1 - Cachorro-Quente: R$ 4,00
        2 - X-Salada: R$ 4,50
        3 - X-Bacon: R$ 5,00
        4 - Torrada Simples: R$ 2,00
        5 - Refrigerante: R$ 1,50
"""

produtos = {1 : 4.00, 2 : 4.50, 3 : 5.00, 4 : 2.00, 5 : 1.50}



chave, quantidade = map(int, input().split())

total = produtos[chave] * quantidade

print(f'Total: R${total: .2f}')
