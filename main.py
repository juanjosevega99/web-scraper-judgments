from flask import Flask, jsonify, request
import os
from scraper import scrape_website

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your web scrapper"})


@app.route('/scrape', methods=['GET'])
def scrape():
    file_number = request.args.get('file_number')
    if not file_number:
        return jsonify({"error": "Missing URL parameter", "status": "failed"}), 400

    result = scrape_website(file_number)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    # app.run(debug=True, port=os.getenv("PORT", default=8080))
