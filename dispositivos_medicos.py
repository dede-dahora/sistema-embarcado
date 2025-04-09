import random
import time

def dispositivo_medico():
    # Valores iniciais
    paciente = {
        'freq_card': 72,
        'pressao': (120, 80),
        'oxigenio': 98,
        'temp': 36.5
    }
    
    # Limites normais
    limites = {
        'freq_min': 60,
        'freq_max': 100,
        'pressao_sis_max': 140,
        'pressao_dia_max': 90,
        'oxigenio_min': 95,
        'temp_min': 36.0,
        'temp_max': 37.5
    }
    
    try:
        while True:
            # Atualiza os sinais vitais
            paciente['freq_card'] += random.randint(-2, 2)
            paciente['pressao'] = (
                paciente['pressao'][0] + random.randint(-3, 3),
                paciente['pressao'][1] + random.randint(-2, 2)
            )
            paciente['oxigenio'] += random.randint(-1, 1)
            paciente['temp'] += random.uniform(-0.1, 0.1)
            
            # Verifica alarmes
            alarmes = []
            if paciente['freq_card'] < limites['freq_min']:
                alarmes.append("FREQUÊNCIA CARDÍACA BAIXA")
            elif paciente['freq_card'] > limites['freq_max']:
                alarmes.append("FREQUÊNCIA CARDÍACA ALTA")
                
            if paciente['pressao'][0] > limites['pressao_sis_max']:
                alarmes.append("PRESSÃO SIS. ALTA")
            if paciente['pressao'][1] > limites['pressao_dia_max']:
                alarmes.append("PRESSÃO DIA. ALTA")
                
            if paciente['oxigenio'] < limites['oxigenio_min']:
                alarmes.append("OXIGÊNIO BAIXO")
                
            if paciente['temp'] < limites['temp_min']:
                alarmes.append("TEMPERATURA BAIXA")
            elif paciente['temp'] > limites['temp_max']:
                alarmes.append("TEMPERATURA ALTA")
            
            # Exibe os dados
            print("\n" * 50)  # Limpa a tela
            print("=== MONITOR MÉDICO ===")
            print(f"Frequência Cardíaca: {paciente['freq_card']} bpm")
            print(f"Pressão Arterial: {paciente['pressao'][0]}/{paciente['pressao'][1]} mmHg")
            print(f"Oxigenação: {paciente['oxigenio']}%")
            print(f"Temperatura: {paciente['temp']:.1f}°C")
            
            if alarmes:
                print("\nALARMES:")
                for alarme in alarmes:
                    print(f"⚠ {alarme}")
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado.")

# Inicia o sistema
dispositivo_medico()