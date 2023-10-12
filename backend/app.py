from flask import Flask, request, jsonify
import requests  # To make API requests to the AI model

app = Flask(__name__)

# Replace with your actual API endpoint and key
AI_MODEL_ENDPOINT = "https://api.openai.com/v1"
AI_MODEL_API_KEY = "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"

@app.route('/')
def home():
    return 'AI Writing Assistant Backend'

@app.route('/api/get-suggestions', methods=['POST'])
def get_suggestions():
    # Get user text from frontend
    data = request.get_json()
    user_text = data.get('text', '')
    
    # Validate user_text
    if not user_text.strip():
        return jsonify({'error': 'Empty text'}), 400
    
    # Make API call to AI model
    try:
        # Replace with actual API call logic
        # response = requests.post(AI_MODEL_ENDPOINT, json={'text': user_text}, headers={'Authorization': f'Bearer {AI_MODEL_API_KEY}'})
        # ai_output = response.json()
        ai_output = {"suggestions": "This is a mock suggestion"}  # Mock response
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Failed to get suggestions from AI model'}), 500
    
    # Send AI output to frontend
    return jsonify(ai_output)

if __name__ == "__main__":
    app.run(debug=True) # Set debug to False in production
    