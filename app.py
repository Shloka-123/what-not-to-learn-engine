from flask_cors import CORS
from flask import Flask, request, jsonify
import json
from explanation import generate_explanation

app = Flask(__name__)
CORS(app)
# Load dataset
with open("skills.json") as f:
    skills_data = json.load(f)

@app.route('/')
def home():
    return "Backend is running"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    skill_name = data.get("skill").lower()

    # Check if skill exists
    if skill_name not in skills_data:
        return jsonify({"error": "Skill not found"})

    skill = skills_data[skill_name]

    # 🔥 Use AI explanation engine
    result = generate_explanation(skill_name, skill)

    return jsonify(result)

# Run server
if __name__ == '__main__':
    app.run(debug=True)