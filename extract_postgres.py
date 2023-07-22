import psycopg2

def extract_from_postgres():
    # Conexão com o banco de dados Postgres
    conn = psycopg2.connect(
    host="db",  # Nome do serviço no Docker Compose
    database="northwind",
    user="northwind_user",
    password="thewindisblowing"
        )

    # Defina as tabelas que você deseja extrair
    tables = ["orders", "customers", "products"]  # Adicione outras tabelas, se necessário

    for table in tables:
        # Execute a consulta SQL para extrair os dados da tabela
        query = f"SELECT * FROM {table};"
        with conn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        # Escreva os dados no arquivo
        with open(f"/data/postgres/{table}/2021-01-01/file.format", "w") as file:
            for row in rows:
                file.write(",".join(str(cell) for cell in row) + "\n")

    # Feche a conexão com o banco de dados
    conn.close()

if __name__ == "__main__":
    extract_from_postgres()
