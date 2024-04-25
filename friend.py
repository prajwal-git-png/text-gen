from flask import Flask, render_template, request
import google.generativeai as genai


app = Flask(__name__)

genai.configure(api_key="AIzaSyAzwzm4RVxgbfaK8CCwb8zT98pM4Xjgipk")

instruction = (
    "Imagine you're chatting with a knowledgeable friend who's an expert in various fields. When you ask them a question, they'll provide proper guidance just like a friend would, not just as an AI. Feel free to ask about anything, and they'll offer friendly advice and insights!"
)

model = genai.GenerativeModel(
    "models/gemini-1.5-pro-latest",
    system_instruction=instruction
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    if user_input.lower() == "exit":
        response = "Goodbye!"
    else:
        response = model.generate_content(user_input).text
    return response

if __name__ == '__main__':
    app.run(debug=True)
