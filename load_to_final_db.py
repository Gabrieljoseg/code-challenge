import psycopg2

def load_to_final_db():
    # Conexão com o banco de dados final (por exemplo, outro banco de dados Postgres)
    conn = psycopg2.connect(
    host="db",  # Nome do serviço no Docker Compose
    database="northwind",
    user="northwind_user",
    password="thewindisblowing"
    )

     # Criar tabela para o arquivo CSV
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_details (
                order_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                unit_price NUMERIC,
                -- Adicione outras colunas do CSV aqui, se necessário
                PRIMARY KEY (order_id, product_id),
                FOREIGN KEY (order_id) REFERENCES orders (order_id),
                FOREIGN KEY (product_id) REFERENCES products (product_id)
            );
        """)

    # Carregar dados do arquivo CSV para a tabela order_details no banco de dados final
    with open(f"/order_details.csv", "r") as file:
        with conn.cursor() as cursor:
            cursor.copy_expert(f"COPY order_details FROM STDIN WITH (FORMAT CSV, HEADER, DELIMITER ',')", file)

    # Carregar dados do arquivo CSV para a tabela orders no banco de dados final
    with open("/data/csv/2023-07-22/file.format", "r") as file:
        with conn.cursor() as cursor:
            cursor.copy_from(file, "orders", sep=",", columns=["order_id", "column1", "column2"])  # Substitua column1 e column2 pelos nomes das colunas do arquivo CSV

    # Carregar dados das tabelas do banco de dados Postgres para o banco de dados final
    tables = ["orders", "customers", "products"]  # Adicione outras tabelas, se necessário

    for table in tables:
        with open(f"/data/postgres/{table}/2021-01-01/file.format", "r") as file:
            with conn.cursor() as cursor:
                cursor.copy_from(file, table, sep=",")  # Substitua pelo nome correto das colunas, se necessário

    # Efetivar as alterações no banco de dados
    conn.commit()

    # Fechar a conexão com o banco de dados
    conn.close()

if __name__ == "__main__":
    load_to_final_db()
