
# 12 Km/L 
consumo = 12

tempo = int(input())
velocidade_media = int(input())

# distancia = tempo * velocidade
litros_necessarios = (tempo*velocidade_media)/consumo

print('%.3f'%(litros_necessarios))