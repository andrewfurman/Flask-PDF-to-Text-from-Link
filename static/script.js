document.addEventListener('DOMContentLoaded', function() {
    const outputArea = document.getElementById('output');
    const wordCountElement = document.getElementById('word-count');
    const tokenCountElement = document.getElementById('token-count');
    const pdfLinkInput = document.getElementById('pdf-link');
    const pdfFileInput = document.getElementById('pdf-file');
    const clearFileButton = document.getElementById('clear-file');
    let firstFocus = true;

    function updateCounts() {
        const text = outputArea.textContent.trim();
        const wordCount = text ? text.split(/\s+/).length : 0;
        const tokenCount = Math.round(wordCount * 0.75);
        wordCountElement.textContent = `🆎 Words: ${wordCount}`;
        tokenCountElement.textContent = `🪙 Tokens: ${tokenCount}`;
    }

    clearFileButton.addEventListener('click', function() {
        pdfFileInput.value = '';
        pdfLinkInput.disabled = false;
    });

    pdfFileInput.addEventListener('change', function() {
        if (pdfFileInput.value) {
            pdfLinkInput.disabled = true;
        } else {
            pdfLinkInput.disabled = false;
        }
    });

    document.getElementById('pdf-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const pdfUrl = pdfLinkInput.value;
        const pdfFile = pdfFileInput.files[0];

        outputArea.innerHTML = 'Processing...';
        updateCounts();

        let formData = new FormData();
        if (pdfFile) {
            formData.append('pdf_file', pdfFile);
        } else if (pdfUrl) {
            formData.append('pdf_url', pdfUrl);
        } else {
            outputArea.textContent = 'Error: Please provide either a PDF URL or upload a PDF file.';
            updateCounts();
            return;
        }

        fetch('/process_pdf', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            const formattedText = data.text.replace(/\n/g, '<br>');
            outputArea.innerHTML = formattedText;
            updateCounts();
        })
        .catch((error) => {
            outputArea.textContent = 'Error: ' + error;
            updateCounts();
        });
    });

    document.getElementById('copy-button').addEventListener('click', function() {
        const range = document.createRange();
        range.selectNodeContents(outputArea);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        document.execCommand('copy');
        selection.removeAllRanges();

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