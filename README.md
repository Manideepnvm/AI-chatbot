# AI Chatbot using Mistral AI

A simple web-based chatbot that uses the Mistral AI API to generate responses.

## Features

- Clean and modern web interface
- Real-time chat interactions
- Powered by Mistral AI's language model
- Responsive design that works on desktop and mobile

## Prerequisites

- Python 3.7 or higher
- Mistral AI API key (get it from [Mistral AI Platform](https://mistral.ai/))

## Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Mistral AI API key:
```
MISTRAL_API_KEY=your_mistral_api_key_here
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Type your message in the input field at the bottom of the chat interface
2. Press Enter or click the Send button to send your message
3. Wait for the AI to respond
4. Continue the conversation as needed

## Note

Make sure to keep your Mistral AI API key secure and never commit it to version control. The `.env` file is included in `.gitignore` for this reason. 