# Analisador Simples de Engenharia Social
print("--- Verificador de Suspeita de Phishing ---")

mensagem = input("Cole aqui o texto do e-mail ou SMS: ").lower()

# Palavras-chave baseadas nos princípios de Urgência e Autoridade
gatilhos = ["urgente", "bloqueio", "senha", "clique aqui", "recadastramento", "policia", "banco"]

suspeita = 0
for gatilho in gatilhos:
    if gatilho in mensagem:
        print(f"[!] Gatilho encontrado: {gatilho}")
        suspeita += 1

if suspeita > 0:
    print(f"\nRESULTADO: Esta mensagem tem {suspeita} pontos de suspeita. Cuidado!")
else:
    print("\nRESULTADO: Nenhum gatilho óbvio encontrado.")