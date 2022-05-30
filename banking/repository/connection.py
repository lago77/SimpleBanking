import psycopg2

def get_connection():
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="jangonine",
        host="mydatabase.ctl5rimbfjcl.us-east-1.rds.amazonaws.com",
        port="5430"
    )

    return connection
    