from flask import Blueprint, request, jsonify
import mysql.connector
from db import db_config  # Імпортуємо словник конфігурації

stored_procedures_bp = Blueprint('stored_procedures', __name__, url_prefix='/sp')


# Універсальна функція для виклику SP
def execute_sp_with_params(sp_name, params=None):
    conn = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.callproc(sp_name, params or [])

        results = []
        for result in cursor.stored_results():
            columns = [column[0] for column in result.description]
            for row in result:
                results.append(dict(zip(columns, row)))

        conn.commit()
        cursor.close()
        return results, None

    except mysql.connector.Error as err:
        return None, f"MySQL Error: {err.msg}"
    except Exception as e:
        return None, f"General Error: {str(e)}"
    finally:
        if conn and conn.is_connected():
            conn.close()


## 1. Параметризована вставка (InsertEquipmentType)
@stored_procedures_bp.route('/equipment-type', methods=['POST'])
def call_insert_equipment_type():
    data = request.json
    try:
        params = [data['name'], data['description']]
    except KeyError:
        return jsonify({"error": "Missing 'name' or 'description'"}), 400

    results, error = execute_sp_with_params('InsertEquipmentType', params)

    if error:
        return jsonify({"error": error}), 400
    return jsonify({"message": f"New equipment type '{data['name']}' inserted."}), 201


## 2. Реалізація зв'язку M:M (LinkPartToJob)
@stored_procedures_bp.route('/link-part-to-job', methods=['POST'])
def call_link_part_to_job():
    data = request.json
    try:
        # p_equipment_model, p_spare_part_name, p_quantity
        params = [data['equipment_model'], data['spare_part_name'], data['quantity']]
    except KeyError:
        return jsonify({"error": "Missing 'equipment_model', 'spare_part_name' or 'quantity'"}), 400

    results, error = execute_sp_with_params('LinkPartToJob', params)

    if error:
        return jsonify({"error": error}), 400
    return jsonify({
                       "message": f"Link created for job related to '{data['equipment_model']}' and part '{data['spare_part_name']}'."}), 201


## 3. Пакетна вставка (BulkInsertNoname)
@stored_procedures_bp.route('/bulk-insert-manufacturers', methods=['POST'])
def call_bulk_insert_noname():
    results, error = execute_sp_with_params('BulkInsertNoname')

    if error:
        return jsonify({"error": error}), 400
    return jsonify({"message": "10 Noname manufacturers successfully inserted via SP."}), 201


## 4. Виклик функції Max/Min/Sum/Avg (ShowAggregate)
# GET /sp/aggregate?table=spare_parts&column=price&operation=AVG
@stored_procedures_bp.route('/aggregate', methods=['GET'])
def call_show_aggregate():
    p_table = request.args.get('table')
    p_column = request.args.get('column')
    print(request.args.get('operation'), True)
    p_operation = request.args.get('operation')

    if not all([p_table, p_column, p_operation]):
        return jsonify({"error": "Missing query parameters: table, column, operation (MAX, MIN, SUM, AVG)"}), 400

    # Оскільки процедура ShowAggregate тепер повертає результат через SELECT,
    # ми викликаємо її без OUT-параметрів.
    params = [p_table, p_column, p_operation.upper()]

    results, error = execute_sp_with_params('ShowAggregate', params)  # Використовуємо існуючу функцію-обгортку

    if error:
        return jsonify({"error": error}), 400

    # Решта логіки залишається незмінною, оскільки обгортка execute_sp_with_params
    # вже вміє читати результати SELECT, що повертає процедура.
    return jsonify({
        "operation": p_operation.upper(),
        "table": p_table,
        "column": p_column,
        "result": results[0]['AggregateResult'] if results and 'AggregateResult' in results[0] else None
    })

## 5. Процедура з курсором (create_random_tables_from_equipment)
@stored_procedures_bp.route('/create-random-tables-from-equipment', methods=['POST'])
def call_create_random_tables():
    results, error = execute_sp_with_params('create_random_tables_from_equipment')

    if error:
        return jsonify({"error": error}), 400
    return jsonify({"message": "Random tables created via SP with cursor based on equipment models."}), 201