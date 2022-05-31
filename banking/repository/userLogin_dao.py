import psycopg2
from repository.connection import get_connection
from models.login_dto import Login
# DAO = Data Access Object
# For database interaction


def select_user_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM userLogin WHERE user_id = {user_id};"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_login = Login(record[0], record[1], record[2])
            return user_login
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def select_user(username):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM userLogin WHERE username = '{username}';"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_login = Login(record[0], record[1], record[2])
            return user_login
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_user(username, password):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO userLogin VALUES (default, %s, %s) RETURNING user_id;"


    try:
        cursor.execute(qry, (username, password))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()


def delete_user(username,password):
    connection = get_connection()
    cursor = connection.cursor()
    print("we are connecting")
    qry = "DELETE FROM userlogin WHERE username = %s AND password = %s;"

    try:
        cursor.execute(qry, (username,password))
        # id = cursor.fetchone()[0]
        connection.commit()
        print("my id is",str(id))
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def delete_user_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    print("we are connecting")
    
    qry = "DELETE FROM userlogin WHERE user_id=%s;"

    try:
        cursor.execute(qry,(id,))
        # id = cursor.fetchone()[0]
        connection.commit()
        print("my id is",str(id))
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def update_password(user_id, newpass):
    connection = get_connection()
    cursor = connection.cursor()
    print("we are connecting")
    qry = "UPDATE userLogin SET password=%s WHERE user_id = %s RETURNING user_id;"

    try:
        cursor.execute(qry, (newpass,user_id))
        id = cursor.fetchone()[0]
        connection.commit()
        print("my id is",str(id))
        print("new password is", newpass)
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()