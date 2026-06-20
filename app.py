from flask import Flask, render_template, request
from config.db import get_db_connection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    student = None

    if request.method == 'POST':

        student_id = request.form['student_id']

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT
                s.id_number,
                s.student_name,
                s.college_name,
                s.department,
                s.year,
                s.bus_number,
                bs.stop_name
            FROM student s
            JOIN bus_stop bs
            ON s.stop_id = bs.stop_id
            WHERE s.id_number = %s
        """, (student_id,))

        student = cur.fetchone()

        cur.close()
        conn.close()

    return render_template('index.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
