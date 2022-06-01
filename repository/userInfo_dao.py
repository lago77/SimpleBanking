import psycopg2
from repository.connection import get_connection
from models.user_info_dto import User
from models.login_dto import Login

def select_user_info_by_id(info_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM userInfo WHERE info_id = {info_id};"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_info = User(record[0], record[1], record[2], record[3],record[4],record[5],record[6])
            return user_info
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def select_by_user(userid):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM userInfo WHERE user_id = {userid};"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_info = User(record[0], record[1], record[2], record[3],record[4],record[5],record[6])
            return user_info
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_user_info(userid, first_name, last_name, email, address, phone_number):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO userInfo VALUES (default, %s, %s, %s, %s, %s, %s) RETURNING info_id;"

    try:
        cursor.execute(qry, (userid, first_name, last_name, email, address, phone_number))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def update_user_info(userid, first_name, last_name, email, address, phone_number):
    connection = get_connection()
    cursor = connection.cursor()
    print("going to query")
    qry = "UPDATE userInfo SET first_name=%s, last_name=%s, email=%s, address=%s, phone_number=%s where user_id=%s RETURNING info_id"

    try:
        cursor.execute(qry, (first_name, last_name, email, address, phone_number, userid))
        id = cursor.fetchone()[0]
        connection.commit()
        print("returning id")
        print(id)
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()