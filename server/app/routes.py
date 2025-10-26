import os
from flask import Blueprint, request, jsonify
from .scripts.parse_transcript import extract_all_courses

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route("/process-file", methods=["POST"])
def process_file():
    """
    Receives a PDF file from the frontend, parses it, and returns a list of course codes.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save temporarily
    tmp_path = os.path.join("/tmp", file.filename)
    file.save(tmp_path)

    courses = extract_all_courses(tmp_path)

    # Remove the temp file
    try:
        os.remove(tmp_path)
    except Exception:
        pass

    return jsonify({"output": courses}), 200
