import socket

# Cores para o terminal
VERMELHO = '\033[91m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
RESET = '\033[0m'

# Simulação de base de dados CVE (Vulnerabilidades Comuns)
BASE_CVE = {
    "21": "CVE-2023-1234 (Vulnerabilidade Crítica em FTP Antigo)",
    "22": "Configuração Segura (SSH)",
    "80": "CVE-2022-4567 (Servidor Web Desatualizado)",
    "445": "CVE-2017-0144 (EternalBlue - Risco de Ransomware)"
}

def scan_portas(alvo):
    print(f"\n{AMARELO}--- Iniciando Varredura Não Intrusiva em: {alvo} ---{RESET}")
    portas_comuns = [21, 22, 80, 445, 3306]
    
    for porta in portas_comuns:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((alvo, porta))
        
        if result == 0:
            status = f"{VERMELHO}ABERTA{RESET}"
            cve = BASE_CVE.get(str(porta), "Nenhuma CVE óbvia encontrada")
            print(f"[+] Porta {porta}: {status} -> {cve}")
        else:
            print(f"[-] Porta {porta}: FECHADA")
        sock.close()

if __name__ == "__main__":
    # Teste em localhost (sua própria máquina) para ser não-intrusivo
    alvo_teste = "127.0.0.1" 
    scan_portas(alvo_teste)
    print(f"\n{VERDE}Varredura concluída. Verifique os logs para evitar Falsos Positivos.{RESET}")