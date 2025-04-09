import time

def semaforo_simulado():
    TEMPO_VERDE = 5
    TEMPO_AMARELO = 2
    TEMPO_VERMELHO = 5
    
    while True:
        print("\033[32mVerde\033[0m")
        time.sleep(TEMPO_VERDE)
        
        print("\033[33mAmarelo\033[0m")
        time.sleep(TEMPO_AMARELO)
        
        print("\033[31mVermelho\033[0m")
        time.sleep(TEMPO_VERMELHO)

if __name__ == '__main__':
    try:
        semaforo_simulado()
    except KeyboardInterrupt:
        print("\nSemaforo desligado")