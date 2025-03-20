import mysql.connector
from mysql.connector import Error

#pip install mysql-connector-python

class Database:
    def __init__(self):
        # Configurações do banco de dados
        self.MYSQL_HOST = "localhost"
        self.MYSQL_USER = "root"
        self.MYSQL_PASSWORD = ""
        self.MYSQL_DATABASE = "farmacia_sa"

        # Inicializa o banco de dados e cria a tabela, se não existir
        self.initialize_database()

    def get_connection(self):
        # Criar uma conexão com o banco de dados
        try:
            connection = mysql.connector.connect(
                host=self.MYSQL_HOST,
                user=self.MYSQL_USER,
                password=self.MYSQL_PASSWORD,
                database=self.MYSQL_DATABASE
            )
            return connection
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def initialize_database(self):
        try:
            connection = mysql.connector.connect(
                host=self.MYSQL_HOST,
                user=self.MYSQL_USER,
                password=self.MYSQL_PASSWORD
            )
            cursor = connection.cursor()
            # Criar o banco de dados, se não existir
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.MYSQL_DATABASE}")
            connection.database = self.MYSQL_DATABASE

            # Criar a tabela "usuario", se não existir
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuario (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    usuario VARCHAR(50) UNIQUE NOT NULL,
                    senha VARCHAR(50) NOT NULL
                )
            """)
            connection.commit()

        except Error as e:
            print(f"Erro ao inicializar o banco de dados: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
