from sqlalchemy.orm import Session
from .models import Question

class QuestionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_question(self, question: str, answer: str) -> Question:
        db_question = Question(question=question, answer=answer)
        self.db.add(db_question)
        self.db.commit()
        self.db.refresh(db_question)
        return db_question

    def get_question_by_id(self, question_id: int) -> Question:
        return self.db.query(Question).filter(Question.id == question_id).first()

    def get_all_questions(self):
        return self.db.query(Question).all()

    def update_question(self, question_id: int, new_question: str, new_answer: str) -> Question:
        db_question = self.get_question_by_id(question_id)
        if db_question:
            db_question.question = new_question
            db_question.answer = new_answer
            self.db.commit()
            self.db.refresh(db_question)
        return db_question

    def delete_question(self, question_id: int) -> bool:
        db_question = self.get_question_by_id(question_id)
        if db_question:
            self.db.delete(db_question)
            self.db.commit()
            return True
        return False