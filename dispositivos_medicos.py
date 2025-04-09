import random
import time
import sys

class DispositivoMedico:
    def __init__(self):
        self.paciente = {
            'frequencia_cardiaca': 72,
            'pressao_arterial': (120, 80),
            'oxigenacao': 98,
            'temperatura': 36.5
        }
        self.alarmes = []
        self.rodando = True

    def simular_sinais_vitais(self):
        """Simula variações nos sinais vitais do paciente"""
        while self.rodando:
            # Modifica os valores aleatoriamente dentro de faixas razoáveis
            self.paciente['frequencia_cardiaca'] += random.randint(-2, 2)
            self.paciente['pressao_arterial'] = (
                self.paciente['pressao_arterial'][0] + random.randint(-3, 3),
                self.paciente['pressao_arterial'][1] + random.randint(-2, 2)
            )
            self.paciente['oxigenacao'] += random.randint(-1, 1)
            self.paciente['temperatura'] += random.uniform(-0.1, 0.1)
            
            self.verificar_alarmes()
            time.sleep(1)

    def verificar_alarmes(self):
        """Verifica se algum parâmetro está fora da faixa normal"""
        self.alarmes = []  # Limpa alarmes anteriores
        
        # Verifica frequência cardíaca
        if self.paciente['frequencia_cardiaca'] < 60:
            self.alarmes.append("Bradicardia detectada!")
        elif self.paciente['frequencia_cardiaca'] > 100:
            self.alarmes.append("Taquicardia detectada!")
            
        # Verifica pressão arterial
        if self.paciente['pressao_arterial'][0] > 140:
            self.alarmes.append("Hipertensão sistólica!")
        if self.paciente['pressao_arterial'][1] > 90:
            self.alarmes.append("Hipertensão diastólica!")
            
        # Verifica oxigenação
        if self.paciente['oxigenacao'] < 95:
            self.alarmes.append("Hipoxemia detectada!")
            
        # Verifica temperatura
        if self.paciente['temperatura'] > 37.5:
            self.alarmes.append("Febre detectada!")
        elif self.paciente['temperatura'] < 36.0:
            self.alarmes.append("Hipotermia detectada!")

    def exibir_painel(self):
        """Exibe os sinais vitais em um painel simples"""
        while self.rodando:
            print("\n" * 50)  # Limpa a tela (simplificado)
            print("=== MONITOR MÉDICO SIMPLES ===")
            print(f"Frequência Cardíaca: {self.paciente['frequencia_cardiaca']} bpm")
            print(f"Pressão Arterial: {self.paciente['pressao_arterial'][0]}/{self.paciente['pressao_arterial'][1]} mmHg")
            print(f"Oxigenação: {self.paciente['oxigenacao']}%")
            print(f"Temperatura: {self.paciente['temperatura']:.1f}°C")
            
            # Mostra alarmes se houver
            if self.alarmes:
                print("\n=== ALARMES ===")
                for alarme in self.alarmes:
                    print(f"! {alarme} !")
            
            time.sleep(0.5)

    def executar(self):
        """Inicia a simulação"""
        try:
            # Inicia a simulação em threads separadas
            import threading
            sim_thread = threading.Thread(target=self.simular_sinais_vitais)
            disp_thread = threading.Thread(target=self.exibir_painel)
            
            sim_thread.start()
            disp_thread.start()
            
            # Aguarda até que o usuário pressione Enter para sair
            input("Pressione Enter para parar o monitoramento...\n")
            self.rodando = False
            
            sim_thread.join()
            disp_thread.join()
            
        except KeyboardInterrupt:
            self.rodando = False
            print("\nSistema desligado.")

if __name__ == "__main__":
    dispositivo = DispositivoMedico()
    dispositivo.executar()