#!/bin/bash

# Script para restaurar o ambiente DVWA no Kali-WSL
# Criado por: LeinadAyla

echo "🚀 Iniciando processo de recuperação do laboratório..."

# 1. Verifica se o Docker está instalado
if ! command -v docker &> /dev/null
then
    echo "❌ Docker não encontrado. Instalando..."
    sudo apt update && sudo apt install -y docker.io
else
    echo "✅ Docker já está instalado."
fi

# 2. Garante que o serviço do Docker está rodando
echo "⚙️ Iniciando o serviço Docker..."
sudo service docker start

# 3. Pega o IP do WSL para facilitar o acesso
IP_WSL=$(hostname -I | awk '{print $1}')

echo "-------------------------------------------------------"
echo "🌐 SEU LABORATÓRIO ESTARÁ DISPONÍVEL EM:"
echo "👉 http://localhost"
echo "👉 http://$IP_WSL"
echo "-------------------------------------------------------"
echo "🔑 LOGIN: admin | SENHA: password"
echo "⚠️  Não esqueça de clicar em 'Create / Reset Database' no primeiro acesso."
echo "-------------------------------------------------------"

# 4. Roda o container (se já houver um rodando, ele avisa)
echo "🐳 Subindo o container DVWA..."
sudo docker run --rm -it -p 80:80 vulnerables/web-dvwa