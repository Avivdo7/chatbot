# app.py
from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

app = Flask(__name__)

# OpenAI setup
client = InferenceClient(
    api_key=os.environ.get("API_KEY"),
)

# Database setup
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/dbname')
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String(500), nullable=False)
    answer = Column(Text, nullable=False)


Base.metadata.create_all(engine)

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
    session = Session()
    new_question = Question(question=question, answer=answer)
    session.add(new_question)
    session.commit()
    session.close()

    return jsonify({"question": question, "answer": answer})


if __name__ == '__main__':
    app.run(debug=True)