import math
import matplotlib.pyplot as pyplot

def main():

    # tempo inicial
    t0 = 0

    # tempo final
    tf = 10

    # passo de tempo
    dt = 1

    estados = []

    # Posição inicial
    s0 = 0

    # Velocidade inicial
    v0 = 0

    # Aceleração inicial
    a0 = 0

    # Aceleração atual
    a = 0

    # Velocidade instantânea
    v = 0

    # Tempo atual
    t = 0

    # Posição atual
    s = 0

    estados.append(0)
    estados.append(0)
    estados.append(0)

    while (t <= tf):
        a = a0 + 6 * t
        v = a + estados[t * 3 + 1]
        s = v + estados[t * 3 + 2]
        t = t + 1
        estados.append(t)
        estados.append(v)
        estados.append(s)
        

    # Se você implementou tudo certinho, use os comandos abaixo para graficar os resultados.
    pyplot.figure(0)

    tempos = []
    velocidades = []
    espacos = []

    for i in range(tf):
        
        tempos.append(estados[i * 3])
        velocidades.append(estados[i * 3 + 1])
        espacos.append(estados[i * 3 + 2])
        

    pyplot.plot(tempos, velocidades, label='Euler',linestyle='',marker='o') 
    pyplot.plot(tempos, espacos, label='Euler',linestyle='',marker='o') 

    pyplot.title('Position')
    pyplot.show(block=False)

main() 