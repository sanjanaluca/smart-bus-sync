from flask import Flask, render_template, request
from config.db import get_db_connection
from datetime import date

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    student = None
    message = ""

    if request.method == 'POST':

        action = request.form['action']

        if action == "search":

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

        elif action == "save":

            student_id = request.form['student_id']
            status = request.form['status']

            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute("""
                INSERT INTO student_status
                (student_id, status, status_date)
                VALUES (%s, %s, %s)
            """, (student_id, status, date.today()))

            conn.commit()

            cur.close()
            conn.close()

            message = "Status saved successfully"

    return render_template(
        'index.html',
        student=student,
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True)
