# 🛡️ Relatório de Auditoria: Quebra de Credenciais Off-line (John the Ripper)

**ID do Lab:** #20251230-004  
**Analista:** LeinadAyla  
**Ambiente:** Kali Linux (Ataque de Dicionário)  
**Ferramenta:** John the Ripper v1.9.0  

---

## 1. Resumo Executivo
Este relatório documenta a fragilidade de credenciais sistêmicas quando submetidas a ataques de força bruta/dicionário. O objetivo foi recuperar a senha em texto claro a partir do hash extraído do arquivo `/etc/shadow`, simulando um cenário de pós-exploração.

## 2. Coleta de Prova Material (Hash Analysis)
Foi identificada a seguinte entrada no banco de dados de senhas do sistema:

```text
teste1:$1$H6qvteqS$dZ84C5VJ0rWJ9YWoVAUNP1:19838:0:99999:7:::