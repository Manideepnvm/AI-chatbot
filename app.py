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

# Updated system prompt for better code explanations
SYSTEM_PROMPT = """
You are a friendly coding teacher. When explaining code:

1. Start with a simple introduction
2. Break down the code into small, digestible parts
3. Explain each line in simple terms
4. Use a step-by-step format
5. Include examples of output
6. Add helpful notes and tips
7. Use this exact format:

Title: [Program Name]

What it does:
• Simple explanation of the program's purpose

Code:
[syntax-highlighted code block]

Let's understand each part:

1. [First concept]:
   • What it does
   • Why we use it
   • Example of usage

2. [Second concept]:
   • Explanation
   • Purpose
   • Example

How to Run:
1. Step one
2. Step two
3. Step three

Expected Output:
[Show what the user will see]

Tips:
• Helpful tip 1
• Helpful tip 2

Common Errors:
• Error 1: How to fix it
• Error 2: How to fix it
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json['message']
        
        # Add context for better responses
        prompt = f"{SYSTEM_PROMPT}\nProvide accurate, factual information for this query: {user_message}"
        response = model.generate_content(prompt)
        
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
        print(f"Error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 