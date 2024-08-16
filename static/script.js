document.addEventListener('DOMContentLoaded', function() {
    const outputArea = document.getElementById('output');
    const wordCountElement = document.getElementById('word-count');
    const tokenCountElement = document.getElementById('token-count');
    const pdfLinkInput = document.getElementById('pdf-link');
    let firstFocus = true;

    function updateCounts() {
        const text = outputArea.value.trim();
        const wordCount = text ? text.split(/\s+/).length : 0;
        const tokenCount = Math.round(wordCount * 0.75);
        wordCountElement.textContent = `🆎 Words: ${wordCount}`;
        tokenCountElement.textContent = `🪙 Tokens: ${tokenCount}`;
    }

    document.getElementById('pdf-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const pdfUrl = pdfLinkInput.value;

        outputArea.value = 'Processing...';
        updateCounts();

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
            updateCounts();
        })
        .catch((error) => {
            outputArea.value = 'Error: ' + error;
            updateCounts();
        });
    });

    document.getElementById('copy-button').addEventListener('click', function() {
        outputArea.select();
        document.execCommand('copy');

        const indicator = document.getElementById('copy-indicator');
        indicator.classList.add('show');
        setTimeout(() => {
            indicator.classList.remove('show');
        }, 2000);
    });

    outputArea.addEventListener('input', updateCounts);

    updateCounts();

    pdfLinkInput.addEventListener('focus', async () => {
        if (firstFocus) {
            firstFocus = false;
            pdfLinkInput.value = '';

            try {
                const text = await navigator.clipboard.readText();
                if (text) {
                    pdfLinkInput.value = text;
                }
            } catch (err) {
                console.error('Failed to read clipboard contents: ', err);
            }
        }
    });
});