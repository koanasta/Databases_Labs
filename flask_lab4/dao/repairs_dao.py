# dao/repairs_dao.py
from config.db import get_connection
from models.repair import Repair

class RepairsDAO:

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idrepairs, equipment_id, client_id, start_date, end_date, status
                FROM repairs
            """)
            rows = cursor.fetchall()
            return [Repair(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()

    def get_by_id(self, repair_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idrepairs, equipment_id, client_id, start_date, end_date, status
                FROM repairs WHERE idrepairs = %s
            """, (repair_id,))
            row = cursor.fetchone()
            return Repair(*row) if row else None
        finally:
            cursor.close()
            conn.close()

    def create(self, r: Repair):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO repairs (equipment_id, client_id, start_date, end_date, status)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                r.equipment_id,
                r.client_id,
                r.start_date,
                r.end_date,
                r.status
            ))
            conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conn.close()

    def update(self, repair_id, r: Repair):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE repairs
                SET equipment_id=%s, client_id=%s, start_date=%s,
                    end_date=%s, status=%s
                WHERE idrepairs=%s
            """, (
                r.equipment_id,
                r.client_id,
                r.start_date,
                r.end_date,
                r.status,
                repair_id
            ))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    def delete(self, repair_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM repairs WHERE idrepairs=%s", (repair_id,))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    # ---------- M:1 — get equipment ----------
    def get_equipment(self, repair_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT e.idequipment, e.serial_number, e.manufacturer_id,
                       e.equipment_type_id, e.model, e.warranty_until
                FROM repairs r
                JOIN equipment e ON r.equipment_id = e.idequipment
                WHERE r.idrepairs = %s
            """, (repair_id,))
            row = cursor.fetchone()
            if not row:
                return None
            return {
                "idequipment": row[0],
                "serial_number": row[1],
                "manufacturer_id": row[2],
                "equipment_type_id": row[3],
                "model": row[4],
                "warranty_until": str(row[5])
            }
        finally:
            cursor.close()
            conn.close()

    # ---------- M:1 — get client ----------
    def get_client(self, repair_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT c.idclients, c.full_name, c.phone, c.email, c.registration_date
                FROM repairs r
                JOIN clients c ON r.client_id = c.idclients
                WHERE r.idrepairs = %s
            """, (repair_id,))
            row = cursor.fetchone()
            if not row:
                return None
            return {
                "idclients": row[0],
                "full_name": row[1],
                "phone": row[2],
                "email": row[3],
                "registration_date": str(row[4])
            }
        finally:
            cursor.close()
            conn.close()

    # ---------- 1:M — get repair_jobs ----------
    def get_jobs(self, repair_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idrepair_jobs, repair_id, repair_type_id, cost, master_id
                FROM repair_jobs
                WHERE repair_id = %s
            """, (repair_id,))
            rows = cursor.fetchall()
            return [
                {
                    "idrepair_jobs": r[0],
                    "repair_id": r[1],
                    "repair_type_id": r[2],
                    "cost": r[3],
                    "master_id": r[4]
                }
                for r in rows
            ]
        finally:
            cursor.close()
            conn.close()
