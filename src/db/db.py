import sqlite3

def init_db():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            illness TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_patient(pid, name, age, illness):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (id, name, age, illness) VALUES (?, ?, ?, ?)",
                   (pid, name, age, illness))
    conn.commit()
    conn.close()

def update_patient_in_db(pid, name, age, illness):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE patients SET name=?, age=?, illness=? WHERE id=?",
                   (name, age, illness, pid))
    conn.commit()
    conn.close()

def delete_patient_from_db(pid):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id=?", (pid,))
    conn.commit()
    conn.close()

def get_patient_from_db(pid):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE id=?", (pid,))
    row = cursor.fetchone()
    conn.close()
    return row
