from flask import Flask, render_template, request
from config.db import get_db_connection
from datetime import date

app = Flask(__name__)

# ---------------- HOME ----------------

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

# ---------------- ATTENDANCE ----------------

@app.route('/history', methods=['GET', 'POST'])
def history():

    history = []

    if request.method == 'POST':

        bus_number = request.form['bus_number']

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
                ss.status,
                ss.status_date
            FROM student_status ss
            JOIN student s
            ON ss.student_id = s.id_number
            WHERE s.bus_number = %s
            AND ss.status_date = CURRENT_DATE
            ORDER BY s.student_name
        """, (bus_number,))

        history = cur.fetchall()

        cur.close()
        conn.close()

    return render_template(
        'history.html',
        history=history
    )

# ---------------- DASHBOARD ----------------

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    strength = None
    bus_number = None

    if request.method == 'POST':

        bus_number = request.form['bus_number']

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT COUNT(*)
            FROM student_status ss
            JOIN student s
            ON ss.student_id = s.id_number
            WHERE s.bus_number = %s
            AND ss.status = 'Present'
            AND ss.status_date = CURRENT_DATE
        """, (bus_number,))

        strength = cur.fetchone()[0]

        cur.close()
        conn.close()

    return render_template(
        'dashboard.html',
        bus_number=bus_number,
        strength=strength
    )

# ---------------- RECOMMENDATION ----------------

@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():

    buses = []
    recommendation = {}
    transfer_plan = []
    final_strength = []

    if request.method == "POST":

        common_stop_id = request.form["common_stop_id"]

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT bus_number
            FROM bus_common_stop
            WHERE common_stop_id = %s
            ORDER BY bus_number
        """, (common_stop_id,))

        bus_list = cur.fetchall()

        total_strength = 0

        cur.execute("""
            SELECT total_capacity
            FROM bus_capacity
            LIMIT 1
        """)

        bus_capacity = cur.fetchone()[0]

        for bus in bus_list:

            bus_number = bus[0]

            cur.execute("""
                SELECT COUNT(*)
                FROM student_status ss
                JOIN student s
                ON ss.student_id = s.id_number
                WHERE s.bus_number = %s
                AND ss.status = 'Present'
                AND ss.status_date = CURRENT_DATE
            """, (bus_number,))

            strength = cur.fetchone()[0]

            buses.append({
                "bus_number": bus_number,
                "strength": strength
            })

            total_strength += strength

        # CASE 1 - Merge All Buses

        if total_strength <= bus_capacity:

            strongest_bus = max(buses, key=lambda x: x["strength"])

            recommendation["type"] = "Merge All"
            recommendation["primary_bus"] = strongest_bus["bus_number"]

            for bus in buses:

                if bus["bus_number"] != strongest_bus["bus_number"]:

                    transfer_plan.append({
                        "from_bus": bus["bus_number"],
                        "to_bus": strongest_bus["bus_number"],
                        "students": bus["strength"]
                    })

            final_strength.append({
                "bus_number": strongest_bus["bus_number"],
                "strength": total_strength
            })

        # CASE 2 - Split Weak Bus

        else:

            weak_bus = None

            for bus in buses:

                if bus["strength"] < 7:
                    weak_bus = bus
                    break

            if weak_bus:

                recommendation["type"] = "Split Bus"
                recommendation["primary_bus"] = weak_bus["bus_number"]

                receivers = []

                for bus in buses:

                    if bus["bus_number"] != weak_bus["bus_number"]:
                        receivers.append(bus)

                students = weak_bus["strength"]
                i = 0

                while students > 0:

                    receivers[i]["strength"] += 1

                    transfer_plan.append({
                        "from_bus": weak_bus["bus_number"],
                        "to_bus": receivers[i]["bus_number"],
                        "students": 1
                    })

                    students -= 1
                    i = (i + 1) % len(receivers)

                for bus in receivers:

                    final_strength.append({
                        "bus_number": bus["bus_number"],
                        "strength": bus["strength"]
                    })

            else:

                recommendation["type"] = "No Merge Required"

        cur.close()
        conn.close()

    return render_template(
        "recommendation.html",
        buses=buses,
        recommendation=recommendation,
        transfer_plan=transfer_plan,
        final_strength=final_strength,
        total_strength=total_strength if request.method == "POST" else None,
        bus_capacity=bus_capacity if request.method == "POST" else None
    )

# ---------------- MAIN ----------------

if __name__ == '__main__':
    app.run(debug=True)
