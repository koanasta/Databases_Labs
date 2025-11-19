from flask import Flask, jsonify
from contollers.clients_controller import clients_bp
from contollers.masters_controller import masters_bp
from contollers.equipment_controller import equipment_bp
from contollers.repairs_controller import repairs_bp
from contollers.reapir_jobs_controller import repair_jobs_bp
from contollers.spare_parts_controller import spare_parts_bp
from contollers.repair_job_spare_part_controller import rjsp_bp
from contollers.manufacturer_controller import manufacturer_bp
from contollers.equipment_type_controller import equipment_type_bp
from contollers.repair_type_controller import repair_type_bp
from contollers.masters_schedule_controller import masters_schedule_bp

app = Flask(__name__)

# register blueprints
app.register_blueprint(clients_bp)
app.register_blueprint(masters_bp)
app.register_blueprint(equipment_bp)
app.register_blueprint(repairs_bp)
app.register_blueprint(repair_jobs_bp)
app.register_blueprint(spare_parts_bp)
app.register_blueprint(rjsp_bp)
app.register_blueprint(manufacturer_bp)
app.register_blueprint(equipment_type_bp)
app.register_blueprint(repair_type_bp)
app.register_blueprint(masters_schedule_bp)


@app.route("/")
def home():
    return jsonify({"message": "Flask + MySQL API is running. Use /clients"}), 200

# simple error handler
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
