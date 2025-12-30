# 🛡️ Configuração de Autenticação e Hardening (SELinux)

**ID do Lab:** #20251230-002
**Analista:** LeinadAyla
**Sistema:** Kali Linux

---

## 1. Modificação de Parâmetros de Autenticação
Foi realizada a auditoria nos arquivos críticos de controle de usuários:
- `/etc/passwd`: Identificação de UIDs (User ID) e GIDs (Group ID). O usuário `aluno` possui UID `1001`.
- `/etc/group`: Verificação de privilégios. O usuário `aluno` pertence ao grupo `sudo` (GID 27).

**Procedimento de Segurança:**
Alteração da credencial administrativa via comando `passwd`, validando a propagação de permissões no sistema.

---

## 2. Implementação de SELinux (Controle de Acesso Obrigatório)
O **SELinux (Security-Enhanced Linux)** foi ativado para elevar o nível de segurança de um modelo Discricionário (DAC) para um modelo **Obrigatório (MAC)**.



### Estados do SELinux observados:
- **Enforcing:** Bloqueio ativo de ações não autorizadas.
- **Permissive:** Apenas log de violações (Modo utilizado durante a ativação).
- **Status da Ativação:** `sestatus` confirmou o modo `permissive` após o *relabeling* do sistema de arquivos.

---
*Notas de laboratório - Atividade 4.1 e 4.2 - Hackers do Bem.*