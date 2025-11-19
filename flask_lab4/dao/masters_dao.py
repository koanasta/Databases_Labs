# dao/masters_dao.py
from config.db import get_connection
from models.master import Master

class MastersDAO:

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT idmasters, full_name, specialization, phone FROM masters")
            rows = cursor.fetchall()
            return [Master(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()

    def get_by_id(self, master_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT idmasters, full_name, specialization, phone FROM masters WHERE idmasters = %s", (master_id,))
            row = cursor.fetchone()
            return Master(*row) if row else None
        finally:
            cursor.close()
            conn.close()

    def create(self, master: Master):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO masters (full_name, specialization, phone) VALUES (%s, %s, %s)",
                (master.full_name, master.specialization, master.phone)
            )
            conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conn.close()

    def update(self, master_id, master: Master):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                UPDATE masters
                SET full_name = %s, specialization = %s, phone = %s
                WHERE idmasters = %s
                """,
                (master.full_name, master.specialization, master.phone, master_id)
            )
            conn.commit()
            return cursor.rowcount  # number of rows affected
        finally:
            cursor.close()
            conn.close()

    def delete(self, master_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM masters WHERE idmasters = %s", (master_id,))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    # M:1 example: get repair_jobs handled by this master
    def get_jobs_for_master(self, master_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT rj.idrepair_jobs, rj.repair_id, rj.repair_type_id, rj.cost, rj.master_id
                FROM repair_jobs rj
                WHERE rj.master_id = %s
            """, (master_id,))
            rows = cursor.fetchall()
            result = []
            for r in rows:
                result.append({
                    "idrepair_jobs": r[0],
                    "repair_id": r[1],
                    "repair_type_id": r[2],
                    "cost": r[3],
                    "master_id": r[4]
                })
            return result
        finally:
            cursor.close()
            conn.close()

    # M:1 example: get work schedule for this master
    def get_schedule_for_master(self, master_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idmasters_schedule, masters_id, work_date, shift
                FROM masters_schedule
                WHERE masters_id = %s
                ORDER BY work_date
            """, (master_id,))
            rows = cursor.fetchall()
            res = []
            for r in rows:
                res.append({
                    "idmasters_schedule": r[0],
                    "masters_id": r[1],
                    "work_date": str(r[2]) if r[2] else None,
                    "shift": r[3]
                })
            return res
        finally:
            cursor.close()
            conn.close()
