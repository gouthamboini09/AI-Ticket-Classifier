from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
responses = pickle.load(open("responses.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    text = request.json["ticket"]

    X = vectorizer.transform([text])

    prediction = model.predict(X)[0]

    probability = max(model.predict_proba(X)[0])

    return jsonify({
        "category": prediction,
        "confidence": round(probability * 100, 2),
        "response": responses[prediction]
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)