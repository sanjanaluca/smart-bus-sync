from config.db import get_db_connection

conn = get_db_connection()

cur = conn.cursor()

cur.execute("SELECT student_name FROM student")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
