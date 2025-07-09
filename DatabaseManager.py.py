import sqlite3

class DatabaseManager:
    def __init__(self):
        self.db_name = "entries.db"
        self._init_db()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _init_db(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                content TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def insert_entry(self, date, content):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO entries (date, content) VALUES (?, ?)", (date, content))
        conn.commit()
        conn.close()

    def update_entry(self, entry_id, content):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE entries SET content = ? WHERE id = ?", (content, entry_id))
        conn.commit()
        conn.close()

    def delete_entry(self, entry_id):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
        conn.commit()
        conn.close()

    def fetch_entry(self, entry_id):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM entries WHERE id = ?", (entry_id,))
        result = cursor.fetchone()
        conn.close()
        return result

    def fetch_all_entries(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, date FROM entries ORDER BY date DESC")
        result = cursor.fetchall()
        conn.close()
        return result

    def fetch_all_entries_bst(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, date FROM entries")
        result = cursor.fetchall()
        conn.close()
        return result

    def search_entries_by_date(self, date_prefix):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, date FROM entries WHERE date LIKE ?", (date_prefix + '%',))
        result = cursor.fetchall()
        conn.close()
        return result