# Módulo 3: Identificação de Ameaças e Análise de Logs

## 1. Localização e Arquitetura de Logs
- **Sistemas Tradicionais:** Os logs são arquivos de texto em `/var/log/auth.log`.
- **Sistemas Modernos (WSL/Systemd):** Utilizam o banco de dados binário do `systemd-journald`.
- **Comando Principal:** `journalctl` (substitui o uso de `tail` e `cat` em arquivos inexistentes).

## 2. Comandos de Análise Prática (Journalctl)
- `sudo journalctl -n 20`: Mostra as últimas 20 entradas do log.
- `sudo journalctl -f`: Monitoramento em tempo real (Live Feed).
- `sudo journalctl -p err`: Filtra apenas erros críticos e falhas de sistema.
- `sudo journalctl --since "10:00"`: Filtra eventos a partir de um horário específico.
- `sudo journalctl | grep "sudo"`: Identifica quem utilizou privilégios de administrador.

## 3. Anatomia de um Log de Segurança
Ao analisar uma linha de log, identificamos:
1. **Timestamp:** Data e hora do evento.
2. **Hostname:** Nome da máquina de origem.
3. **Processo:** Serviço que gerou o registro (ex: `sudo`, `kernel`, `CRON`).
4. **Mensagem:** Descrição detalhada da atividade ou erro.

## 4. Indicadores de Comprometimento (IoC) em Logs
- Múltiplas mensagens de `password failure` em curto tempo (Brute Force).
- Sessões abertas para o usuário `root` em horários atípicos.
- Comandos `sudo` desconhecidos executados por usuários comuns.

---
*Notas de laboratório desenvolvidas por **LeinadAyla** - Foco em Identificação de Ameaças.*