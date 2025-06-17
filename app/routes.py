from flask import Blueprint, jsonify, request

bp = Blueprint('api', __name__)

tasks = []

@bp.route('/')
def index():
    return jsonify({"message": "Flask Task API"}), 200

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {"id": len(tasks) + 1, "title": data.get("title", "")}
    tasks.append(task)
    return jsonify(task), 201

@bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return '', 204

@bp.route('/error')
def trigger_error():
    1/0  # Forzar error para probar Sentry
