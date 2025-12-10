# dao/repair_job_spare_part_dao.py
from db import get_connection
from models.reapir_job_spare_part import RepairJobSparePart

class RepairJobSparePartDAO:

    def add_spare_part(self, m: RepairJobSparePart):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO repair_job_spare_part (repair_job_id, spare_part_id, quantity)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity)
            """, (m.repair_job_id, m.spare_part_id, m.quantity))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    def update_quantity(self, repair_job_id, spare_part_id, quantity):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE repair_job_spare_part
                SET quantity = %s
                WHERE repair_job_id = %s AND spare_part_id = %s
            """, (quantity, repair_job_id, spare_part_id))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    def delete_spare_part(self, repair_job_id, spare_part_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                DELETE FROM repair_job_spare_part
                WHERE repair_job_id = %s AND spare_part_id = %s
            """, (repair_job_id, spare_part_id))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    def get_all_for_job(self, repair_job_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT repair_job_id, spare_part_id, quantity
                FROM repair_job_spare_part
                WHERE repair_job_id = %s
            """, (repair_job_id,))
            rows = cursor.fetchall()
            return [RepairJobSparePart(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()
