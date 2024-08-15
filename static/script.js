document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('pdf-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const pdfUrl = document.getElementById('pdf-link').value;
        const outputArea = document.getElementById('output');

        outputArea.value = 'Processing...';

        fetch('/process_pdf', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({pdf_url: pdfUrl}),
        })
        .then(response => response.json())
        .then(data => {
            outputArea.value = data.text;
        })
        .catch((error) => {
            outputArea.value = 'Error: ' + error;
        });
    });

    document.getElementById('copy-button').addEventListener('click', function() {
        const outputArea = document.getElementById('output');
        outputArea.select();
        document.execCommand('copy');
        
        const indicator = document.getElementById('copy-indicator');
        indicator.classList.add('show');
        setTimeout(() => {
            indicator.classList.remove('show');
        }, 2000);
    });
});