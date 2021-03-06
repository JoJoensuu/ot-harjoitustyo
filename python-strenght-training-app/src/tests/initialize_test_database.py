from tests.test_database_connection import get_database_connection

def drop_tables(connection):
    """Removes existing tables from database.

    Args:
        connection: connection entity for database.
    """
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists exercise_days;
    ''')

    cursor.execute('''
        drop table if exists exercises;
    ''')

    connection.commit()

def create_tables(connection):
    """Creates tables into database

    Args:
        connection: connection entity for database.
    """

    cursor = connection.cursor()

    cursor.execute('''
        create table exercise_days (
            id integer primary key,
            date date
        );
    ''')

    cursor.execute('''
        create table exercises (
            id integer primary key,
            day_id integer references exercise_days,
            name text,
            sets integer,
            reps integer,
            rest integer,
            comments text
        );
    ''')

    connection.commit()

def initialize_test_database():
    """Initializes database
    """

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_test_database()
