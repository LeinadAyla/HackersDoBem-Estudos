# Analisador de Engenharia Social com Cores
VERMELHO = '\033[91m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
RESET = '\033[0m'

print(f"{AMARELO}--- Verificador de Suspeita de Phishing ---{RESET}")

mensagem = input("Cole aqui o texto do e-mail ou SMS: ").lower()

gatilhos = ["urgente", "bloqueio", "senha", "clique aqui", "recadastramento", "policia", "banco"]

suspeita = 0
for gatilho in gatilhos:
    if gatilho in mensagem:
        print(f"{VERMELHO}[!] Gatilho encontrado: {gatilho}{RESET}")
        suspeita += 1

if suspeita > 0:
    print(f"\n{VERMELHO}RESULTADO: Esta mensagem tem {suspeita} pontos de suspeita. CUIDADO!{RESET}")
else:
    print(f"\n{VERDE}RESULTADO: Nenhum gatilho óbvio encontrado.{RESET}")