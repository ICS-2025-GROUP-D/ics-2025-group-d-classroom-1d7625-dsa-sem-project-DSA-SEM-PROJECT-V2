# Step 1: Create a virtual environment
# python3 -m venv venv

# Step 2: Activate it
# source venv/bin/activate

# Step 3: Install requirements
# pip install -r requirements.txt

# Step 4: Launch Dashboard
# python3 main.py

# Step 5: To deactivate
# deactivate

import customtkinter as ctk # type: ignore
from widgets.room_tabs import create_room_tabs
from utils.helpers import get_current_time
 
class SmartHomeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Home Dashboard")
        self.geometry("1425x800")
        self.protocol("WM_DELETE_WINDOW", lambda: self.destroy())

        # Title Label
        self.title_label = ctk.CTkLabel(self, text="Hello", font=("Arial", 24))
        self.title_label.place(x=20, y=20)


        # Time Label ( Displays the current time )
        self.title_label = ctk.CTkLabel(self, font=("Arial", 24), text=get_current_time())
        self.title_label.place(x=1300, y=20)

        create_room_tabs(self)

if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()