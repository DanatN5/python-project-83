import psycopg2
from psycopg2.extras import DictCursor


class Urls:
    def __init__(self, database_url):
        self.conn = psycopg2.connect(database_url)
        
    def find_url(self, url):
        query = "SELECT * FROM urls WHERE name = %s"
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query, (url,))
            row = cur.fetchone()
            return dict(row) if row else None
        
    def find_id(self, id):
        query = "SELECT * FROM urls WHERE id = %s"
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query, (id,))
            row = cur.fetchone()
            return dict(row) if row else None

    def save(self, url):
        query = """
        INSERT INTO urls (name, created_at)
        VALUES (%s, NOW())
        RETURNING id
        """
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query, (url,))
            id = cur.fetchone()[0]
            
        self.conn.commit()
        
        return id

    def get_all_urls(self):
        query = "SELECT * FROM urls ORDER BY id DESC"
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query)
            row = cur.fetchall()
            return row if row else None
        
    def add_url_check(self, data):
        query = """
        INSERT INTO url_checks (url_id, status_code, h1, title, description)
        VALUES (%s, %s, %s, %s, %s)
        """
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query, (
                data["url_id"],
                data["status_code"],
                data["h1"],
                data["title"],
                data["description"],)
            )
        self.conn.commit()
        
    def get_url_check(self, id):
        query = """SELECT * FROM url_checks 
        WHERE url_id = %s ORDER BY created_at DESC"""
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query, (id,))
            row = cur.fetchall()
            return row if row else None
