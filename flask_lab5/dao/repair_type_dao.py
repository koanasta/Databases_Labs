# dao/repair_type_dao.py
from db import get_connection
from models.repair_type import RepairType

class RepairTypeDAO:

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM repair_types")
            rows = cursor.fetchall()
            return [RepairType(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()

    def get_by_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM repair_types WHERE idrepair_types = %s", (id,))
            row = cursor.fetchone()
            return RepairType(*row) if row else None
        finally:
            cursor.close()
            conn.close()

    def create(self, rt: RepairType):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO repair_types (name, description)
                VALUES (%s, %s)
            """, (rt.name, rt.description))
            conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conn.close()

    def update(self, id, rt: RepairType):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE repair_types
                SET name = %s, description = %s
                WHERE idrepair_types = %s
            """, (rt.name, rt.description, id))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    def delete(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM repair_types WHERE idrepair_types = %s", (id,))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()
