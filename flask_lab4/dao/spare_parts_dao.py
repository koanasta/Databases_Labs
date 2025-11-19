# dao/spare_parts_dao.py
from config.db import get_connection
from models.spare_part import SparePart

class SparePartsDAO:

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idspare_parts, name, price, stock_quantity
                FROM spare_parts
            """)
            rows = cursor.fetchall()
            return [SparePart(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()

    def get_by_id(self, part_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idspare_parts, name, price, stock_quantity
                FROM spare_parts
                WHERE idspare_parts = %s
            """, (part_id,))
            row = cursor.fetchone()
            return SparePart(*row) if row else None
        finally:
            cursor.close()
            conn.close()

    def create(self, part: SparePart):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO spare_parts (name, price, stock_quantity)
                VALUES (%s, %s, %s)
            """, (part.name, part.price, part.stock_quantity))
            conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conn.close()

    def update(self, part_id, part: SparePart):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE spare_parts
                SET name=%s, price=%s, stock_quantity=%s
                WHERE idspare_parts=%s
            """, (part.name, part.price, part.stock_quantity, part_id))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    def delete(self, part_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM spare_parts WHERE idspare_parts = %s", (part_id,))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()
