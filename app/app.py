from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

@app.route("/")
def home():
    return "Spam Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Get text input
    text = data.get("text")

    if not data or "text" not in data:
        return jsonify({"error": "Invalid input"}), 400

    # Convert to model input
    X = vectorizer.transform([text])

    # Predict
    prediction = model.predict(X)[0]

    result = "Spam" if prediction == 1 else "Not Spam"

    return jsonify({
        "input": text,
        "prediction": result
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)