
A, B, C = map(float, input().split())


area_triangulo = 0.5 * A * C

area_circulo = 3.14159 * (C ** 2)

area_trapezio = 0.5 * (A + B) * C

area_quadrado = B**2

area_retangulo =  A * B

areas = [area_triangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo]
names = ["TRIANGULO", "CIRCULO", "TRAPEZIO", "QUADRADO", "RETANGULO"]

for i in range(5):
    print(names[i] +':' +' %.3f'%(areas[i]))
