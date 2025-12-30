#!/bin/bash

# Script para automatizar a criação de módulos do Hackers do Bem
echo "Hacker do Bem - Gerador de Estrutura de Aula"
read -p "Número do Módulo: " MODULO
read -p "Nome do Módulo (use-hifens): " NOME_MOD

PASTA="modulo${MODULO}-${NOME_MOD}"

mkdir -p "$PASTA"
touch "$PASTA/notas_aula.md"
touch "$PASTA/laboratorio.py"

echo "# Módulo $MODULO: $NOME_MOD" > "$PASTA/notas_aula.md"
echo "## Resumo da Aula 01" >> "$PASTA/notas_aula.md"

echo "✅ Estrutura criada com sucesso na pasta: $PASTA"
ls -R "$PASTA"