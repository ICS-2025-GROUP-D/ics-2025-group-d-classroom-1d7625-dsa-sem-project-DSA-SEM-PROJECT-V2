# waiting_queue.py
import sqlite3
from tkinter import *
from tkinter import messagebox


class WaitingQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, patient):
        self.queue.append(patient)
        print(f"[Enqueued] {patient}")

    def dequeue(self):
        if not self.is_empty():
            patient = self.queue.pop(0)
            print(f"[Dequeued] {patient}")
            return patient
        else:
            print("Queue is empty!")
            return None

    def peek(self):
        return self.queue[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        return self.queue


class PatientDB:
    def __init__(self):
        self.conn = sqlite3.connect("patients.db")
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL
                        )''')
        self.conn.commit()

    def add_patient(self, name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO patients (name) VALUES (?)", (name,))
        self.conn.commit()

    def delete_patient(self, name):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM patients WHERE name = ?", (name,))
        self.conn.commit()

    def get_all_patients(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM patients")
        return [row[0] for row in cursor.fetchall()]


class WaitingQueueApp:
    def __init__(self, root):
        self.db = PatientDB()
        self.queue = WaitingQueue()

        self.root = root
        self.root.title("Waiting Queue Manager")
        self.root.geometry("400x400")

        self.label = Label(root, text="Enter Patient Name")
        self.label.pack()

        self.name_entry = Entry(root)
        self.name_entry.pack()

        self.add_btn = Button(root, text="Add to Queue", command=self.add_patient)
        self.add_btn.pack()

        self.next_btn = Button(root, text="Treat Next Patient", command=self.treat_patient)
        self.next_btn.pack()

        self.queue_listbox = Listbox(root)
        self.queue_listbox.pack(fill=BOTH, expand=True)

        self.refresh_queue()

    def add_patient(self):
        name = self.name_entry.get().strip()
        if name:
            self.queue.enqueue(name)
            self.db.add_patient(name)
            self.name_entry.delete(0, END)
            self.refresh_queue()
        else:
            messagebox.showwarning("Input Error", "Patient name cannot be empty.")

    def treat_patient(self):
        patient = self.queue.dequeue()
        if patient:
            self.db.delete_patient(patient)
            messagebox.showinfo("Treated", f"{patient} has been treated.")
            self.refresh_queue()
        else:
            messagebox.showwarning("Queue Empty", "No patients in queue.")

    def refresh_queue(self):
        self.queue_listbox.delete(0, END)
        self.queue.queue = self.db.get_all_patients()
        for patient in self.queue.queue:
            self.queue_listbox.insert(END, patient)


if __name__ == "__main__":
    root = Tk()
    app = WaitingQueueApp(root)
    root.mainloop()
