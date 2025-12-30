# 🛡️ Jornada Hackers do Bem - Estudos de Cibersegurança

Repositório dedicado ao armazenamento de notas de aula, laboratórios práticos e scripts desenvolvidos durante o curso **Hackers do Bem** (Nível Intermediário).

## 🚀 Ambiente de Trabalho
- **Sistema Operacional:** Kali Linux (WSL2)
- **IDE:** Visual Studio Code
- **Linguagens:** Python, Shell Script
- **Tecnologias:** Docker, Git

## 📂 Estrutura do Repositório

### [Módulo 1] - Princípios de Segurança e Engenharia Social
Conteúdo focado em entender quem são os atacantes e como eles manipulam o fator humano.

- **Aula 3: Inteligência de Ameaças**
  - Estudo sobre Black, White e Gray Hat Hackers.
  - Análise de Superfície de Ataque.
  - Arquivo: `intel_fontes.md` (Minhas notas sobre fontes de OSINT).

- **Aula 4: Engenharia Social**
  - Técnicas de Phishing, Vishing e Personificação.
  - **Lab Prático:** `analisador_phishing.py`
    - Um script em Python que identifica gatilhos psicológicos (Urgência, Autoridade) em mensagens suspeitas.

---

## 🛠️ Como rodar os scripts
Para testar o analisador de phishing:
```bash
python3 modulo1-teoria-e-labs/analisador_phishing.py