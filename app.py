from flask import Flask, request, jsonify, render_template
import joblib
import traceback
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Load stopwords
stop_words = set(stopwords.words('english'))

# Preprocessing function
def preprocess_text(text):
    if not isinstance(text, str):
        return ''
    return ' '.join(
        [word for word in word_tokenize(text.lower()) if word.isalpha() and word not in stop_words]
    )

# ✅ Load pretrained model
model = joblib.load("sentiment_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')  # simple UI

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        tweet = data.get("tweet")

        if not tweet:
            return jsonify({"error": "No tweet provided"}), 400

        preprocessed_tweet = preprocess_text(tweet)
        sentiment = model.predict([preprocessed_tweet])[0]

        return jsonify({"sentiment": sentiment})

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
