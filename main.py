from flask import Flask, render_template, request, jsonify, send_from_directory
from getPdfUrl import get_url_text
from pdf_processor import extract_text_from_pdf
import io

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    if 'pdf_file' in request.files:
        pdf_file = request.files['pdf_file']
        if pdf_file.filename != '':
            pdf_stream = io.BytesIO(pdf_file.read())
            text = extract_text_from_pdf(pdf_stream)
            return jsonify({'text': text})
    elif 'pdf_url' in request.form:
        pdf_url = request.form['pdf_url']
        text = get_url_text(pdf_url)
        return jsonify({'text': text})
    return jsonify({'error': 'No PDF file or URL provided'}), 400

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)