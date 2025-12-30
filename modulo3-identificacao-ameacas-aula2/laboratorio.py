import time

# Cores para o terminal
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def analisar_vulnerabilidade(id_vuln, status_real, detectado_pelo_scanner):
    print(f"Analisando {id_vuln}...")
    time.sleep(1)
    
    if status_real and detectado_pelo_scanner:
        return f"{GREEN}[+] VERDADEIRO POSITIVO:{RESET} Falha real detectada com sucesso."
    elif not status_real and detectado_pelo_scanner:
        return f"{RED}[!] FALSO POSITIVO:{RESET} O scanner errou! A falha não existe (alerta desnecessário)."
    elif status_real and not detectado_pelo_scanner:
        return f"{RED}[!!!] FALSO NEGATIVO:{RESET} PERIGO! A falha existe mas o scanner não viu."
    else:
        return f"{GREEN}[V] VERDADEIRO NEGATIVO:{RESET} Sistema limpo e scanner correto."

print(f"{YELLOW}--- SIMULADOR DE ANÁLISE DE LOGS ---{RESET}\n")

# Caso 1: Scanner diz que tem falha, mas a configuração está correta (Revisão de Configuração)
print(analisar_vulnerabilidade("CVE-2023-456", status_real=False, detectado_pelo_scanner=True))

# Caso 2: Existe uma falha crítica, mas o scanner passou batido (Risco de Invasão)
print(analisar_vulnerabilidade("CVE-2024-001", status_real=True, detectado_pelo_scanner=False))

# Caso 3: O scanner achou uma falha que realmente está lá
print(analisar_vulnerabilidade("CVE-2022-999", status_real=True, detectado_pelo_scanner=True))