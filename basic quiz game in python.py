# basic quiz game in python
class Questions:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    
    def display_question(self,question):
        print(question.text)
        for index,choice in enumerate(question.choices):
            print(f"{index + 1}. {choice}")
        answer = int(input("Enter You answer (1-4): "))
        self.check_answer(question,answer)

    def check_answer(self,question,answer):
        if answer == question.answer:
            print("Correct Answer!")
            self.score += 1
        else:
            print("Wrong answer") 
    
    def play_game(self):
        for question in self.questions:
            self.display_question(question)
        print(f"Quize Completed. Your Score is : {self.score}/{len(self.questions)} ") 

questions = [
    Questions("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], 2),
    Questions("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], 1),
    Questions("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"], 1),
    Questions("What is the largest mammal in the world?", ["Elephant", "Blue whale", "Giraffe", "Hippopotamus"], 2),
] 

#create Quiz game
game = QuizGame(questions)

#play Game
game.play_game()

