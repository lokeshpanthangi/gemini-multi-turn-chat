# 🤖 Gemini Console Chatbot

A simple console-based chatbot that demonstrates multi-turn conversations using Google's Gemini API.

## 🌟 What This Script Does

This Python script creates a console-based chat application that:

- Initializes a Gemini chat session using the "gemini-1.5-flash" model
- Prompts the user for an initial input and sends it to Gemini
- Prompts for a second input and sends it with preserved context
- Displays the final response from Gemini
- Includes a bonus feature to continue the conversation for additional turns
- Allows customization of the temperature parameter to control response creativity

## 🚀 How to Run

### Prerequisites

- Python 3.7 or higher
- Google Gemini API key

### Setup

1. **Install dependencies**
   ```
   pip install google-generativeai python-dotenv
   ```

2. **Set up your API key**
   - Get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file in the same directory as the script with the following content:
     ```
     GOOGLE_API_KEY=your_actual_api_key_here
     ```

### Running the Application

1. **Execute the script**
   ```
   python gemini_chat.py
   ```

2. **Enter a temperature value**
   - Lower values (e.g., 0.2) for more focused, deterministic responses
   - Higher values (e.g., 0.8) for more creative, varied responses

3. **Follow the prompts**
   - Enter your first message
   - View Gemini's response
   - Enter your second message (follow-up or additional detail)
   - Continue the conversation naturally
   - Type 'bye' when you want to exit

## 🔒 Security Note

The `.env` file contains your API key and should not be shared or committed to version control. A `.gitignore` file has been included to prevent this.

## 🛠️ Error Handling

The script includes error handling for:
- Missing API key
- Invalid temperature values
- API errors during conversation

## 📝 Example Conversation

```
Welcome to the Gemini Console Chatbot!
--------------------------------------
Enter temperature (0.0-1.0, lower for deterministic, higher for creative): 0.7

Chat started! Context will be preserved between messages.
--------------------------------------

Enter your first message: What are the main features of Python?

Gemini: Python has several key features that make it popular among developers:

1. **Easy to Learn and Read**: Python's syntax is clear and intuitive, resembling English.

2. **Interpreted Language**: Code executes line by line, making debugging easier.

3. **Dynamically Typed**: No need to declare variable types explicitly.

4. **Object-Oriented**: Supports object-oriented programming paradigms.

5. **Extensive Standard Library**: Comes with a rich set of modules and packages.

6. **Cross-Platform**: Works on various operating systems (Windows, macOS, Linux).

7. **High-Level Language**: Abstracts complex details from the programmer.

8. **Versatile Applications**: Used in web development, data science, AI, automation, etc.

9. **Strong Community Support**: Large community contributing to libraries and frameworks.

10. **Free and Open Source**: Available for anyone to use and modify.

Enter your second message (follow-up or additional detail): Which of these features make it good for data science specifically?

Gemini: Python excels in data science due to several of its features:

1. **Rich Ecosystem of Libraries**: Python offers specialized libraries like NumPy (for numerical computing), pandas (for data manipulation), Matplotlib and Seaborn (for visualization), scikit-learn (for machine learning), and TensorFlow/PyTorch (for deep learning).

2. **Easy to Learn and Read**: Data scientists can focus on analyzing data rather than complex syntax, making it accessible to those without extensive programming backgrounds.

3. **Interpreted Nature**: Allows for interactive data exploration in notebooks like Jupyter, enabling iterative analysis and immediate visualization of results.

4. **Versatility**: Can handle various aspects of the data science workflow from data cleaning and preprocessing to modeling and deployment.

5. **Integration Capabilities**: Easily interfaces with other languages (like R, SQL, C++) and data sources.

6. **Community Support**: Extensive documentation, tutorials, and forums specifically for data science applications.

7. **Reproducibility**: Tools like virtual environments and notebooks make it easier to share and reproduce analyses.

8. **Scalability**: Can handle everything from small datasets on a laptop to big data processing with frameworks like PySpark.

9. **Visualization Tools**: Rich visualization capabilities make communicating insights straightforward.

10. **Free and Open Source**: Accessibility to everyone, including students, researchers, and organizations of all sizes.

You: Can you recommend some good Python libraries for beginners in data science?

Gemini: Absolutely! For beginners in data science with Python, I recommend starting with these libraries:

1. **pandas**: Essential for data manipulation and analysis. It provides data structures like DataFrames that make working with structured data intuitive.

2. **NumPy**: The foundation for numerical computing in Python. It provides efficient array operations and mathematical functions.

3. **Matplotlib**: The most basic visualization library. It's great for creating standard plots and understanding visualization fundamentals.

4. **Seaborn**: Built on Matplotlib but provides a higher-level interface for creating attractive statistical graphics with less code.

5. **scikit-learn**: Perfect for beginners in machine learning. It has consistent APIs, good documentation, and implements many common algorithms.

6. **Jupyter Notebooks**: Not a library per se, but an interactive environment that's excellent for learning and experimenting with code.

Start with simple projects like:
- Data cleaning and exploration with pandas
- Basic visualizations with Matplotlib/Seaborn
- Simple predictive models with scikit-learn

As you grow more comfortable, you can explore more specialized libraries like TensorFlow or PyTorch for deep learning, or Plotly for interactive visualizations.

You: bye

Conversation ended. Thank you for using Gemini Console Chatbot!
```
