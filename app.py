from flask import Flask, request, jsonify, render_template
import joblib
import nltk
import traceback

# Point NLTK to the bundled data folder (downloaded locally & committed)
nltk.data.path.append("nltk_data")

# Load your model
model = joblib.load("sentiment_model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"error": "No text provided"}), 400

        prediction = model.predict([text])[0]

        return jsonify({
            "input_text": text,
            "predicted_sentiment": prediction
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        }), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
