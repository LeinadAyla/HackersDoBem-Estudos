# Módulo 1: Gerenciamento de Vulnerabilidades

## 1. Conceitos Fundamentais

### CVE (Common Vulnerabilities and Exposures)
- **O que é:** Um dicionário internacional de vulnerabilidades conhecidas publicamente.
- **Formato:** `CVE-ANO-NÚMERO` (Ex: CVE-2023-4567).
- **Importância:** Padroniza a comunicação global sobre falhas de segurança.

### CVSS (Common Vulnerability Scoring System)
- **O que é:** Sistema de pontuação (0.0 a 10.0) para priorização de riscos.
- **Métricas:** Base (impacto), Temporal (maturidade do exploit) e Ambiental (relevância para o negócio).

## 2. Técnicas de Verificação (Scanners)

### Varredura Não Intrusiva (Passiva)
- Identificação de portas e serviços com baixo impacto sistêmico.
- **Banner Grabbing:** Técnica de coleta da string de boas-vindas de um serviço para extração de versão. Fundamental para o mapeamento inicial de vulnerabilidades (Reconnaissance).

### Varredura Intrusiva (Ativa)
- Interação profunda ou tentativa de exploração de falhas.
- **Risco:** Pode causar negação de serviço (DoS) ou instabilidade.

### Varredura Credenciada vs. Não Credenciada
- **Não Credenciada:** Perspectiva do atacante externo (caixa-preta).
- **Credenciada:** Auditoria interna completa (configurações e patches).

## 3. Resultados de Análise

- **Falso Positivo:** Alerta de falha inexistente (gera ruído operacional).
- **Falso Negativo:** Falha real não detectada (risco crítico de segurança).

## 4. Laboratório de Campo (Comandos Kali)

- **Identificar Serviços:** `nmap -sV [IP]`
- **Extração de Banner:** `python3 laboratorio.py`
- **Mapeamento de Exploits:** `searchsploit [Versão_do_Serviço]`

---

## 5. Relatório de Atividade Prática: Banner Grabbing

**Data:** 30/12/2025  
**Alvo:** `scanme.nmap.org` (Serviço: SSH - Porta 22)

### 5.1 Coleta de Dados
Através do script customizado `laboratorio.py`, foi realizada a conexão via Socket e a extração do seguinte banner:
> `SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13`

### 5.2 Análise de Vulnerabilidades (Vulnerability Mapping)
Utilizando a ferramenta `searchsploit` para correlacionar a versão identificada com a base de dados do *Exploit-DB*, foram identificados os seguintes vetores de ataque:

| Vulnerabilidade | Identificador | Impacto |
| :--- | :--- | :--- |
| **User Enumeration** | CVE-2018-15473 | Permite descobrir nomes de usuários válidos no sistema. |
| **Privilege Escalation** | EDB-ID: 40962 | Possibilidade de ganho de privilégios root localmente. |
| **Arbitrary Library Loading** | EDB-ID: 40963 | Execução de código arbitrário via protocolo de agente. |

### 5.3 Conclusão Técnica
O serviço alvo está executando uma versão de software obsoleta (OpenSSH 6.6.1). A exposição deste banner facilita o reconhecimento para um atacante, permitindo a seleção de exploits específicos. **Recomendação:** Atualizar o serviço para a versão estável mais recente e desabilitar a exibição de banners detalhados.

---
*Notas de laboratório desenvolvidas por **LeinadAyla** - Estudos Hackers do Bem.*