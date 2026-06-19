from flask import Flask
from config.db import get_db_connection

app = Flask(__name__)

@app.route('/')
def home():

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            id_number,
            student_name,
            bus_number
        FROM student
    """)

    students = cur.fetchall()

    cur.close()
    conn.close()

    result = ""

    for student in students:
        result += f"""
        Student ID: {student[0]} <br>
        Name: {student[1]} <br>
        Bus: {student[2]} <br><br>
        """

    return result


if __name__ == '__main__':
    app.run(debug=True)
