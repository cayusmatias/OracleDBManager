import oracledb
import os
import dotenv
import time
from colorama import Fore, init


class OracleDBManager:
    def __init__(self):
        init(autoreset=True)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        dotenv.load_dotenv()

        try:
            self.connection = oracledb.connect(
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                dsn=os.getenv("DB_DSN"),
                config_dir=os.path.join(BASE_DIR, "Wallet_Oracle"),
                wallet_location=os.path.join(BASE_DIR, "Wallet_Oracle"),
                wallet_password=os.getenv("DB_WALLET_PASSWORD")
            )
        except oracledb.DatabaseError as e:
            print(Fore.RED + f"Erro ao conectar ao banco de dados: {e}")

    def cria_tabela_se_nao_existe(self, tabela, colunas):
        with self.connection.cursor() as cursor:
            # Verificar se a tabela já existe
            cursor.execute("SELECT COUNT(*) FROM ALL_TABLES WHERE TABLE_NAME = :tabela",
                           {"tabela": tabela.upper()})

            if cursor.fetchone()[0] == 0:
                # Construir a parte da definição da coluna da consulta SQL
                col_defs = ", ".join(f"{col} {tipo}" for col, tipo in colunas.items())

                # Criar a tabela
                sql = f"CREATE TABLE {tabela} ({col_defs})"
                cursor.execute(sql)

                print(f"Tabela {tabela} criada com sucesso!")

    def executa_acao_bd(self, acao, tabela):
        with self.connection.cursor() as cursor:
            if acao == "LISTAR":
                cursor.execute(f"SELECT * FROM {tabela}")
                for row in cursor:
                    print(f"ID: {row[0]} - DADO: {row[1]}")
                return "Listagem realizada com sucesso!"

            if acao == "TRUNCATE":
                cursor.execute(f"TRUNCATE TABLE {tabela}")
                return "Tabela truncada com sucesso!"

            if acao == "POVOAMENTO_UM_A_UM":
                query = f"INSERT INTO {tabela} (ID, DATA) VALUES (:indice, :dado)"
                for indice, dado in enumerate(range(10)):
                    params = {'indice': indice, 'dado': f'Hello World {dado}'}
                    cursor.execute(query, params)
                cursor.execute("commit")
                return "Povoamento realizado com sucesso!"

            if acao == "POVOAMENTO":
                dados = range(15)
                chunk_size = 5
                for i in range(0, len(dados), chunk_size):
                    chunk = dados[i:i+chunk_size]
                    print(f"Chunk: {chunk}")
                    values = " ".join(f"INTO {tabela} VALUES ({index}, 'Hello World {dado}')" for index, dado in enumerate(chunk, start=i))
                    sql = f"INSERT ALL {values} SELECT * FROM dual"
                    cursor.execute(sql)
                cursor.execute("commit")
                return "Povoamento realizado com sucesso!"

    def lista_colunas(self, tabela):
        sql = f"""SELECT COLUMN_NAME
        FROM ALL_TAB_COLUMNS
        WHERE TABLE_NAME = '{tabela}'
        ORDER BY COLUMN_ID"""
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            for row in cursor:
                print(row)

    def lista_tabelas(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT table_name FROM all_tables")
            for row in cursor:
                print(row)

    def drop_tabela(self, tabela):
        with self.connection.cursor() as cursor:
            cursor.execute(f"DROP TABLE {tabela}")
            cursor.execute("commit")
            print(f"Tabela {tabela} apagada com sucesso!")

    def close(self):
        self.connection.close()
