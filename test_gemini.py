import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini AI
api_key = os.getenv("GEMINI_API_KEY")
print(f"API key found: {'Yes' if api_key else 'No'}")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

try:
    response = model.generate_content("Hello, are you working?")
    print("Response:", response.text)
except Exception as e:
    print("Error:", str(e)) 