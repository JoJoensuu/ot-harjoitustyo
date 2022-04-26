from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists exercise_days;
    ''')

    connection.commit()

def create_tables(connection):

    cursor = connection.cursor()

    cursor.execute('''
        create table exercise_days (
            id serial primary key,
            date date
        );
    ''')

    connection.commit()

def initialize_database():

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_database()