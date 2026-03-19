import psycopg2
import csv


def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook_db",
        user="postgres",
        password="your_password",
        port="5432"
    )


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        phone VARCHAR(30) NOT NULL UNIQUE
    );
    """
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
    print("Table created successfully")


def insert_from_console():
    first_name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    query = """
    INSERT INTO phonebook (first_name, phone)
    VALUES (%s, %s);
    """

    try:
        with connect() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (first_name, phone))
        print("Data inserted from console")
    except Exception as e:
        print("Error:", e)


def insert_from_csv(filename):
    query = """
    INSERT INTO phonebook (first_name, phone)
    VALUES (%s, %s)
    ON CONFLICT (phone) DO NOTHING;
    """

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            with connect() as conn:
                with conn.cursor() as cur:
                    for row in reader:
                        if len(row) >= 2:
                            first_name = row[0].strip()
                            phone = row[1].strip()
                            cur.execute(query, (first_name, phone))

        print("Data inserted from CSV")
    except Exception as e:
        print("Error:", e)


def update_user():
    print("1 - Update name by phone")
    print("2 - Update phone by name")
    choice = input("Choose option: ").strip()

    try:
        with connect() as conn:
            with conn.cursor() as cur:
                if choice == "1":
                    phone = input("Enter current phone: ").strip()
                    new_name = input("Enter new name: ").strip()

                    query = """
                    UPDATE phonebook
                    SET first_name = %s
                    WHERE phone = %s;
                    """
                    cur.execute(query, (new_name, phone))
                    print("Name updated")

                elif choice == "2":
                    name = input("Enter current name: ").strip()
                    new_phone = input("Enter new phone: ").strip()

                    query = """
                    UPDATE phonebook
                    SET phone = %s
                    WHERE first_name = %s;
                    """
                    cur.execute(query, (new_phone, name))
                    print("Phone updated")

                else:
                    print("Invalid choice")
    except Exception as e:
        print("Error:", e)


def query_data():
    print("1 - Show all records")
    print("2 - Find by name")
    print("3 - Find by phone")
    print("4 - Find names starting with letter")
    choice = input("Choose option: ").strip()

    try:
        with connect() as conn:
            with conn.cursor() as cur:
                if choice == "1":
                    query = "SELECT * FROM phonebook ORDER BY id;"
                    cur.execute(query)

                elif choice == "2":
                    name = input("Enter name: ").strip()
                    query = """
                    SELECT * FROM phonebook
                    WHERE first_name = %s
                    ORDER BY id;
                    """
                    cur.execute(query, (name,))

                elif choice == "3":
                    phone = input("Enter phone: ").strip()
                    query = """
                    SELECT * FROM phonebook
                    WHERE phone = %s
                    ORDER BY id;
                    """
                    cur.execute(query, (phone,))

                elif choice == "4":
                    letter = input("Enter first letter: ").strip()
                    query = """
                    SELECT * FROM phonebook
                    WHERE first_name ILIKE %s
                    ORDER BY id;
                    """
                    cur.execute(query, (letter + "%",))

                else:
                    print("Invalid choice")
                    return

                rows = cur.fetchall()

                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("No data found")
    except Exception as e:
        print("Error:", e)


def delete_data():
    print("1 - Delete by name")
    print("2 - Delete by phone")
    choice = input("Choose option: ").strip()

    try:
        with connect() as conn:
            with conn.cursor() as cur:
                if choice == "1":
                    name = input("Enter name: ").strip()
                    query = "DELETE FROM phonebook WHERE first_name = %s;"
                    cur.execute(query, (name,))
                    print("Data deleted by name")

                elif choice == "2":
                    phone = input("Enter phone: ").strip()
                    query = "DELETE FROM phonebook WHERE phone = %s;"
                    cur.execute(query, (phone,))
                    print("Data deleted by phone")

                else:
                    print("Invalid choice")
    except Exception as e:
        print("Error:", e)


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1 - Create table")
        print("2 - Insert from console")
        print("3 - Insert from CSV")
        print("4 - Update data")
        print("5 - Query data")
        print("6 - Delete data")
        print("0 - Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            filename = input("Enter CSV filename: ").strip()
            insert_from_csv(filename)
        elif choice == "4":
            update_user()
        elif choice == "5":
            query_data()
        elif choice == "6":
            delete_data()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()