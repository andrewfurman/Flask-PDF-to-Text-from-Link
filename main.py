from flask import Flask, render_template, request, jsonify
from pdf_processor import get_url_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    data = request.json
    pdf_url = data.get('pdf_url')
    text = get_url_text(pdf_url)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)