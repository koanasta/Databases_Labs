import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anako1603!",
        database="mydb"
    )
    return connection
