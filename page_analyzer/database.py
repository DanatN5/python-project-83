import os
import psycopg2
from psycopg2.extras import DictCursor


DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

class Urls:
    def __init__(self, conn):
        self.conn = conn

    def _create(self, url):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO urls (name, created_at) VALUES (%s) RETURNING id",
                (url,)
            )
        self.conn.commit()

    def save(self, url):
        self._create(url)
"""
    def _update(self, url):
        with self.conn.cursor() as cur:
            cur.execute(
                "UPDATE urls SET name = %s, RETURNING id",
                (url,)
            )
        self.conn.commit()
"""
