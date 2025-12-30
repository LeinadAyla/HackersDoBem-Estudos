import re

# Simulação de análise de logs para identificar SQL Injection
def analisar_log(linha_log):
    # Padrões comuns de SQL Injection (URL Encoded)
    padroes_suspeitos = [
        r"%27",      # Aspa simples (')
        r"OR",       # Operador OR
        r"%3D",      # Sinal de igual (=)
        r"UNION",    # Comando UNION
        r"SELECT"    # Comando SELECT
    ]
    
    print(f"🔍 Analisando evento: {linha_log[:50]}...")
    
    for padrao in padroes_suspeitos:
        if padrao.upper() in linha_log.upper():
            return f"🚨 ALERTA: Tentativa de SQL Injection detectada! Padrão encontrado: {padrao}"
    
    return "✅ Requisição normal."

# Exemplo da linha que você capturou no terminal
log_capturado = '172.17.0.1 - - [30/Dec/2025:18:36:46 +0000] "GET /vulnerabilities/sqli/?id=1%27+OR+%271%27%3D%271&Submit=Submit HTTP/1.1" 200 1854'

resultado = analisar_log(log_capturado)
print("-" * 50)
print(resultado)
print("-" * 50)