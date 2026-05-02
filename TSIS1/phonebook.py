# -*- coding: utf-8 -*-
import psycopg2
import json
from connect import connect


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



def search_user():
    pattern = input("Insert name pattern: ")

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM find_pattern(%s);", (pattern, ))
            result = cur.fetchall()
            for user in result:
                print(user) 



def pagination():
    limit = int(input("Enter limit: "))
    
    offset = int(input("Enter offset: "))
    
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook_paginated(%s, %s);", (limit, offset, ))
            result = cur.fetchall()
            for user in result:
                print(user)


def insert_update_user():
    
    name = input("Insert name: ")

    phone = input("Insert phone: ")

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_name_phone(%s, %s);", (name, phone, ))
    
    print("User inserted or updated.")


def insert_many_users():

    users = [
        {"name": "Alex", "surname": "Doyel", "phone": "987456"},
        {"name": "Alice", "surname": "Red", "phone": "negative"},
        {"name": "Sanzhar", "surname": "Zhal", "phone": "+770124589"}
    ]

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_many_users(%s);", (json.dumps(users), ))



def delete():

    print("1 - Delete by name")

    print("2 - Delete by phone")
    
    command = input("Enter your choice: ")

    with connect() as conn:
        with conn.cursor() as cur:
            if command == "1":
                name = input("Enter name: ")
                cur.execute("CALL delete_user(%s, NULL);", (name, ))
            
            elif command == "2":

                phone = input("Enter phone: ")
                cur.execute("CALL delete_user(NULL, %s);", (phone, ))

    print("Deleted succesfully!")

        




def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1 - Create table")
        print("2 - Insert from console")
        print("3 - Update data")
        print("4 - Insert many users")
        print("5 - Delete data")
        print("6 - Pagination")
        print("0 - Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            create_table()
        elif choice == "2":
            search_user()
        elif choice == "3":
            insert_update_user()
        elif choice == "4":
            pass
        elif choice == "5":
            delete()
        elif choice == "6":
            pagination()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()