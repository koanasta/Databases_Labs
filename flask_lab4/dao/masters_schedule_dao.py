# dao/masters_schedule_dao.py
from config.db import get_connection
from models.master_schedule import MastersSchedule

class MastersScheduleDAO:

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM masters_schedule")
            rows = cursor.fetchall()
            return [MastersSchedule(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()

    def get_by_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM masters_schedule WHERE idmasters_schedule = %s", (id,))
            row = cursor.fetchone()
            return MastersSchedule(*row) if row else None
        finally:
            cursor.close()
            conn.close()

    def create(self, ms: MastersSchedule):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO masters_schedule (masters_id, work_date, shift)
                VALUES (%s, %s, %s)
            """, (ms.masters_id, ms.work_date, ms.shift))
            conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conn.close()

    def update(self, id, ms: MastersSchedule):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE masters_schedule
                SET masters_id = %s, work_date = %s, shift = %s
                WHERE idmasters_schedule = %s
            """, (ms.masters_id, ms.work_date, ms.shift, id))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    def delete(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM masters_schedule WHERE idmasters_schedule = %s", (id,))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()
