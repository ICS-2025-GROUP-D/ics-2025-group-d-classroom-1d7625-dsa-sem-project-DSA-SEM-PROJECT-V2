import tkinter as tk
from tkinter import ttk, messagebox
from backend import MovieTracker


class MovieTrackerGUI:
  def __init__(self, root):
    self.root = root
    self.tracker = MovieTracker()  # Our backend class
    self.setup_gui()
    self.load_movies()

  def setup_gui(self):
    # Main window configuration
    self.root.title("Movie Watchlist Tracker")
    self.root.geometry("900x600")

    # Configure styles
    self.style = ttk.Style()
    self.style.configure("Treeview", rowheight=25)
    self.style.configure("TButton", padding=5)

    # ===== Top Controls Frame =====
    control_frame = ttk.Frame(self.root)
    control_frame.pack(pady=10, padx=10, fill=tk.X)

    # Search components
    ttk.Label(control_frame, text="Search:").pack(side=tk.LEFT, padx=5)
    self.search_var = tk.StringVar()
    self.search_entry = ttk.Entry(control_frame, textvariable=self.search_var, width=30)
    self.search_entry.pack(side=tk.LEFT, padx=5)
    self.search_entry.bind("<KeyRelease>", self.search_movies)

    # Action buttons
    ttk.Button(control_frame, text="Add Movie", command=self.show_add_form).pack(side=tk.RIGHT, padx=5)
    ttk.Button(control_frame, text="Refresh", command=self.load_movies).pack(side=tk.RIGHT, padx=5)

    # ===== Main Movie Table =====
    self.tree_frame = ttk.Frame(self.root)
    self.tree_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Treeview setup
    self.tree = ttk.Treeview(self.tree_frame, columns=("Title", "Genre", "Rating", "Year", "Watched"), show="headings")
    self.tree.heading("Title", text="Title", command=lambda: self.sort_column("Title"))
    self.tree.heading("Genre", text="Genre")
    self.tree.heading("Rating", text="Rating")
    self.tree.heading("Year", text="Year")
    self.tree.heading("Watched", text="Watched")

    # Column configuration
    self.tree.column("Title", width=200)
    self.tree.column("Genre", width=100)
    self.tree.column("Rating", width=80, anchor=tk.CENTER)
    self.tree.column("Year", width=60, anchor=tk.CENTER)
    self.tree.column("Watched", width=70, anchor=tk.CENTER)

    self.tree.pack(fill=tk.BOTH, expand=True)

    # Scrollbar
    scrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
    self.tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # ===== Action Buttons =====
    button_frame = ttk.Frame(self.root)
    button_frame.pack(pady=10, fill=tk.X)

    ttk.Button(button_frame, text="Mark Watched", command=self.mark_watched).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_frame, text="Edit", command=self.edit_movie).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_frame, text="Delete", command=self.delete_movie).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_frame, text="View Details", command=self.show_details).pack(side=tk.LEFT, padx=5)

    # ===== Status Bars =====
    status_frame = ttk.Frame(self.root)
    status_frame.pack(fill=tk.X, padx=10, pady=5)

    # Watchlist queue status
    self.watchlist_status = ttk.Label(status_frame, text="Watchlist (Queue): 0 movies")
    self.watchlist_status.pack(side=tk.LEFT, padx=5)

    # Watched history status
    self.watched_status = ttk.Label(status_frame, text="Recently Watched (Stack): 0 movies")
    self.watched_status.pack(side=tk.LEFT, padx=5)

    # ===== Console Log =====
    log_frame = ttk.LabelFrame(self.root, text="Console Log")
    log_frame.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

    self.log_text = tk.Text(log_frame, height=5, state=tk.DISABLED)
    self.log_text.pack(fill=tk.BOTH, expand=True)

  def load_movies(self):
    """Load movies from backend into the table"""
    # Clear existing data
    for item in self.tree.get_children():
      self.tree.delete(item)

    # Add movies from BST (sorted)
    movies = self.tracker.get_sorted_movies()
    for movie in movies:
      self.tree.insert("", tk.END, values=(
        movie['title'],
        movie['genre'],
        self.get_star_rating(movie['rating']),
        movie['year'],
        "✓" if movie['watched'] else "✗"
      ), tags=("watched" if movie['watched'] else "unwatched"))

    # Update status bars
    self.update_status()
    self.log("Loaded all movies from database")

  def get_star_rating(self, rating):
    """Convert numeric rating to star symbols"""
    return "★" * rating + "☆" * (5 - rating)

  def update_status(self):
    """Update the queue and stack status labels"""
    self.watchlist_status.config(text=f"Watchlist (Queue): {len(self.tracker.watchlist)} movies")
    self.watched_status.config(text=f"Recently Watched (Stack): {len(self.tracker.watched_history)} movies")

  def search_movies(self, event=None):
    """Search movies in real-time as user types"""
    query = self.search_var.get().lower()

    # Show all if search is empty
    if not query:
      for item in self.tree.get_children():
        self.tree.item(item, tags=())
        self.tree.detach(item)
        self.tree.attach(item, "", 0)
      return

    # Hide non-matching items
    for item in self.tree.get_children():
      values = self.tree.item(item)['values']
      if query in values[0].lower():  # Search in title
        self.tree.item(item, tags=())
        self.tree.detach(item)
        self.tree.attach(item, "", 0)
      else:
        self.tree.detach(item)

  def show_add_form(self):
    """Show the add movie dialog"""
    dialog = tk.Toplevel(self.root)
    dialog.title("Add New Movie")
    dialog.geometry("300x200")

    # Form fields
    ttk.Label(dialog, text="Title:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
    title_entry = ttk.Entry(dialog)
    title_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

    ttk.Label(dialog, text="Genre:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
    genre_entry = ttk.Entry(dialog)
    genre_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

    ttk.Label(dialog, text="Rating (1-5):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
    rating_entry = ttk.Spinbox(dialog, from_=1, to=5)
    rating_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

    ttk.Label(dialog, text="Year:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
    year_entry = ttk.Entry(dialog)
    year_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

    # Submit button
    def submit():
      title = title_entry.get()
      genre = genre_entry.get()
      rating = int(rating_entry.get())
      year = year_entry.get()

      if not title:
        messagebox.showerror("Error", "Title is required!")
        return

      if self.tracker.add_movie(title, genre, rating, year):
        self.load_movies()
        self.log(f"Added new movie: {title}")
        dialog.destroy()
      else:
        messagebox.showerror("Error", "Movie already exists!")

    ttk.Button(dialog, text="Add Movie", command=submit).grid(row=4, column=1, pady=10)

  def mark_watched(self):
    """Mark selected movie as watched"""
    selected = self.tree.selection()
    if not selected:
      messagebox.showwarning("Warning", "Please select a movie first!")
      return

    title = self.tree.item(selected)['values'][0]
    if self.tracker.mark_as_watched(title):
      self.load_movies()
      self.log(f"Marked '{title}' as watched")
    else:
      messagebox.showerror("Error", "Failed to update movie status")

  def delete_movie(self):
    """Delete selected movie"""
    selected = self.tree.selection()
    if not selected:
      messagebox.showwarning("Warning", "Please select a movie first!")
      return

    title = self.tree.item(selected)['values'][0]
    if messagebox.askyesno("Confirm", f"Delete '{title}' permanently?"):
      # Need to implement delete_movie in backend
      if self.tracker.delete_movie(title):
        self.load_movies()
        self.log(f"Deleted movie: {title}")
      else:
        messagebox.showerror("Error", "Failed to delete movie")

  def edit_movie(self):
    """Edit selected movie details"""
    selected = self.tree.selection()
    if not selected:
      messagebox.showwarning("Warning", "Please select a movie first!")
      return

    # Similar to add_form but with existing values
    pass  # Implementation would mirror show_add_form but with update logic

  def show_details(self):
    """Show detailed view of selected movie"""
    selected = self.tree.selection()
    if not selected:
      messagebox.showwarning("Warning", "Please select a movie first!")
      return

    title = self.tree.item(selected)['values'][0]
    movie = self.tracker.search_movie(title)

    details = tk.Toplevel(self.root)
    details.title(f"Details: {title}")

    # Display all movie information in a formatted way
    ttk.Label(details, text=f"Title: {movie['title']}").pack(pady=5)
    ttk.Label(details, text=f"Genre: {movie['genre']}").pack(pady=5)
    ttk.Label(details, text=f"Rating: {self.get_star_rating(movie['rating'])}").pack(pady=5)
    ttk.Label(details, text=f"Year: {movie['year']}").pack(pady=5)
    ttk.Label(details, text=f"Status: {'Watched' if movie['watched'] else 'Unwatched'}").pack(pady=5)

  def sort_column(self, col):
    """Sort treeview by column"""
    data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]
    data.sort()

    for index, (val, child) in enumerate(data):
      self.tree.move(child, '', index)

  def log(self, message):
    """Add message to console log"""
    self.log_text.config(state=tk.NORMAL)
    self.log_text.insert(tk.END, message + "\n")
    self.log_text.config(state=tk.DISABLED)
    self.log_text.see(tk.END)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MovieTrackerGUI(root)
    root.mainloop()
