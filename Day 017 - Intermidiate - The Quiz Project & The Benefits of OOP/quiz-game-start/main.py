from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for quest in question_data:
    quest_text = quest["question"] 
    quest_answer = quest["correct_answer"]
    new_quest = Question(quest_text, quest_answer)
    # Make quest_text, quest_answer, and new_quest for easier to reference and readable.
    question_bank.append(new_quest)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")