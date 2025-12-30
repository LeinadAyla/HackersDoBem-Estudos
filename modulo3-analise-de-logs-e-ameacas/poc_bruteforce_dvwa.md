# 🛡️ Relatório de Laboratório: Detecção de Brute Force

**Data:** 30/12/2025  
**Ambiente:** DVWA (Docker) em Kali Linux (WSL2)  
**Nível de Segurança:** Low  

## 1. Objetivo
Simular um ataque de força bruta no formulário de login do DVWA e identificar como esse ataque é registrado nos logs do servidor web (Apache).

## 2. Metodologia (O Ataque)
1. Acessei o módulo **Brute Force** do DVWA.
2. Realizei tentativas sucessivas de login com usuários e senhas incorretas:
   - Tentativa 1: `admin` / `123456`
   - Tentativa 2: `hacker` / `password`
   - Tentativa 3: `root` / `root`

## 3. Análise de Logs (A Identificação da Ameaça)
Ao monitorar o terminal do Docker (STDOUT), identifiquei as seguintes entradas de log correspondentes ao ataque:

```text
172.17.0.1 - - [30/Dec/2025:16:58:10] "GET /vulnerabilities/brute/?username=admin&password=123456&Login=Login HTTP/1.1" 200
172.17.0.1 - - [30/Dec/2025:16:58:12] "GET /vulnerabilities/brute/?username=hacker&password=password&Login=Login HTTP/1.1" 200
172.17.0.1 - - [30/Dec/2025:16:58:15] "GET /vulnerabilities/brute/?username=root&password=root&Login=Login HTTP/1.1" 200