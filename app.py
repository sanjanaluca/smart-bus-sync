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
                SELECT *
                FROM student_status
                WHERE student_id = %s
                AND status_date = %s
            """, (student_id, date.today()))

            existing_status = cur.fetchone()

            if existing_status:

                message = "Status already submitted today"

            else:

                cur.execute("""
                    INSERT INTO student_status
                    (student_id, status, status_date)
                    VALUES (%s, %s, %s)
                """, (student_id, status, date.today()))

                conn.commit()

                message = "Status saved successfully"

            cur.close()
            conn.close()

    return render_template(
        'index.html',
        student=student,
        message=message
    )
@app.route('/history')
def history():

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            student_id,
            status,
            status_date
        FROM student_status
        ORDER BY status_date
    """)

    history = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        'history.html',
        history=history
    )
@app.route('/dashboard')
def dashboard():

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            bus_number,
            strength_count,
            calculation_date
        FROM bus_strength
        ORDER BY bus_number
    """)

    dashboard = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        'dashboard.html',
        dashboard=dashboard
    )
@app.route('/recommendation')
def recommendation():

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            primary_bus,
            merged_bus,
            total_students,
            recommendation_date
        FROM bus_merge_recommendation
        ORDER BY recommendation_date DESC
    """)

    recommendations = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        'recommendation.html',
        recommendations=recommendations
    )
if __name__ == '__main__':
    app.run(debug=True)
