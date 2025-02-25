from flask import Flask, request, jsonify
from backend.models.resume_parser import extract_text_from_pdf
from backend.models.scorer import analyze_resume
import os

app = Flask(__name__)

@app.route("/analyze_resume", methods=["POST"])
def analyze_resume_endpoint():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    temp_path = "temp_resume.pdf"
    file.save(temp_path)
    
    # Extract text from PDF
    text = extract_text_from_pdf(temp_path)
    os.remove(temp_path)
    
    # Analyze the resume
    result = analyze_resume(text)
    
    return jsonify(result)

if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
    app.run(debug=True)
