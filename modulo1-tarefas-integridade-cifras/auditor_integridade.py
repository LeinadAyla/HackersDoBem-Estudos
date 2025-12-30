import hashlib
import os

def gerar_hash(arquivo):
    with open(arquivo, "rb") as f:
        bytes = f.read()
        return hashlib.md5(bytes).hexdigest()

# Simulando a Atividade 1.1 e 1.2
print("--- Auditor de Integridade Hacker do Bem ---")

# Criando arquivos para teste
with open("original.txt", "w") as f: f.write("Hackers do Bem - Integridade Total")
with open("copia_identica.txt", "w") as f: f.write("Hackers do Bem - Integridade Total")
with open("copia_alterada.txt", "w") as f: f.write("Packers do Bem - Integridade Total")

arquivos = ["original.txt", "copia_identica.txt", "copia_alterada.txt"]

for arq in arquivos:
    hash_valor = gerar_hash(arq)
    print(f"Arquivo: {arq} | MD5: {hash_valor}")

# Comparação lógica
if gerar_hash("original.txt") == gerar_hash("copia_identica.txt"):
    print("\n✅ Original e Cópia são IDÊNTICOS.")
if gerar_hash("original.txt") != gerar_hash("copia_alterada.txt"):
    print("❌ ALERTA: A cópia alterada violou a INTEGRIDADE.")