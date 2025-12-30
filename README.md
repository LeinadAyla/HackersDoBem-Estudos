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
- **Aula 4 (Lab Prático):** `analisador_phishing.py` -> Script Python que detecta gatilhos psicológicos em mensagens fraudulentas.

### [Módulo 3] - Defesa Cibernética e Resposta a Incidentes
Focado em análise de logs, monitoramento e perícia digital.
- **Análise Forense de SQL Injection:**
  - **Lab Prático:** Exploração controlada em ambiente Docker (DVWA).
  - **Documentação:** [Laudo Pericial Jurídico](modulo3-analise-logs-sqli/poc_sqli.md) detalhando IoCs, status HTTP e anomalias de tráfego.

### [Módulo 4] - Gestão de Identidade e Criptografia
Focado em controle de acesso, proteção de sistemas e auditoria de credenciais.
- **Auditoria de Senhas (John the Ripper):** - [Relatório de Auditoria](modulo4-autenticacao-e-criptografia/auditoria_senhas_john.md) demonstrando a quebra de hashes offline em algoritmos legados (MD5).
- **Hardening de Sistema:** Ativação e análise do **SELinux** para controle de acesso obrigatório (MAC).
- **Tooling:** `analisador_shadow.py` -> Script de auditoria que valida a integridade e permissões do arquivo `/etc/shadow`.

---

## 🛠️ Ferramentas de Automação (DevSecOps)

Desenvolvi ferramentas para otimizar o fluxo de trabalho e gerenciamento do laboratório:

1. **`reset_lab.sh`**: Script Bash para automação de infraestrutura e limpeza de portas (80/TCP).
2. **`gerar_aula.sh`**: Script de automação para padronização da estrutura de diretórios do repositório.

---

## ⚡ Como Executar os Laboratórios

### 1. Auditoria de Senhas (Módulo 4):
```bash
cd modulo4-autenticacao-e-criptografia
python3 analisador_shadow.py
john --format=crypt credencial.txt