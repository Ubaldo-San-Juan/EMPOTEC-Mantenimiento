from flask import Flask, jsonify, request
from admin import AdminBackend
from cursos import Usuario
from models.db import Database

app = Flask(__name__)


usuario_admin = Usuario(id=1, nombre="Admin", rol="admin", permisos=["ver_cursos", "ver_inscripciones", "ver_progreso_lecciones", "eliminar_inscripciones"])


backend = AdminBackend(usuario_admin)

@app.route("/cursos", methods=["GET"])
def obtener_todos_los_cursos():
    try:
        cursos = backend.ver_todos_los_cursos()
        return jsonify(cursos), 200
    except PermissionError as e:
        return jsonify({"error": str(e)}), 403

@app.route("/cursos/<int:curso_id>", methods=["GET"])
def obtener_detalle_curso(curso_id):
    try:
        curso = backend.ver_detalle_curso(curso_id)
        return jsonify(curso), 200
    except PermissionError as e:
        return jsonify({"error": str(e)}), 403

@app.route("/inscripciones/<int:usuario_id>", methods=["GET"])
def obtener_inscripciones_usuario(usuario_id):
    try:
        inscripciones = backend.ver_inscripciones_de_usuario(usuario_id)
        return jsonify(inscripciones), 200
    except PermissionError as e:
        return jsonify({"error": str(e)}), 403

@app.route("/progreso/<int:usuario_id>", methods=["GET"])
def obtener_progreso_usuario(usuario_id):
    try:
        progreso = backend.ver_progreso_de_lecciones_de_usuario(usuario_id)
        return jsonify(progreso), 200
    except PermissionError as e:
        return jsonify({"error": str(e)}), 403

@app.route("/eliminar_inscripcion/<int:inscripcion_id>", methods=["DELETE"])
def eliminar_inscripcion(inscripcion_id):
    try:
        resultado = backend.eliminar_inscripcion(inscripcion_id)
        return jsonify({"mensaje": "Inscripción eliminada correctamente"}), 200
    except PermissionError as e:
        return jsonify({"error": str(e)}), 403

if __name__ == "__main__":
    app.run(debug=True)
