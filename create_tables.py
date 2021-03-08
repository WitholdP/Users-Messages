from connection import connect
from psycopg2 import errors

users = """
CREATE TABLE users (
id serial PRIMARY KEY,
username varchar(255) UNIQUE,
first_name varchar(25),
last_name varchar(25),
password varchar(80),
loged_in boolean DEFAULT False
);
"""

messages = """
CREATE TABLE messages (
id serial PRIMARY KEY,
from_id int,
to_id int,
message text,
creation_date timestamp,
FOREIGN KEY (from_id) REFERENCES users(id),
FOREIGN KEY (to_id) REFERENCES users(id)
);
"""

rides = """
CREATE TABLE rides (
id serial PRIMARY KEY,
frow_where varchar(50),
to_where varchar(50)
);
"""

user_rides = """
CREATE TABLE user_rides (
id serial PRIMARY KEY,
passenger_id int,
ride_id int,
FOREIGN KEY (passenger_id) REFERENCES users(id),
FOREIGN KEY (ride_id) REFERENCES rides(id)
);
"""

def create_tables():
    tables = [users, messages, rides, user_rides]
    try:
        connection = connect()
        cursor = connection.cursor()
        for table in tables:
            try:
                cursor.execute(table)
            except errors.DuplicateTable as e:
                print(f"Tabela już instnieje", e)
        connection.close()
    except errors.OperationalError as e:
        print("Cant connect", e)

if __name__ == "__main__":
    create_tables()
