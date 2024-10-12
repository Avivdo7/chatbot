from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String(500), nullable=False)
    answer = Column(Text, nullable=False)

    def __repr__(self):
        return f"<Question(id={self.id}, question='{self.question}')>"