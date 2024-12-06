import sqlite3

def initialize_database():
    conn = sqlite3.connect('lr8.db')
    cursor = conn.cursor()
    return conn, cursor

def create_courier_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courier (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT,
            first_name TEXT,
            patronymic TEXT,
            passport TEXT,
            birth_date DATE,
            hire_date DATE,
            work_start TIME,
            work_end TIME,
            city TEXT,
            street TEXT,
            building TEXT,
            apartment TEXT,
            phone TEXT
        )
    """)

def create_sender_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sender (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT,
            first_name TEXT,
            patronymic TEXT,
            birth_date DATE,
            postal_code TEXT,
            city TEXT,
            street TEXT,
            building TEXT,
            apartment TEXT,
            phone TEXT
        )
    """)

def add_courier_sample(cursor):
    courier_data = (
    "Ivanov", "Dmitriy", "Ivanovich", "9876 543210", "10.03.1985", "15.05.2021",
    "08:00", "17:00", "Moscow", "Arbat", "12", "7", "+79051234567"
    )
    cursor.execute("""
        INSERT INTO courier (
            last_name, first_name, patronymic, passport, birth_date, hire_date, 
            work_start, work_end, city, street, building, apartment, phone
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, courier_data)

def add_sender_sample(cursor):
    sender_data = (
        "Kuznetsov", "Alexey", "Sergeevich", "14.07.1990", "654321", "Saint Petersburg",
        "Nevsky", "25", "12", "+79265554444"
    )

    cursor.execute("""
        INSERT INTO sender (
            last_name, first_name, patronymic, birth_date, postal_code, city, 
            street, building, apartment, phone
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, sender_data)

def update_sender_phone(cursor):
    sender_identifiers = ("Kuznetsov", "Alexey", "Sergeevich", "14.07.1990")
    cursor.execute("""
        UPDATE sender 
        SET phone = "+79333334000" 
        WHERE last_name = ? AND first_name = ? AND patronymic = ? AND birth_date = ?
    """, sender_identifiers)

def main():
    try:
        conn, cursor = initialize_database()

        create_courier_table(cursor)
        create_sender_table(cursor)
        add_courier_sample(cursor)
        add_sender_sample(cursor)
        update_sender_phone(cursor)

        conn.commit()

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
