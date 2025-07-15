# app.py

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from src.data_structures.patient import Patient
from src.data_structures.linkedlist import HospitalLinkedList
import src.db.db as db

db.init_db()
linked_list = HospitalLinkedList()

def refresh_display():
    output_listbox.delete(0, tk.END)
    for patient in linked_list.to_list():
        output_listbox.insert(tk.END, f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Illness: {patient.illness}, Level: {patient.emergency_level}")

def add_patient():
    try:
        id_val = int(id_entry.get())
        name_val = name_entry.get()
        age_val = int(age_entry.get())
        illness_val = illness_entry.get()
        level_val = int(level_entry.get())

        if not name_val or not illness_val:
            raise ValueError("All fields must be filled.")

        if level_val not in (1, 2, 3):
            raise ValueError("Emergency level must be between 1 and 3.")

        if linked_list.find(id_val):
            raise ValueError("Patient ID already exists.")

        patient = Patient(id_val, name_val, age_val, illness_val, level_val)
        linked_list.append(patient)
        db.insert_patient(patient)
        refresh_display()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_patient():
    try:
        id_val = int(id_entry.get())
        name_val = name_entry.get()
        age_val = int(age_entry.get())
        illness_val = illness_entry.get()
        level_val = int(level_entry.get())

        if not name_val or not illness_val:
            raise ValueError("All fields must be filled.")

        patient = Patient(id_val, name_val, age_val, illness_val, level_val)
        if not linked_list.update(patient):
            raise ValueError("Patient not found.")
        db.update_patient(patient)
        refresh_display()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_patient():
    try:
        id_val = int(id_entry.get())
        if not linked_list.delete(id_val):
            raise ValueError("Patient not found.")
        db.delete_patient(id_val)
        refresh_display()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def treat_patient():
    try:
        id_val = int(id_entry.get())
        patient = linked_list.find(id_val)
        if not patient:
            raise ValueError("Patient not found.")
        visit_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes = f"Treated for {patient.illness}"
        db.insert_visit(id_val, visit_date, notes)
        messagebox.showinfo("Success", "Treatment recorded.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_visit():
    try:
        id_val = int(id_entry.get())
        notes = visit_entry.get()
        if not notes:
            raise ValueError("Visit notes cannot be empty.")
        if not db.get_patient_by_id(id_val):
            raise ValueError("Patient not found.")
        visit_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.insert_visit(id_val, visit_date, notes)
        messagebox.showinfo("Success", "Visit added.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_visits():
    try:
        id_val = int(id_entry.get())
        visits = db.get_visits_by_patient_id(id_val)
        output_listbox.delete(0, tk.END)
        for visit in visits:
            output_listbox.insert(tk.END, f"Date: {visit[0]}, Notes: {visit[1]}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_treatments():
    try:
        patient_id = int(id_entry.get())
        if not db.get_patient_by_id(patient_id):
            raise ValueError("Patient not found")

        visits = db.get_visits_by_patient_id(patient_id)
        treatments = [v for v in visits if "treated for" in v[1].lower()]
        output_listbox.delete(0, tk.END)
        for visit in treatments:
            output_listbox.insert(tk.END, f"Date: {visit[0]}, {visit[1]}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# UI Setup
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("950x600")
root.configure(bg="#f0f2f5")

form_frame = tk.LabelFrame(root, text="Patient Information", padx=10, pady=10, bg="#ffffff", font=("Arial", 10, "bold"))
form_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nw")

labels = ["ID", "Name", "Age", "Illness", "Emergency Level (1-3)", "Visit Notes"]
entries = []

for i, label in enumerate(labels):
    tk.Label(form_frame, text=label, bg="#ffffff").grid(row=i, column=0, sticky="w")
    entry = tk.Entry(form_frame, width=30)
    entry.grid(row=i, column=1, pady=2)
    entries.append(entry)

id_entry, name_entry, age_entry, illness_entry, level_entry, visit_entry = entries

button_frame = tk.LabelFrame(root, text="Actions", padx=10, pady=10, bg="#ffffff", font=("Arial", 10, "bold"))
button_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nw")

buttons = [
    ("Add Patient", add_patient),
    ("Update Patient", update_patient),
    ("Delete Patient", delete_patient),
    ("Treat Patient", treat_patient),
    ("Add Visit", add_visit),
    ("Current Visits", show_visits),
    ("Treatment History", show_treatments),
]

for i, (text, command) in enumerate(buttons):
    tk.Button(button_frame, text=text, command=command, width=25, bg="#4CAF50", fg="white", font=("Arial", 9)).grid(row=i, column=0, pady=2)

output_frame = tk.LabelFrame(root, text="Output", padx=10, pady=10, bg="#ffffff", font=("Arial", 10, "bold"))
output_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="ne")

output_listbox = tk.Listbox(output_frame, width=70, height=25, font=("Courier", 10))
output_listbox.pack()

refresh_display()
root.mainloop()