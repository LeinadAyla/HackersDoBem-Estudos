# 🛡️ Jornada Hackers do Bem - Estudos de Cibersegurança

Repositório dedicado ao armazenamento de notas de aula, laboratórios práticos, scripts de automação e perícia forense desenvolvidos durante o curso **Hackers do Bem**.

## 🚀 Perfil e Ambiente de Trabalho
- **Analista Responsável:** LeinadAyla (Engenharia de Software / Cyber Security)
- **Sistema Operacional:** Kali Linux (WSL2)
- **Stack Tecnológica:** Python, Shell Script, Docker, Git.

---

## 📂 Estrutura do Repositório

### [Módulo 1] - Princípios de Segurança e Engenharia Social
Focado no fator humano e inteligência de ameaças.
- **Aula 3:** Inteligência de Ameaças (OSINT) e análise de superfície de ataque.
- **Aula 4 (Lab Prático):** `analisador_phishing.py` -> Script Python que detecta gatilhos psicológicos em mensagens fraudulentas.

### [Módulo 3] - Defesa Cibernética e Resposta a Incidentes
Focado em análise de logs, monitoramento e perícia digital.
- **Análise Forense de SQL Injection:**
  - **Lab Prático:** Exploração controlada em ambiente Docker (DVWA).
  - **Documentação:** [Laudo Pericial Jurídico](modulo3-analise-logs-sqli/poc_sqli.md) detalhando IoCs (Indicadores de Comprometimento), status HTTP e anomalias de tráfego.
  - **Identificação:** Decodificação de *URL Encoding* (`%27`, `%3D`) para fins de compliance e evidência criminal.

---

## 🛠️ Ferramentas de Automação (DevSecOps)

Desenvolvi ferramentas para otimizar o fluxo de trabalho e gerenciamento do laboratório:

1.  **`reset_lab.sh`**: Script Bash avançado para automação de infraestrutura.
    - Realiza o *kill* de processos em portas específicas (80/TCP).
    - Reinicia containers Docker de forma limpa.
    - Garante a integridade do ambiente antes de cada perícia.
2.  **`gerar_aula.sh`**: Automação da estrutura de diretórios para manter o repositório organizado e escalável.

---

## ⚡ Como Executar os Laboratórios

### Monitorar Logs em Tempo Real:
```bash
./reset_lab.sh

Rodar Analisador de Phishing (Python):
Bash

python3 modulo1-teoria-e-labs/analisador_phishing.py

Este repositório serve como portfólio técnico para demonstração de habilidades em Red Team (Exploração), Blue Team (Defesa) e Compliance Digital.