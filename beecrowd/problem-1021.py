
value = float(input())

intValue = int(value)

cts = round((value - int(value))*100)


def notas(cedules):

    c = int(cedules/100)
    cedules = cedules - c*100
    d = int(cedules/50)
    cedules = cedules - d*50
    u = int(cedules/20)
    cedules = cedules - u*20
    i = int(cedules/10)
    cedules = cedules - i*10
    v = int(cedules/5)
    cedules = cedules - v*5
    w = int(cedules/2)
    cedules = cedules - w*2
    l = cedules
    return c, d, u, i, v ,w, l


def cents(centavos):

    c = int(centavos/50)
    centavos = centavos - c*50
    d = int(centavos/25)
    centavos = centavos - d*25
    u = int(centavos/10)
    centavos = centavos - u*10
    i = int(centavos/5)
    centavos = centavos - i*5
    l = centavos

    return c, d, u, i, l


cedulas = notas(intValue)

centavos = cents(cts)


print("NOTAS:")
print(cedulas[0], 'nota(s) de R$ 100.00' )
print(cedulas[1], 'nota(s) de R$ 50.00' )
print(cedulas[2], 'nota(s) de R$ 20.00' )
print(cedulas[3], 'nota(s) de R$ 10.00' )
print(cedulas[4], 'nota(s) de R$ 5.00' )
print(cedulas[5], 'nota(s) de R$ 2.00' )

print("MOEDAS:")
print(cedulas[6], 'moeda(s) de R$ 1.00' )
print(centavos[0], 'moeda(s) de R$ 0.50' )
print(centavos[1], 'moeda(s) de R$ 0.25' )
print(centavos[2], 'moeda(s) de R$ 0.10' )
print(centavos[3], 'moeda(s) de R$ 0.05' )
print(centavos[4], 'moeda(s) de R$ 0.01' )

