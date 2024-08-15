from flask import Flask, render_template, request, jsonify, send_from_directory
from pdf_processor import get_url_text

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    data = request.json
    pdf_url = data.get('pdf_url')
    text = get_url_text(pdf_url)
    return jsonify({'text': text})

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)