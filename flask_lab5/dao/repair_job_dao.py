# dao/repair_jobs_dao.py
from db import get_connection
from models.repair_job import RepairJob

class RepairJobsDAO:

    # ---------- BASIC CRUD ----------

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idrepair_jobs, repair_id, repair_type_id, cost, master_id
                FROM repair_jobs
            """)
            rows = cursor.fetchall()
            return [RepairJob(*row) for row in rows]
        finally:
            cursor.close()
            conn.close()

    def get_by_id(self, job_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT idrepair_jobs, repair_id, repair_type_id, cost, master_id
                FROM repair_jobs
                WHERE idrepair_jobs = %s
            """, (job_id,))
            row = cursor.fetchone()
            return RepairJob(*row) if row else None
        finally:
            cursor.close()
            conn.close()

    def create(self, job: RepairJob):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO repair_jobs (repair_id, repair_type_id, cost, master_id)
                VALUES (%s, %s, %s, %s)
            """, (job.repair_id, job.repair_type_id, job.cost, job.master_id))
            conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conn.close()

    def update(self, job_id, job: RepairJob):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE repair_jobs
                SET repair_id=%s, repair_type_id=%s, cost=%s, master_id=%s
                WHERE idrepair_jobs=%s
            """, (job.repair_id, job.repair_type_id, job.cost, job.master_id, job_id))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    def delete(self, job_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM repair_jobs WHERE idrepair_jobs = %s", (job_id,))
            conn.commit()
            return cursor.rowcount
        finally:
            cursor.close()
            conn.close()

    # ---------- M:1 FETCHERS ----------

    def get_repair(self, job_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT r.idrepairs, r.equipment_id, r.client_id,
                       r.start_date, r.end_date, r.status
                FROM repair_jobs j
                JOIN repairs r ON j.repair_id = r.idrepairs
                WHERE j.idrepair_jobs = %s
            """, (job_id,))
            row = cursor.fetchone()
            if not row:
                return None
            return {
                "idrepairs": row[0],
                "equipment_id": row[1],
                "client_id": row[2],
                "start_date": str(row[3]),
                "end_date": str(row[4]),
                "status": row[5]
            }
        finally:
            cursor.close()
            conn.close()

    def get_type(self, job_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT rt.idrepair_types, rt.name, rt.description
                FROM repair_jobs j
                JOIN repair_types rt ON j.repair_type_id = rt.idrepair_types
                WHERE j.idrepair_jobs = %s
            """, (job_id,))
            row = cursor.fetchone()
            if not row:
                return None
            return {
                "idrepair_types": row[0],
                "name": row[1],
                "description": row[2]
            }
        finally:
            cursor.close()
            conn.close()

    def get_master(self, job_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT m.idmasters, m.full_name, m.specialization, m.phone
                FROM repair_jobs j
                JOIN masters m ON j.master_id = m.idmasters
                WHERE j.idrepair_jobs = %s
            """, (job_id,))
            row = cursor.fetchone()
            if not row:
                return None
            return {
                "idmasters": row[0],
                "full_name": row[1],
                "specialization": row[2],
                "phone": row[3]
            }
        finally:
            cursor.close()
            conn.close()

    # ---------- M:M spare_parts ----------

    def get_spare_parts(self, job_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT sp.idspare_parts, sp.name, sp.price, sp.stock_quantity,
                       rjsp.quantity
                FROM repair_job_spare_part rjsp
                JOIN spare_parts sp ON sp.idspare_parts = rjsp.spare_part_id
                WHERE rjsp.repair_job_id = %s
            """, (job_id,))
            rows = cursor.fetchall()
            return [
                {
                    "idspare_parts": r[0],
                    "name": r[1],
                    "price": r[2],
                    "stock_quantity": r[3],
                    "quantity_used": r[4]
                }
                for r in rows
            ]
        finally:
            cursor.close()
            conn.close()
