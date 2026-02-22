from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import uuid

app = Flask(__name__)
CORS(app)

# In-memory store (replace with DB in production)
notes = {}

# ──────────────────────────────────────────
#  HEALTH CHECK
# ──────────────────────────────────────────

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }), 200


# ──────────────────────────────────────────
#  GET ALL NOTES
# ──────────────────────────────────────────

@app.route("/api/notes", methods=["GET"])
def get_notes():
    return jsonify({
        "success": True,
        "count": len(notes),
        "notes": list(notes.values())
    }), 200


# ──────────────────────────────────────────
#  GET SINGLE NOTE
# ──────────────────────────────────────────

@app.route("/api/notes/<note_id>", methods=["GET"])
def get_note(note_id):
    note = notes.get(note_id)
    if not note:
        return jsonify({"success": False, "error": "Note not found"}), 404
    return jsonify({"success": True, "note": note}), 200


# ──────────────────────────────────────────
#  CREATE NOTE
# ──────────────────────────────────────────

@app.route("/api/notes", methods=["POST"])
def create_note():
    data = request.get_json()

    if not data or not data.get("title") or not data.get("content"):
        return jsonify({
            "success": False,
            "error": "title and content are required"
        }), 400

    note_id = str(uuid.uuid4())
    note = {
        "id": note_id,
        "title": data["title"].strip(),
        "content": data["content"].strip(),
        "tag": data.get("tag", "general"),
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }

    notes[note_id] = note
    return jsonify({"success": True, "note": note}), 201


# ──────────────────────────────────────────
#  UPDATE NOTE
# ──────────────────────────────────────────

@app.route("/api/notes/<note_id>", methods=["PUT"])
def update_note(note_id):
    note = notes.get(note_id)
    if not note:
        return jsonify({"success": False, "error": "Note not found"}), 404

    data = request.get_json()
    if data.get("title"):
        note["title"] = data["title"].strip()
    if data.get("content"):
        note["content"] = data["content"].strip()
    if data.get("tag"):
        note["tag"] = data["tag"]

    note["updated_at"] = datetime.utcnow().isoformat()
    notes[note_id] = note

    return jsonify({"success": True, "note": note}), 200


# ──────────────────────────────────────────
#  DELETE NOTE
# ──────────────────────────────────────────

@app.route("/api/notes/<note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = notes.pop(note_id, None)
    if not note:
        return jsonify({"success": False, "error": "Note not found"}), 404
    return jsonify({"success": True, "message": "Note deleted"}), 200


# ──────────────────────────────────────────
#  SEARCH NOTES
# ──────────────────────────────────────────

@app.route("/api/notes/search", methods=["GET"])
def search_notes():
    query = request.args.get("q", "").lower()
    if not query:
        return jsonify({"success": False, "error": "Query param 'q' is required"}), 400

    results = [
        n for n in notes.values()
        if query in n["title"].lower() or query in n["content"].lower()
    ]

    return jsonify({
        "success": True,
        "count": len(results),
        "notes": results
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
