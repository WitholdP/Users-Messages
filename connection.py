import psycopg2
from settings import db_server

def connect():
    c = psycopg2.connect(**db_server)
    c.autocommit = True
    return c
