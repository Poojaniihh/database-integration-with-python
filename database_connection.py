from psycopg_pool import ConnectionPool

DB_CONN_URL = "postgresql://postgres:admin@localhost:5432/keells"

pool = ConnectionPool(conninfo=DB_CONN_URL)


def get_db_conn():
    return pool.connection()