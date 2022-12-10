import psycopg2


def create_flightsdb():
    db = psycopg2.connect(
        database="flights",
        user="program",
        password="test",
        host="10.5.0.2",
        port="5432"
    )
    cursor = db.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS airport
                    (
                        id      SERIAL PRIMARY KEY,
                        name    VARCHAR(255),
                        city    VARCHAR(255),
                        country VARCHAR(255)
                    );
                       """)
    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS flight
                        (
                            id              SERIAL PRIMARY KEY,
                            flight_number   VARCHAR(20)              NOT NULL,
                            datetime        TIMESTAMP WITH TIME ZONE NOT NULL,
                            from_airport_id INT REFERENCES airport (id),
                            to_airport_id   INT REFERENCES airport (id),
                            price           INT                      NOT NULL
                        );
                       """)
    db.commit()

    cursor.execute(f"INSERT INTO airport (id, name, city, country) "
                   f"VALUES (DEFAULT, 'Шереметьево', 'Москва', 'Россия');")
    db.commit()

    cursor.execute(f"INSERT INTO airport (id, name, city, country) "
                   f"VALUES (DEFAULT, 'Пулково', 'Санкт-Петербург', 'Россия');")
    db.commit()

    cursor.execute(f"INSERT INTO flight (id, flight_number, datetime, from_airport_id, to_airport_id, price) "
                   f"VALUES (DEFAULT, 'AFL031', timestamp '2021-10-08 20:00:00', 1, 2, 1500);")
    db.commit()


    cursor.close()
    db.close()
    return


def get_flights(page: int, size: int):
    left = str(page * size - size)
    right = str(page * size)
    db = psycopg2.connect(
        database="flights",
        user="program",
        password="test",
        host="10.5.0.2",
        port="5432"
    )
    cursor = db.cursor()
    cursor.execute(f"""SELECT flight.flight_number, airport_from.city, airport_from.name, airport_to.city, 
                       airport_to.name, flight.datetime, flight.price 
                       FROM flight 
                       JOIN airport AS airport_from ON airport_from.id = flight.from_airport_id 
                       JOIN airport AS airport_to ON airport_to.id = flight.to_airport_id 
                       WHERE flight.id > {left} and flight.id <= {right};""")
    flights = cursor.fetchall()
    cursor.close()
    db.close()
    return flights


def get_flights_bynum(flight_num: str):
    db = psycopg2.connect(
        database="flights",
        user="program",
        password="test",
        host="10.5.0.2",
        port="5432"
    )
    cursor = db.cursor()
    cursor.execute(f""" SELECT flight.flight_number, airport_from.city, airport_from.name, airport_to.city, 
                        airport_to.name, flight.datetime, flight.price 
                        FROM flight  
                        JOIN airport AS airport_from ON airport_from.id = flight.from_airport_id 
                        JOIN airport AS airport_to ON airport_to.id = flight.to_airport_id
                        WHERE flight.flight_number = '{flight_num}';""")
    flight = cursor.fetchone()
    cursor.close()
    db.close()
    return flight
