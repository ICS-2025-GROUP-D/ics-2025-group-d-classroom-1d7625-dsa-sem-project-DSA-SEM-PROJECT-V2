import sqlite3
from sqlite3 import Error

## ====================== DATABASE LAYER ====================== ##
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

## ====================== DATA STRUCTURES ====================== ##
class BSTNode:
    """Binary Search Tree Node for sorting movies by title"""
    def __init__(self, movie):
        self.movie = movie
        self.left = None
        self.right = None

class MovieTracker:
    def __init__(self):
        self.db = Database()
        self.movies_db = {}       # Hash Table (title -> movie data)
        self.bst_root = None      # BST sorted by title
        self.watchlist = []       # Queue (FIFO)
        self.watched_history = [] # Stack (LIFO)
        self._load_data()

    def _load_data(self):
        """Load data from database into data structures"""
        movies = self.db.get_all_movies()
        for movie in movies:
            movie_data = {
                'id': movie[0],
                'title': movie[1],
                'genre': movie[2],
                'rating': movie[3],
                'year': movie[4],
                'watched': bool(movie[5])
            }
            self.movies_db[movie[1]] = movie_data
            self._bst_insert(movie_data)
            if movie_data['watched']:
                self.watched_history.append(movie_data)
            else:
                self.watchlist.append(movie_data)

    def _bst_insert(self, movie_data):
        """Helper for BST insertion"""
        new_node = BSTNode(movie_data)
        if not self.bst_root:
            self.bst_root = new_node
            return

        current = self.bst_root
        while True:
            if movie_data['title'] < current.movie['title']:
                if not current.left:
                    current.left = new_node
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    break
                current = current.right

    def add_movie(self, title, genre, rating, year):
        """Add movie to all data structures and database"""
        if title in self.movies_db:
            return False  # Movie already exists

        # Add to database
        success = self.db.add_movie(title, genre, rating, year)
        if not success:
            return False

        # Add to data structures
        movie_data = {
            'title': title,
            'genre': genre,
            'rating': rating,
            'year': year,
            'watched': False
        }
        self.movies_db[title] = movie_data
        self._bst_insert(movie_data)
        self.watchlist.append(movie_data)
        return True

    def search_movie(self, title):
        """Search by title using Hash Table (O(1))"""
        return self.movies_db.get(title)

    def get_sorted_movies(self):
        """In-order traversal of BST (returns movies alphabetically)"""
        movies = []
        self._in_order_traversal(self.bst_root, movies)
        return movies

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.movie)
            self._in_order_traversal(node.right, result)

    def mark_as_watched(self, title):
        """Move movie from watchlist (Queue) to watched history (Stack)"""
        if title not in self.movies_db:
            return False

        # Update in memory
        movie = self.movies_db[title]
        movie['watched'] = True
        if movie in self.watchlist:
            self.watchlist.remove(movie)
        self.watched_history.append(movie)

        # Update database
        try:
            cursor = self.db.conn.cursor()
            cursor.execute('''
                UPDATE movies SET watched = 1 WHERE title = ?
            ''', (title,))
            self.db.conn.commit()
            return True
        except Error as e:
            print(f"Error updating movie: {e}")
            return False

    def get_next_to_watch(self):
        """Queue peek operation"""
        return self.watchlist[0] if self.watchlist else None

    def get_recently_watched(self):
        """Stack peek operation"""
        return self.watched_history[-1] if self.watched_history else None

    def close(self):
        """Clean up resources"""
        self.db.close()

## ====================== USAGE EXAMPLE ====================== ##
if __name__ == '__main__':
    tracker = MovieTracker()
    
    # Add some movies
    tracker.add_movie("Inception", "Sci-Fi", 5, 2010)
    tracker.add_movie("The Shawshank Redemption", "Drama", 5, 1994)
    tracker.add_movie("Pulp Fiction", "Crime", 4, 1994)

    # Search a movie
    print(tracker.search_movie("Inception"))  # O(1) lookup

    # Get sorted list (BST traversal)
    print("Alphabetical order:")
    for movie in tracker.get_sorted_movies():
        print(movie['title'])

    # Mark as watched
    tracker.mark_as_watched("Inception")
    print(f"Recently watched: {tracker.get_recently_watched()['title']}")
    
    tracker.close()