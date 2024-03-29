#!/usr/bin/env python3


from common import connect, disconnect
from create_db import create_new_database


def populate_faculty(connection):
    faculty_data = [
        (1, 'Underwater Needlework', 'Prof John Jones',),
        (2, 'High Altitude Basket Weaving', 'Dr Jane Smith',),
    ]

    cur = connection.cursor()
    cur.executemany('insert into faculty (id, name, dean) values (?, ?, ?)', faculty_data)

    cur.close()
    connection.commit()


def populate_room(connection):
    room_data = [
        (1, 'TU101', 'Turing',),
        (2, 'TU102', 'Turing',),
        (3, 'TU103', 'Turing',),
        (4, 'TU104', 'Turing',),
        (5, 'TU105', 'Turing',),
        (6, 'TU106', 'Turing',),
        (7, 'LO201', 'Lovelace',),
        (8, 'LO202', 'Lovelace',),
        (9, 'LO203', 'Lovelace',),
        (10, 'LO204', 'Lovelace',),
    ]

    cur = connection.cursor()
    cur.executemany('insert into room (id, number, building) values (?, ?, ?)', room_data)

    cur.close()
    connection.commit()


def populate_tutor(connection):
    tutor_data = [
        ('Alan Smith', 1, 1,),
        ('Billie Jackson', 1, 2,),
        ('Colin White', 2, 4,),
        ('Denise Cooper', 2, 3,),
        ('Edgar Wallace', 2, 7,),
        ('Fiona Richards', 1, 10,),
        ('Gary Steele', 1, 4,),
        ('Harriet Pugh', 2, 2,),
        ('Ian Smith', 2, 8,),
        ('Jackie Power', 1, 3,),
        ('Kevin Appleton', 1, 6,),
        ('Lucy Green', 2, 6,),
    ]

    cur = connection.cursor()
    cur.executemany('insert into tutor (name, faculty, room) values (?, ?, ?)', tutor_data)

    cur.close()
    connection.commit()


if __name__ == '__main__':

    create_new_database()

    con = connect()

    populate_faculty(con)
    populate_room(con)
    populate_tutor(con)

    disconnect(con)
