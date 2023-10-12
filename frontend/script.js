document.addEventListener("DOMContentLoaded", function() {
    const submitBtn = document.getElementById('submitBtn');
    const userInput = document.getElementById('userInput');
    const suggestions = document.getElementById('suggestions');

    submitBtn.addEventListener('click', function() {
        const userText = userInput.value;
        if(userText.trim()) {
            // Make API call to backend
            fetch('/api/get-suggestions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: userText })
            })
            .then(response => response.json())
            .then(data => {
                // Update UI with AI's response
                suggestions.innerText = data.suggestions;
            })
            .catch(error => {
                console.error('Error:', error);
                suggestions.innerText = 'Sorry, something went wrong. Please try again later.';
            });
        } else {
            alert('Please enter some text!');
        }
    });
});
