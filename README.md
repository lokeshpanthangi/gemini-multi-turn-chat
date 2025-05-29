# Gemini Console Chatbot

A simple console-based chatbot using Google's Gemini API.

## Features

- Uses Google's "gemini-1.5-flash" model
- Securely loads API key from environment variables
- Customizable temperature setting for response creativity
- Maintains chat history between turns
- Simple console interface

## Setup

1. **Clone the repository**

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   - Get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Copy the `.env` file and replace `your_key_here` with your actual API key:
     ```
     GOOGLE_API_KEY=your_actual_api_key_here
     ```

## Usage

1. **Run the script**
   ```
   python gemini_chat.py
   ```

2. **Enter a temperature value**
   - Lower values (e.g., 0.3) for more deterministic responses
   - Higher values (e.g., 0.9) for more creative responses

3. **Start chatting**
   - Type your messages and press Enter
   - Type 'bye', 'exit', or 'quit' to end the conversation

## Security Note

The `.env` file contains your API key and should not be shared or committed to version control. A `.gitignore` file has been included to prevent this.

## Error Handling

The script includes basic error handling for:
- Missing API key
- Invalid temperature values
- API errors during conversation
