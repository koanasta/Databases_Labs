# dao/equipment_type_dao.py
from config.db import get_connection
from models.equipment_type import EquipmentType

class EquipmentTypeDAO:

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM equipment_types")
            rows = cursor.fetchall()
            return [EquipmentType(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()

    def get_by_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM equipment_types WHERE idequipment_types = %s", (id,))
            row = cursor.fetchone()
            return EquipmentType(*row) if row else None
        finally:
            cursor.close()
            conn.close()

    def create(self, et: EquipmentType):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO equipment_types (name, description)
                VALUES (%s, %s)
            """, (et.name, et.description))
            conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conn.close()

    def update(self, id, et: EquipmentType):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE equipment_types
                SET name = %s, description = %s
                WHERE idequipment_types = %s
            """, (et.name, et.description, id))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    def delete(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM equipment_types WHERE idequipment_types = %s", (id,))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()
