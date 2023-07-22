#!/bin/bash

docker-compose up -d

# Criar um diretório com base na data atual (formato: YYYY-MM-DD)
output_dir="/data/$(date +%Y-%m-%d)"

# Criar o diretório se ainda não existir
mkdir -p $output_dir

# Passo 1: Executar o script para extrair dados do banco de dados Postgres
python3 extract_postgres.py > "$output_dir/postgres_output.txt"

# Passo 2: Executar o script para extrair dados do arquivo CSV
python3 extract_csv.py > "$output_dir/csv_output.txt"

# Passo 3: Executar o script para carregar dados no banco de dados final
python3 load_to_final_db.py > "$output_dir/load_output.txt"
