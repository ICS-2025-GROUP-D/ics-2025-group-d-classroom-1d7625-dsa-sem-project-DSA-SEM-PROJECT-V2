import sqlite3
from sqlite3 import Error

## DATABASE creation and connection (Grace)##
class Database:
    def __init__(self, db_file='movie_watchlist.db'):
        self.conn = self._create_connection(db_file)
        self._create_tables()

    def _create_connection(self, db_file):
        """Create a database connection."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Database connection error: {e}")
            return None

    def _create_tables(self):
        """Initialize database tables."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT UNIQUE NOT NULL,
                    genre TEXT,
                    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
                    year INTEGER,
                    watched BOOLEAN DEFAULT 0
                )
            ''')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_title ON movies (title)')
            self.conn.commit()
        except Error as e:
            print(f"Table creation error: {e}")

    # CRUD Operations
    def add_movie(self, title, genre, rating, year):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO movies (title, genre, rating, year)
                VALUES (?, ?, ?, ?)
            ''', (title, genre, rating, year))
            self.conn.commit()
            return True
        except Error as e:
            print(f"Error adding movie: {e}")
            return False

    def get_all_movies(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM movies')
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching movies: {e}")
            return []

    def close(self):
        if self.conn:
            self.conn.close()

