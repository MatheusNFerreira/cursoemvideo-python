from time import sleep
def contagem_regressiva(tempo_total):
    for i in range(tempo_total, 0, -1):
        print(i)
        sleep(1)
    print('BUM! BUM! POOOW!')

tempo_total = 10
contagem_regressiva(tempo_total)
