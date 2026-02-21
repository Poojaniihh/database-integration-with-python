from psycopg_pool import ConnectionPool

DB_CONN_URL = "postgresql://postgres:postgres@localhost:5433/keells"

pool = ConnectionPool(conninfo=DB_CONN_URL)


def get_db_conn():
    return pool.connection()