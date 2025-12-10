from flask import Blueprint, jsonify, request
from services.clients_service import ClientsService

clients_bp = Blueprint("clients_bp", __name__, url_prefix="/clients")
service = ClientsService()

@clients_bp.route("/", methods=["GET"])
def get_clients():
    return jsonify(service.get_all_clients()), 200

@clients_bp.route("/<int:id>", methods=["GET"])
def get_client(id):
    result = service.get_client(id)
    return (jsonify(result), 200) if result else (jsonify({"error": "Not found"}), 404)

@clients_bp.route("/", methods=["POST"])
def create_client():
    data = request.get_json()
    new_id = service.create_client(data)
    return jsonify({"id": new_id}), 201

@clients_bp.route("/<int:id>", methods=["PUT"])
def update_client(id):
    data = request.get_json()
    updated = service.update_client(id, data)
    return jsonify({"updated": updated}), 200

@clients_bp.route("/<int:id>", methods=["DELETE"])
def delete_client(id):
    try:
        deleted = service.delete_client(id)
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # FK error → 400 Bad Request

    if deleted and deleted > 0:
        return '', 204  # No Content
    return jsonify({"error": "Клієнта не знайдено"}), 404
