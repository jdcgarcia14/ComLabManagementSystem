import sqlite3

DB_FILE = "database.db"

with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()
    cur.execute("""
             SELECT id, tag, hostname, comlab_id, assigned_student FROM devices;
        """)
    rows = cur.fetchall()
    for r in rows:
        print(r)
