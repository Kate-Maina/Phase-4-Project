from flask import Flask, request, jsonify
import joblib
import traceback

# Load the trained model
# Make sure you already saved it as: joblib.dump(pipeline_multi2, "sentiment_model.pkl")
model = joblib.load("sentiment_model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Sentiment Analysis API! Use the /predict endpoint."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Expecting JSON input like: {"text": "I love this product!"}
        data = request.get_json(force=True)
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"error": "No text provided"}), 400

        # Predict sentiment
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
