from pickletools import read_unicodestring1
import psycopg2
from repository.connection import get_connection
from models.user_info_dto import User
from models.login_dto import Login
from models.account_dto import Account

def select_accounts_by_id(userid):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM useraccount WHERE user_id = {userid};"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchall()
            print("my records")
            print(record)

            if record is None:
                break
           
            # user_accounts = Account(record[0], record[1], record[2])
            print(record)
            print("end")
            return record
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def select_accounts_by_account_id(accountid):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM useraccount WHERE account_id = {accountid};"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            print("my record")
            print(record)

            if record is None:
                break
            user_accounts = Account(record[0], record[1], record[2])
            return record
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_account(userid, balance):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO useraccount VALUES (default, %s, %s) RETURNING account_id;"

    try:
        cursor.execute(qry, (userid, balance))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def update_balance(account_id, newbalance):
    connection = get_connection()
    cursor = connection.cursor()

   
    qry = "UPDATE useraccount SET balance=%s where account_id=%s RETURNING account_id"

    try:
        cursor.execute(qry, (newbalance, account_id))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()