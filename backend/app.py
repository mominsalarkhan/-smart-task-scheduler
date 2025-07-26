from flask import Flask, request, jsonify
from model import predict_priority

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    task_text = data.get("task", "")
    priority = predict_priority(task_text)
    return jsonify({"task": task_text, "predicted_priority": priority})

# NEW: Health check or test route
@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "API is up and running!"})

if __name__ == "__main__":
    app.run(debug=True)
