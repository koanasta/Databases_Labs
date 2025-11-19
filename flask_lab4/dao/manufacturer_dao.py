# dao/manufacturer_dao.py
from config.db import get_connection
from models.manufacturer import Manufacturer

class ManufacturerDAO:

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM manufacturers")
            rows = cursor.fetchall()
            return [Manufacturer(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()

    def get_by_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM manufacturers WHERE idmanufacturers = %s", (id,))
            row = cursor.fetchone()
            return Manufacturer(*row) if row else None
        finally:
            cursor.close()
            conn.close()

    def create(self, m: Manufacturer):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO manufacturers (name, country, website, phone)
                VALUES (%s, %s, %s, %s)
            """, (m.name, m.country, m.website, m.phone))
            conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conn.close()

    def update(self, id, m: Manufacturer):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE manufacturers
                SET name = %s, country = %s, website = %s, phone = %s
                WHERE idmanufacturers = %s
            """, (m.name, m.country, m.website, m.phone, id))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    def delete(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM manufacturers WHERE idmanufacturers = %s", (id,))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()
