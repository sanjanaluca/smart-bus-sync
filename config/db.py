import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="smart_bus_sync",
        user="postgres",
        password="postgres123",
        host="localhost"
    )
    return conn
