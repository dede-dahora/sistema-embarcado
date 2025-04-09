import time
import random
import logging
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class SistemaIrrigacao:
    def __init__(self):
        self.umidade_solo = 50  # % (valor inicial)
        self.umidade_minima = 30  # % abaixo do qual ativa irrigação
        self.tempo_irrigacao = 5  # segundos
        self.intervalo_verificacao = 10  # segundos
        self.bomba_ligada = False
        self.historico = []
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            handlers=[
                logging.FileHandler('irrigacao.log'),
                logging.StreamHandler()
            ]
        )
        
        self.log("Sistema de irrigação inicializado")
    
    def log(self, mensagem):
        """Registra mensagens no log"""
        logging.info(mensagem)
        self.historico.append(f"{datetime.now().strftime('%H:%M:%S')} - {mensagem}")
    
    def ler_sensor(self):
        """Simula a leitura do sensor de umidade"""
        # Variação aleatória simulando condições reais
        variacao = random.uniform(-2, 2)
        
        # Se a bomba está ligada, reduz a umidade mais rápido
        if self.bomba_ligada:
            variacao -= random.uniform(5, 8)
        else:
            # Simula evaporação e absorção pelas plantas
            variacao -= random.uniform(0.5, 1.5)
            
            # Simula chuva ocasionalmente (10% de chance)
            if random.random() < 0.1:
                variacao += random.uniform(5, 15)
                self.log("Chuva detectada - umidade aumentando")
        
        self.umidade_solo = max(0, min(100, self.umidade_solo + variacao))
        return self.umidade_solo
    
    def controlar_bomba(self, ligar):
        """Simula o controle da bomba de irrigação"""
        self.bomba_ligada = ligar
        estado = "ligada" if ligar else "desligada"
        self.log(f"Bomba {estado} - Umidade: {self.umidade_solo:.1f}%")
    
    def executar_ciclo(self):
        """Executa um ciclo de verificação e controle"""
        umidade = self.ler_sensor()
        self.log(f"Umidade do solo: {umidade:.1f}%")
        
        if umidade < self.umidade_minima and not self.bomba_ligada:
            self.controlar_bomba(True)
            time.sleep(self.tempo_irrigacao)
            self.controlar_bomba(False)
    
    def monitorar(self, duracao=300):
        """Monitora o sistema por um período de tempo"""
        self.log(f"Iniciando monitoramento por {duracao} segundos")
        inicio = time.time()
        
        # Configuração do gráfico em tempo real
        plt.style.use('ggplot')
        fig, ax = plt.subplots()
        x_data, y_data = [], []
        ln, = ax.plot([], [], 'b-', label='Umidade (%)')
        ax.axhline(y=self.umidade_minima, color='r', linestyle='--', label='Limite mínimo')
        
        def init():
            ax.set_xlim(0, duracao)
            ax.set_ylim(0, 100)
            ax.set_xlabel('Tempo (s)')
            ax.set_ylabel('Umidade do Solo (%)')
            ax.set_title('Sistema de Irrigação - Monitoramento')
            ax.legend()
            return ln,
        
        def update(frame):
            # Executa um ciclo do sistema
            self.executar_ciclo()
            
            # Atualiza dados do gráfico
            tempo_decorrido = time.time() - inicio
            x_data.append(tempo_decorrido)
            y_data.append(self.umidade_solo)
            
            ln.set_data(x_data, y_data)
            
            # Destaca quando a bomba está ligada
            if self.bomba_ligada:
                ax.axvspan(tempo_decorrido-0.5, tempo_decorrido+0.5, color='yellow', alpha=0.3)
            
            return ln,
        
        # Configura a animação
        ani = FuncAnimation(fig, update, frames=range(duracao),
                          init_func=init, blit=True, interval=1000)
        
        plt.tight_layout()
        plt.show()
        
        self.log("Monitoramento concluído")

    def mostrar_historico(self):
        """Exibe o histórico de eventos"""
        print("\nHistórico do Sistema:")
        for evento in self.historico[-10:]:  # Mostra os últimos 10 eventos
            print(evento)

# Simulação do sistema
if __name__ == "__main__":
    print("""\nSIMULADOR DE SISTEMA DE IRRIGAÇÃO EMBARCADO
----------------------------------------
Este programa simula um sistema de irrigação automático que:
1. Monitora a umidade do solo (simulado)
2. Ativa a bomba quando a umidade está baixa
3. Desliga após o tempo configurado
4. Registra todos os eventos em log
5. Mostra gráfico em tempo real\n""")
    
    sistema = SistemaIrrigacao()
    
    # Configurações personalizadas (opcional)
    config = input("Deseja alterar as configurações padrão? (s/n): ").lower()
    if config == 's':
        sistema.umidade_minima = float(input("Nova umidade mínima (%): "))
        sistema.tempo_irrigacao = int(input("Tempo de irrigação (segundos): "))
        sistema.intervalo_verificacao = int(input("Intervalo de verificação (segundos): "))
    
    duracao = int(input("\nDuração da simulação (segundos, recomendado 300): "))
    
    try:
        sistema.monitorar(duracao)
    except KeyboardInterrupt:
        sistema.log("Simulação interrompida pelo usuário")
    finally:
        sistema.mostrar_historico()