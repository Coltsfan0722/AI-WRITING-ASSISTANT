from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api.openai.com/v1"  # Replace with your actual API endpoint
API_KEY = "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"  # Replace with your actual API key


@app.route('/')
def home():
    return 'AI Writing Assistant Backend'

@app.route('/api/get-suggestions', methods=['POST'])
def get_suggestions():
    data = request.get_json()
    user_text = data.get('text', '')

    if not user_text.strip():
        return jsonify({'error': 'Empty text'}), 400

    try:
        # Make API call to AI model
        response = requests.post(API_URL, json={'text': user_text}, headers={'Authorization': f'Bearer {API_KEY}'})
        ai_output = response.json()
    except Exception as e:
        return jsonify({'error': 'Failed to get suggestions from AI model'}), 500

    return jsonify(ai_output)

if __name__ == "__main__":
    app.run(debug=False)  # Set debug to False in productionQ