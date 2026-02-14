from database_connection import get_db_conn


def create_user(name: str, email: str):
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO users(name, email)
                VALUES(%s, %s)
                RETURNING id, name, email
                """,
                (name, email)
            )
            return cursor.fetchone()

def get_user(user_id: int):
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, email FROM users WHERE id=%s"
                , (user_id,)
            )
            return cursor.fetchone()

def get_all_users():
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, email FROM users ORDER BY id;"
            )
            return cursor.fetchall()

def delete_user(user_id: int):
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                 "DELETE FROM users WHERE id=%s;"
                , (user_id,)
            )
            return cursor.fetchone()




