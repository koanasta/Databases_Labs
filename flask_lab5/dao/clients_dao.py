import mysql.connector
from db import get_connection
from models.client import Client

class ClientsDAO:
    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clients")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Client(**row) for row in rows]

    def get_by_id(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clients WHERE idclients = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Client(**row) if row else None

    def create(self, client: Client):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO clients (full_name, phone, email, registration_date)
                VALUES (%s, %s, %s, %s)
            """, (
                client.full_name,
                client.phone,
                client.email,
                client.registration_date
            ))

            conn.commit()  # !!! Дуже важливо
            new_id = cursor.lastrowid
            return new_id

        except mysql.connector.Error as e:
            print("Insert error:", e)
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

    def update(self, id, data):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE clients
                SET full_name=%s, phone=%s, email=%s, registration_date=%s
                WHERE idclients=%s
            """, (
                data["full_name"],
                data["phone"],
                data["email"],
                data["registration_date"],
                id
            ))

            conn.commit()
            return cursor.rowcount

        finally:
            cursor.close()
            conn.close()

    def delete(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM clients WHERE idclients = %s", (id,))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()
