import os
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = (
    f"dbname={os.getenv('DB_NAME')} "
    f"user={os.getenv('DB_USER')} "
    f"password={os.getenv('DB_PASSWORD')} "
    f"host={os.getenv('DB_HOST')} "
    f"port={os.getenv('DB_PORT')}"
)

def obter_conexao():
    """Estabelece e retorna uma conexão com o banco de dados PostgreSQL."""
    try:
        conn = psycopg.connect(DB_CONFIG, row_factory=dict_row)
        return conn
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco de dados: {e}")
        return None

def testar_conexao():
    """Valida se a ponte Python -> Postgres está funcionando."""
    conn = obter_conexao()
    if conn:
        print("✅ Conexão com o PostgreSQL estabelecida com sucesso!")
        conn.close()
