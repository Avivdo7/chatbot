# app.py
from flask import Flask, request, jsonify, render_template
from dal.database import get_db
from dal.repositories import QuestionRepository
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

app = Flask(__name__)

# OpenAI setup
client = InferenceClient(
    api_key=os.environ.get("API_KEY"),
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # OpenAI API call
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            max_tokens=256

        )

        answer = response.choices[0].message.content

    except Exception as e:
        answer = f"An error occurred: {str(e)}"

    # Save to database
    with get_db() as db:
        repo = QuestionRepository(db)
        new_question = repo.create_question(question, answer)

    return jsonify({"question": question, "answer": answer})


if __name__ == '__main__':
    app.run(debug=True)