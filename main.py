from flask import Flask, render_template, request, jsonify
from pdf_processor import extract_text_from_pdf_url

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    pdf_url = request.json['pdf_url']
    extracted_text = extract_text_from_pdf_url(pdf_url)
    return jsonify({'text': extracted_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)