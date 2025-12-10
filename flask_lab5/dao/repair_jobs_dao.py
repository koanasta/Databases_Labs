from db import get_connection


class RepairJobsDAO:

    def get_spare_parts_for_repair_job(self, repair_job_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT sp.idspare_parts, sp.name, sp.price, sp.stock_quantity, rjsp.quantity
                FROM repair_job_spare_part rjsp
                JOIN spare_parts sp ON sp.idspare_parts = rjsp.spare_part_id
                WHERE rjsp.repair_job_id = %s
            """, (repair_job_id,))

            rows = cursor.fetchall()
            result = []

            for row in rows:
                result.append({
                    "idspare_parts": row[0],
                    "name": row[1],
                    "price": row[2],
                    "stock_quantity": row[3],
                    "quantity_used": row[4]
                })

            return result

        finally:
            cursor.close()
            conn.close()
