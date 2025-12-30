#!/bin/bash

# =================================================================
# Script: reset_lab.sh
# Descrição: Restaura o ambiente DVWA no Kali-WSL via Docker
# Criado por: LeinadAyla (Engenheiro de Software)
# =================================================================

echo "🚀 Iniciando processo de recuperação do laboratório..."

# 1. Verificar/Instalar Docker
if ! command -v docker &> /dev/null
then
    echo "❌ Docker não encontrado. Instalando..."
    sudo apt update && sudo apt install -y docker.io
else
    echo "✅ Docker já está instalado."
fi

# 2. Iniciar Serviço Docker
echo "⚙️ Garantindo que o motor do Docker está rodando..."
sudo service docker start

# 3. Limpeza Preventiva (Evita o erro de 'Porta já alocada')
echo "🧹 Limpando possíveis conflitos na porta 80..."
# Para qualquer container que use a imagem do DVWA
docker stop $(docker ps -q --filter "ancestor=vulnerables/web-dvwa") 2>/dev/null || true
# Para o container pelo nome específico, se existir
docker stop dvwa 2>/dev/null || true
# Para o Apache nativo do Kali, caso esteja rodando
sudo service apache2 stop 2>/dev/null || true

# 4. Obter IP do WSL
IP_WSL=$(hostname -I | awk '{print $1}')

echo "-------------------------------------------------------"
echo "🌐 SEU LABORATÓRIO ESTARÁ DISPONÍVEL EM:"
echo "👉 http://localhost"
echo "👉 http://$IP_WSL"
echo "-------------------------------------------------------"
echo "🔑 LOGIN: admin | SENHA: password"
echo "⚠️  AÇÃO NECESSÁRIA: Clique em 'Create / Reset Database'"
echo "-------------------------------------------------------"

# 5. Execução do Container
echo "🐳 Subindo o container DVWA..."
# --name dvwa: facilita identificação
# --rm: remove o container ao fechar, mantendo o sistema limpo
# -it: modo interativo para você ver os LOGS em tempo real
sudo docker run --rm -it -p 80:80 --name dvwa vulnerables/web-dvwa