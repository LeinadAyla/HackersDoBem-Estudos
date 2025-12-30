# 🛡️ LAUDO PERICIAL DE INFRAESTRUTURA DIGITAL E SEGURANÇA DA INFORMAÇÃO

**PROCESSO REF:** INCIDENTE #20251230-001  
**DATA DO FATO:** 30/12/2025  
**HORÁRIO:** 18:36:46 (UTC)  
**PERITO RESPONSÁVEL:** LeinadAyla (Engenharia de Software / Forense Digital)  
**OBJETO:** Constatação de invasão de banco de dados via técnica de SQL Injection (SQLi)

---

## 1. PREÂMBULO (Resumo para Não Especialistas)

Este laudo pericial tem por finalidade documentar a exploração de uma vulnerabilidade sistêmica que possibilitou o acesso não autorizado a dados sensíveis.

Em termos simplificados, o agente malicioso utilizou comandos próprios da linguagem de banco de dados, disfarçados como texto comum, para subverter os mecanismos de validação da aplicação. Como resultado, informações de terceiros — que deveriam estar protegidas por sigilo — foram indevidamente expostas.

---

## 2. METODOLOGIA E CADEIA DE CUSTÓDIA

A coleta das evidências digitais observou rigorosamente os princípios da integridade, autenticidade e rastreabilidade da prova técnica.

- **Procedimento:** Espelhamento e análise de registros de eventos (*logs*) em tempo real do servidor afetado.  
- **Ambiente:** Infraestrutura Docker sobre sistema Debian, em ambiente controlado.  
- **Integridade da Prova:** Os registros analisados são imutáveis e foram coletados no exato momento da transação maliciosa, garantindo a preservação da cadeia de custódia.

---

## 3. DESCRIÇÃO TÉCNICA DO ILÍCITO (Prova Material)

O vetor de ataque identificado foi **SQL Injection (SQLi)**, técnica amplamente conhecida por explorar falhas na validação de entradas de dados em aplicações web.

O agente inseriu, no campo destinado à identificação de usuários, uma instrução maliciosa com o objetivo de alterar a lógica da consulta SQL executada pelo sistema.

### 3.1 Evidência Digital (Rastro no Servidor)

O trecho abaixo, extraído dos arquivos de log do servidor, constitui a **impressão digital técnica** do acesso indevido:

```text
172.17.0.1 - - [30/Dec/2025:18:36:46 +0000] "GET /vulnerabilities/sqli/?id=1%27+OR+%271%27%3D%271&Submit=Submit HTTP/1.1" 200 1854

### 3.2 Análise dos Indicadores para Fins Judiciais

A decomposição técnica do registro evidencia, de forma inequívoca, a materialidade e o dolo do ato:

- **Intencionalidade (`%27+OR+%271%27%3D%271`):**  
  Não se trata de erro de digitação. O uso de operadores lógicos codificados em *URL Encoding* demonstra clara intenção de contornar filtros de segurança e manipular a consulta SQL.

- **Sucesso da Incursão (Status HTTP `200`):**  
  O servidor confirmou o processamento da requisição, indicando que o comando malicioso foi aceito e executado com êxito.

- **Volume de Dados Exfiltrados (`1854 bytes`):**  
  Um acesso legítimo retornaria aproximadamente 300 bytes (um único registro). O volume observado comprova a extração simultânea de múltiplos registros sigilosos.

---

## 4. CONCLUSÃO PERICIAL

Com base nas evidências técnicas analisadas, conclui-se que:

- Houve acesso indevido a dispositivo informático, com violação da integridade e confidencialidade dos dados.
- O método empregado exige conhecimento técnico especializado, reforçando o caráter doloso da conduta.
- A prova material apresentada (logs do servidor) é inequívoca quanto à cronologia, autoria técnica e método utilizado para a exploração da vulnerabilidade.

---

## 5. RECOMENDAÇÕES DE COMPLIANCE E SEGURANÇA (LGPD)

Visando a mitigação de riscos futuros e a conformidade com a Lei Geral de Proteção de Dados (LGPD), recomenda-se:

- Implementação obrigatória de **Prepared Statements** (consultas parametrizadas) em nível de código.
- Emprego de **Web Application Firewall (WAF)** para bloqueio de padrões maliciosos e caracteres de escape.
- Realização de **auditorias periódicas de logs**, com foco na detecção precoce de anomalias volumétricas e comportamentais.

---

## ASSINATURA DIGITAL

**LeinadAyla**  
Engenheiro de Software | Analista Forense Digital  

---

*Documentação gerada exclusivamente para fins instrucionais — Curso Hackers do Bem.*
