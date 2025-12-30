import socket

def capturar_banner(ip, porta):
    """
    Tenta conectar a um IP e porta para extrair o banner do serviço.
    """
    try:
        # Configurações do Socket
        socket.setdefaulttimeout(2)
        s = socket.socket()
        
        # Tentativa de conexão
        print(f"[*] Conectando em {ip}:{porta}...")
        s.connect((ip, porta))
        
        # Recebendo os dados (Banner)
        # O .decode().strip() limpa espaços e converte de bytes para texto
        banner = s.recv(1024).decode().strip()
        return banner
    except socket.timeout:
        return "Erro: Tempo de conexão esgotado (Timeout)."
    except ConnectionRefusedError:
        return "Erro: Conexão recusada pelo alvo."
    except Exception as e:
        return f"Erro inesperado: {str(e)}"
    finally:
        s.close()

# --- CONFIGURAÇÃO DO TESTE ---
# Alvo: scanme.nmap.org é um servidor seguro para testes de portas
alvo = "scanme.nmap.org" 
porta_alvo = 22 # SSH (Geralmente retorna banner)

# Execução
resultado = capturar_banner(alvo, porta_alvo)

print("-" * 30)
print(f"[+] Resultado do Banner: {resultado}")
print("-" * 30)