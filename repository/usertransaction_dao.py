import psycopg2
from repository.connection import get_connection
from models.user_info_dto import User
from models.login_dto import Login
from models.account_dto import Account
from models.transaction_dto import Transactions

def select_transactions_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM usertransactions WHERE user_id = {user_id};"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchall()
            if record is None:
                break
            # user_transaction= Transactions(record[0], record[1], record[2], record[3], record[4])
            return record
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def insert_transaction(userid, account_id, amount, type):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO usertransactions VALUES (default,%s, %s, %s, %s) RETURNING trans_id;"

    try:
        cursor.execute(qry, (userid,account_id, amount, type))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

