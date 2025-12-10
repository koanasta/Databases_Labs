# Перейменуємо функцію, щоб вона працювала як словник конфігурації для `mysql.connector.connect(**db_config)`
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Anako1603!",
    "database": "mydb"
}

# Залишаємо get_connection, щоб не ламати існуючий код в інших контролерах
def get_connection():
    import mysql.connector
    return mysql.connector.connect(**db_config)