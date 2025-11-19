from config.db import get_connection
from models.client import Client

class ClientsDAO:

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idclients, full_name, phone, email, registration_date
                FROM clients
            """)
            rows = cursor.fetchall()
            return [Client(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()

    def get_by_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idclients, full_name, phone, email, registration_date
                FROM clients WHERE idclients = %s
            """, (id,))
            row = cursor.fetchone()
            return Client(*row) if row else None
        finally:
            cursor.close()
            conn.close()

    def create(self, client: Client):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO clients (full_name, phone, email, registration_date)
                VALUES (%s, %s, %s, %s)
            """, (client.full_name, client.phone, client.email, client.registration_date))
            conn.commit()
            client_id = cursor.lastrowid
            return client_id
        finally:
            cursor.close()
            conn.close()

    def update(self, id, client: Client):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE clients
                SET full_name = %s, phone = %s, email = %s, registration_date = %s
                WHERE idclients = %s
            """, (client.full_name, client.phone, client.email, client.registration_date, id))
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
