#!/usr/bin/env python3
import os

def check_security():
    print("🚀 Iniciando Auditoria de Permissões Críticas...")
    # O arquivo /etc/shadow nunca deve ser legível por usuários comuns
    file_path = "/etc/shadow"
    
    # os.R_OK é a constante correta para verificar permissão de leitura
    if os.access(file_path, os.R_OK):
        print("🚨 ALERTA DE SEGURANÇA: O arquivo /etc/shadow está exposto (Leitura permitida)!")
    else:
        print("✅ SUCESSO: O arquivo /etc/shadow está protegido contra leitura não autorizada.")

if __name__ == "__main__":
    check_security()