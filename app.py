from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
from flask_cors import CORS
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini AI
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Configure Gemini AI
genai.configure(api_key=api_key)

# Initialize model - using gemini-1.5-flash
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json['message']
        
        # Generate response
        response = model.generate_content(user_message)
        
        if response and response.text:
            return jsonify({
                'status': 'success',
                'response': response.text
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'No response generated'
            }), 500

    except Exception as e:
        print(f"Error: {str(e)}")  # Debug print
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 