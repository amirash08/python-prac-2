# -*- coding: utf-8 -*-
import psycopg2
from config import MY_DATABASE_CONFIG


def connect():
    return psycopg2.connect(
        host=MY_DATABASE_CONFIG["host"],
        database=MY_DATABASE_CONFIG["database"],
        user=MY_DATABASE_CONFIG["user"],
        password=MY_DATABASE_CONFIG["password"],
        port=MY_DATABASE_CONFIG["port"],
        options='-c client_encoding=UTF8'
    )