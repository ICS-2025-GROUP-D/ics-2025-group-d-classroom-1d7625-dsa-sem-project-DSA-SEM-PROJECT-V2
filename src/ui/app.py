import tkinter as tk
from tkinter import messagebox
from src.db.db import insert_patient, delete_patient_from_db, update_patient_in_db, get_patient_from_db, init_db
from src.data_structures.bst import PatientBST

# Initialize BST and DB
bst = PatientBST()
init_db()

# GUI logic
def add_patient():
    try:
        pid = int(entry_id.get())
        name = entry_name.get()
        age = int(entry_age.get())
        illness = entry_illness.get()
        bst.insert(pid, name, age, illness)
        insert_patient(pid, name, age, illness)  # ✅ save to DB
        messagebox.showinfo("Success", f"Patient {name} added.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_patient():
    try:
        pid = int(entry_id.get())
        # First try from BST
        patient = bst.search(pid)
        if patient:
            messagebox.showinfo("Found", f"Name: {patient.name}, Age: {patient.age}, Illness: {patient.illness}")
        else:
            # If not in BST, try DB (optional fallback)
            row = get_patient_from_db(pid)
            if row:
                messagebox.showinfo("Found in DB", f"Name: {row[1]}, Age: {row[2]}, Illness: {row[3]}")
            else:
                messagebox.showwarning("Not Found", "No patient with that ID.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_patient():
    try:
        pid = int(entry_id.get())
        bst.delete(pid)
        delete_patient_from_db(pid)  # ✅ delete from DB
        messagebox.showinfo("Deleted", f"Patient with ID {pid} deleted.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_patient():
    try:
        pid = int(entry_id.get())
        name = entry_name.get()
        age = int(entry_age.get())
        illness = entry_illness.get()

        existing = bst.search(pid)
        if existing:
            bst.delete(pid)
            bst.insert(pid, name, age, illness)
            update_patient_in_db(pid, name, age, illness)  # ✅ update in DB
            messagebox.showinfo("Updated", f"Patient ID {pid} updated.")
        else:
            messagebox.showwarning("Not Found", "Patient not found to update.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Hospital Management - BST")

tk.Label(root, text="Patient ID").grid(row=0, column=0)
tk.Label(root, text="Name").grid(row=1, column=0)
tk.Label(root, text="Age").grid(row=2, column=0)
tk.Label(root, text="Illness").grid(row=3, column=0)

entry_id = tk.Entry(root)
entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_illness = tk.Entry(root)

entry_id.grid(row=0, column=1)
entry_name.grid(row=1, column=1)
entry_age.grid(row=2, column=1)
entry_illness.grid(row=3, column=1)

tk.Button(root, text="Add", command=add_patient).grid(row=4, column=0)
tk.Button(root, text="Search", command=search_patient).grid(row=4, column=1)
tk.Button(root, text="Delete", command=delete_patient).grid(row=5, column=0)
tk.Button(root, text="Update", command=update_patient).grid(row=5, column=1)

root.mainloop()
