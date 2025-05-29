#!/usr/bin/env python3
"""
Gemini Console Chatbot
A simple console-based chatbot using Google's Gemini API.
"""

import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

def setup_gemini_api():
    """Configure the Gemini API with the API key from .env file."""
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the API key from environment variables
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env file.")
        print("Please create a .env file with your Gemini API key.")
        sys.exit(1)
    
    # Configure the Gemini API with the API key
    genai.configure(api_key=api_key)

def get_valid_temperature():
    """Get a valid temperature value from the user."""
    while True:
        try:
            temp = float(input("Enter temperature (0.0-1.0, lower for deterministic, higher for creative): "))
            if 0.0 <= temp <= 1.0:
                return temp
            else:
                print("Temperature must be between 0.0 and 1.0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0.0 and 1.0.")

def create_chat_session(temperature):
    """Create a new chat session with the specified temperature."""
    # Initialize the Gemini model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"temperature": temperature}
    )
    
    # Start a new chat session
    return model.start_chat(history=[])

def main():
    """Main function to run the Gemini chatbot with exactly two turns by default."""
    print("Welcome to the Gemini Console Chatbot!")
    print("--------------------------------------")
    
    # Setup the Gemini API
    setup_gemini_api()
    
    # Get temperature from user
    temperature = get_valid_temperature()
    
    # Create a chat session
    chat = create_chat_session(temperature)
    
    print("\nChat started! Context will be preserved between messages.")
    print("--------------------------------------")
    
    # First turn
    first_input = input("\nEnter your first message: ")
    
    try:
        # Send first input to Gemini and get response
        first_response = chat.send_message(first_input)
        print(f"\nGemini: {first_response.text}")
        
        # Second turn
        second_input = input("\nEnter your second message (follow-up or additional detail): ")
        
        # Send second input to Gemini (context is automatically preserved)
        second_response = chat.send_message(second_input)
        print(f"\nGemini: {second_response.text}")
        
        # Continue conversation by default until user types 'bye'
        while True:
            next_input = input("\nYou: ")
            
            # Exit if user types 'bye'
            if next_input.lower() == "bye":
                print("\nConversation ended. Thank you for using Gemini Console Chatbot!")
                break
                
            # Otherwise continue the conversation
            response = chat.send_message(next_input)
            print(f"\nGemini: {response.text}")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("Please try again.")

if __name__ == "__main__":
    main()
