🤖 Gemini Dual-Mode Assistant
This project is a versatile AI assistant that operates in a dual-mode: a text-based chat interface and a speech-to-text powered voice assistant. It's built using Google's Gemini AI and Streamlit, providing a powerful, multilingual conversational experience.

✨ Features
Dual-Mode Interaction: Seamlessly switch between typing your queries and speaking to the assistant using a microphone.

Multilingual Support: Communicate with the assistant in multiple languages for a more inclusive user experience.

Gemini Integration: Powered by Google's Gemini large language model for natural, context-aware, and intelligent responses.

Conversational AI: Maintains chat history to provide a fluid and coherent conversation.

Simple UI: A clean and intuitive interface built with Streamlit for a great user experience.

💻 Technologies Used
Python: The core programming language.

Streamlit: For creating the interactive web application.

Google Gemini API: The backbone of the AI functionality.

Speech Recognition Libraries: For converting spoken language to text.

gTTS (Google Text-to-Speech): For converting text responses to speech (if applicable).

python-dotenv: To securely manage API keys and environment variables.

🚀 Installation & Setup
Clone the repository:

git clone [https://github.com/Pranshu51/GeminiDual-Mode-Assistant.git](https://github.com/Pranshu51/GeminiDual-Mode-Assistant.git)
cd GeminiDual-Mode-Assistant

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

Windows:

.\venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

(You will need to create a requirements.txt file from your project's dependencies, e.g., pip freeze > requirements.txt).

Set up your Google API Key:

Create a .env file in the root directory of your project.

Add your Google API key to the file in the following format:

GOOGLE_API_KEY="your_api_key_here"

▶️ Usage
Run the Streamlit app:

streamlit run app.py

Your browser will open automatically.

Choose your input mode (text or voice) and start interacting with the Gemini assistant!
