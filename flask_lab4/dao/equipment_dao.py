# dao/equipment_dao.py
from config.db import get_connection
from models.equipment import Equipment

class EquipmentDAO:

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idequipment, serial_number, manufacturer_id,
                       equipment_type_id, model, warranty_until
                FROM equipment
            """)
            rows = cursor.fetchall()
            return [Equipment(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()

    def get_by_id(self, equipment_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idequipment, serial_number, manufacturer_id,
                       equipment_type_id, model, warranty_until
                FROM equipment WHERE idequipment = %s
            """, (equipment_id,))
            row = cursor.fetchone()
            return Equipment(*row) if row else None
        finally:
            cursor.close()
            conn.close()

    def create(self, eq: Equipment):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO equipment (serial_number, manufacturer_id,
                    equipment_type_id, model, warranty_until)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                eq.serial_number,
                eq.manufacturer_id,
                eq.equipment_type_id,
                eq.model,
                eq.warranty_until
            ))
            conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conn.close()

    def update(self, equipment_id, eq: Equipment):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE equipment SET
                    serial_number=%s, manufacturer_id=%s,
                    equipment_type_id=%s, model=%s, warranty_until=%s
                WHERE idequipment=%s
            """, (
                eq.serial_number,
                eq.manufacturer_id,
                eq.equipment_type_id,
                eq.model,
                eq.warranty_until,
                equipment_id
            ))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    def delete(self, equipment_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM equipment WHERE idequipment=%s", (equipment_id,))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    # M:1 → manufacturers
    def get_manufacturer(self, equipment_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT m.idmanufacturers, m.name, m.country, m.website, m.phone
                FROM equipment e
                JOIN manufacturers m ON e.manufacturer_id = m.idmanufacturers
                WHERE e.idequipment = %s
            """, (equipment_id,))
            row = cursor.fetchone()
            if not row:
                return None
            return {
                "idmanufacturers": row[0],
                "name": row[1],
                "country": row[2],
                "website": row[3],
                "phone": row[4],
            }
        finally:
            cursor.close()
            conn.close()

    # M:1 → equipment_types
    def get_equipment_type(self, equipment_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT et.idequipment_types, et.name, et.description
                FROM equipment e
                JOIN equipment_types et ON e.equipment_type_id = et.idequipment_types
                WHERE e.idequipment = %s
            """, (equipment_id,))
            row = cursor.fetchone()
            if not row:
                return None
            return {
                "idequipment_types": row[0],
                "name": row[1],
                "description": row[2]
            }
        finally:
            cursor.close()
            conn.close()

    # 1:M → repairs
    def get_repairs(self, equipment_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idrepairs, equipment_id, client_id, start_date, end_date, status
                FROM repairs
                WHERE equipment_id = %s
            """, (equipment_id,))
            rows = cursor.fetchall()
            return [
                {
                    "idrepairs": r[0],
                    "equipment_id": r[1],
                    "client_id": r[2],
                    "start_date": str(r[3]) if r[3] else None,
                    "end_date": str(r[4]) if r[4] else None,
                    "status": r[5]
                }
                for r in rows
            ]
        finally:
            cursor.close()
            conn.close()
