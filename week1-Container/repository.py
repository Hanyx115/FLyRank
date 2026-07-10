import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

class PostgresRepo:
    def __init__(self):
        self.conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        
    def get_items(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM items;")
            return cur.fetchall()

    def create_item(self, name, description):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "INSERT INTO items (name, description) VALUES (%s, %s) RETURNING *;",
                (name, description)
            )
            self.conn.commit()
            return cur.fetchone()