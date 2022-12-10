import psycopg2

#DB_URL = "host='localhost' port = '5432' dbname='postgres' user='post' password='1234' "
DB_URL = "host='postgres' port = '5432' dbname='ticket' user='program' password='test' "
# password = "test"
# user = "program"
# dbname = "postgres"
# port = "5432"
# host = "postgres"
# database = "flight"

password = "1234"
user = "post"
port = "5432"
host = "localhost"
database = "postgres"


def create_ticketsdb():
    db = psycopg2.connect(DB_URL, sslmode="require")
    cursor = db.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS ticket
                    (
                    id            SERIAL PRIMARY KEY,
                    ticket_uid    uuid UNIQUE NOT NULL,
                    username      VARCHAR(80) NOT NULL,
                    flight_number VARCHAR(20) NOT NULL,
                    price         INT         NOT NULL,
                    status        VARCHAR(20) NOT NULL
                        CHECK (status IN ('PAID', 'CANCELED'))
                    );
                   """)
    db.commit()
    cursor.close()
    db.close()
    return


def get_user_flight(user: str):
    db = psycopg2.connect(DB_URL, sslmode="require")
    cursor = db.cursor()
    cursor.execute(f"""SELECT ticket_uid, flight_number, price, status
                       FROM ticket 
                       WHERE ticket.username = '{user}';""")
    flight = cursor.fetchall()
    cursor.close()
    db.close()
    return flight


def get_one_flight(ticketUid: str, user: str):
    db = psycopg2.connect(DB_URL, sslmode="require")
    cursor = db.cursor()
    cursor.execute(f"""SELECT ticket_uid, flight_number, price, status 
                       FROM ticket  
                       WHERE ticket_uid = '{ticketUid}' and username = '{user}';""")
    flight = cursor.fetchone()
    cursor.close()
    db.close()
    return flight


def add_ticker(ticketUid: str, user: str, flight_number: str, price: str):
    db = psycopg2.connect(DB_URL, sslmode="require")
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO ticket (id, ticket_uid, username, flight_number, price, status) "
                   f"VALUES (DEFAULT, '{ticketUid}', '{user}', '{flight_number}', {price}, 'PAID');")
    db.commit()
    cursor.close()
    db.close()
    return True


def change_ticker_status(ticketUid: str, user: str):
    db = psycopg2.connect(DB_URL, sslmode="require")
    cursor = db.cursor()
    cursor.execute(f"""UPDATE ticket SET status = 'CANCELED' WHERE ticket_uid = '{ticketUid}' and username = '{user}'""")
    db.commit()
    cursor.close()
    db.close()
    return True
