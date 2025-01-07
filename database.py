import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT NOT NULL,
        password TEXT NOT NULL
        
    )
""")
conn.commit()
conn.close()

def add_user(name,email,age,gender, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (name,email,age,gender,password) VALUES (?, ?, ?,?,?)", (name,email,age,gender, password))
    conn.commit()
    conn.close()

def authenticate_user(email, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = c.fetchone()
    conn.close()
    return user
def fetch_user(email):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = c.fetchone()
    conn.close()
    return user
