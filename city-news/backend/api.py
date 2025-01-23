# api.py

from flask import Flask, jsonify
from newsfeed import fetch_news, format_news

app = Flask(__name__)

@app.route("/api/news", methods=["GET"])
def get_news():
    """
    Serve the latest news stories to the frontend.
    """
    try:
        news = fetch_news()
        formatted = format_news(news)
        return jsonify(formatted)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
