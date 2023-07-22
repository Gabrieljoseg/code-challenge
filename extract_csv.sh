#!/bin/bash

# Caminho para o arquivo CSV de entrada
input_csv="./data/order_details.csv"

# Obter a data atual
current_date=$(date +"%Y-%m-%d")  # Formato: YYYY-MM-DD

cd data/csv/

# Definir o caminho do diretório que deseja criar
nome_do_diretorio="${current_date}"

# Verificar se o diretório não existe antes de criá-lo
if [ ! -d "$nome_do_diretorio" ]; then
    mkdir -p "$nome_do_diretorio"
fi

# Caminho para o arquivo de saída
output_csv="${nome_do_diretorio}/order_details.csv"

# Ler o arquivo CSV e escrever os dados no arquivo com a data atual no caminho
cat "$input_csv" > "$output_csv"
