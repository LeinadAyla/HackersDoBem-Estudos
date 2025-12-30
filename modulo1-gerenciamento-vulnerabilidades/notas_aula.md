# Módulo 1: Gerenciamento de Vulnerabilidades

## 1. Conceitos Fundamentais

### CVE (Common Vulnerabilities and Exposures)
- **O que é:** Um dicionário internacional de vulnerabilidades conhecidas publicamente.
- **Formato:** `CVE-ANO-NÚMERO` (Ex: CVE-2023-4567).
- **Importância:** Padroniza a comunicação. Quando um analista fala de uma CVE, todos os sistemas e ferramentas sabem exatamente de qual falha ele está falando.

### CVSS (Common Vulnerability Scoring System)
- **O que é:** Um sistema de pontuação de 0.0 a 10.0 que define a gravidade da falha.
- **Métricas Principais:**
    - **Base:** Gravidade intrínseca (Quão fácil é explorar? Qual o impacto?).
    - **Temporal:** O status atual (Tem patch? Tem exploit público?).
    - **Ambiental:** O contexto da sua rede (O servidor está exposto à internet?).
- **Regra de Priorização:** Nem sempre o maior score é o primeiro. Um CVSS 7.0 em um servidor crítico de pagamentos pode ser mais perigoso que um 9.0 em uma máquina de teste isolada.

## 2. Técnicas de Verificação (Scanners)

### Varredura Não Intrusiva (Passiva)
- Apenas identifica portas e serviços.
- Baixo risco de queda do sistema.
- **Ferramenta:** `nmap -sS` (SYN Scan).
- **Banner Grabbing:** Técnica para identificar a versão exata de um serviço através da resposta inicial da conexão. Com essa versão, consultamos a base CVE para verificar se o alvo possui vulnerabilidades conhecidas sem precisar realizar um ataque intrusivo.

### Varredura Intrusiva (Ativa)
- Tenta explorar a falha ou interagir profundamente com o serviço.
- Pode causar instabilidade ou DoS (Negação de Serviço) acidental.
- Deve ser feita em janelas de manutenção.
- **Ferramenta:** `nmap -sV -sC` ou scripts agressivos.

### Varredura Credenciada vs. Não Credenciada
- **Não Credenciada:** Visão do atacante externo (vê apenas o que está exposto).
- **Credenciada:** Visão interna (usa login/senha para ver falhas de configuração e patches faltando dentro do SO).

## 3. Resultados de Análise

- **Falso Positivo:** A ferramenta diz que tem um buraco, mas ele não existe (perda de tempo).
- **Falso Negativo:** A ferramenta diz que está tudo bem, mas existe uma falha real (**Cenário mais perigoso: gera falsa sensação de segurança**).

## 4. Laboratório de Campo (Comandos Kali)

- **Identificar Serviços:** `nmap -sV [IP]`
- **Banner Grabbing (Python):** `python3 laboratorio.py` (Script customizado para extração de versão).
- **Buscar Vulnerabilidades:** `searchsploit "Nome do Serviço"`
- **Validar Integridade (Forense):** `sha256sum arquivo.txt`
- **Proteção de Dados:** `gpg -c --pinentry-mode loopback arquivo.txt`

---
*Notas geradas durante a aula prática no Kali Linux por LeinadAyla.*