n = int(input())

qtde_100 = 0
qtde_50 = 0
qtde_20 = 0
qtde_10 = 0
qtde_5 = 0
qtde_2 = 0
qtde_1 = 0

print(n)

while(n/100 >= 1):
    qtde_100 = int(n/100) 
    n = n - qtde_100 * 100


while(n/50 >= 1):
    qtde_50 = int(n/50) 
    n = n - qtde_50 * 50


while(n/20 >= 1):
    qtde_20 = int(n/20) 
    n = n - qtde_20 * 20

while(n/10 >= 1):
    qtde_10 = int(n/10) 
    n = n - qtde_10 * 10
    

while(n/5 >= 1):
    qtde_5 = int(n/5) 
    n = n - qtde_5 * 5

while(n/2 >= 1):
    qtde_2 = int(n/2) 
    n = n - qtde_2 * 2

if(n != 0): 
    qtde_1 = n


print(qtde_100, 'nota(s) de R$ 100,00')
print(qtde_50, 'nota(s) de R$ 50,00')
print(qtde_20, 'nota(s) de R$ 20,00')
print(qtde_10, 'nota(s) de R$ 10,00')
print(qtde_5, 'nota(s) de R$ 5,00')
print(qtde_2, 'nota(s) de R$ 2,00')
print(qtde_1, 'nota(s) de R$ 1,00')

# Método alternativo
'''
def cedules(valor, n1=0):
    if(valor/ 100 >= 1):
        n1 = int(valor/100)
        valor = valor - n1*100
        print(n1,'nota(s) de R$ 100,00')
        return cedules(valor, n1)
    if(valor/ 50 >= 1):
        n1 = int(valor/50)
        valor = valor - n1*50
        print(n1,'nota(s) de R$ 50,00')
        return cedules(valor, n1)
    if(valor/ 20 >= 1):
        n1 = int(valor/20)
        valor = valor - n1*20
        print(n1,'nota(s) de R$ 20,00')
        return cedules(valor, n1)
    if(valor/ 10 >= 1):
        n1 = int(valor/10)
        valor = valor - n1*10
        print(n1,'nota(s) de R$ 10,00')
        return cedules(valor, n1)
    if(valor/ 5 >= 1):
        n1 = int(valor/5)
        valor = valor - n1*5
        print(n1,'nota(s) de R$ 5,00')
        return cedules(valor, n1)
    if(valor/ 2 >= 1):
        n1 = int(valor/2)
        valor = valor - n1*2
        print(n1,'nota(s) de R$ 2,00')
        return cedules(valor, n1)        
    return  print(valor, 'nota(s) de R$ 1,00')
'''