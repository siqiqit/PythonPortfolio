#Siqi Tang
#Period 3
#Multiplication Quiz
#Jan 8, 2025

#Initialization

import random

#I utilized three different variables for the three difficulties.

questionNum1 = 0
questionNum2 = 0
questionNum3 = 0

score1 = 0
score2 = 0
score3 = 0

#Functions

#Introduction
def multQuiz():
    difficulty = input("Welcome to the Multiplication Quiz, please choose the difficulty (easy, medium, hard):")

#Easy difficulty
    if difficulty == "easy":
        length = int(input(("Please select how many questions you would like to answer:")))
        for i in range(length):
            global questionNum1
            global score1
            questionNum1 = questionNum1 + 1
            Qone = random.randint(1,5)
            Qtwo = random.randint(1,5)
            print("Question " + str(questionNum1) + " out of " + str(length))
            answer = int(input("What is " + str(Qone) + " * " + str(Qtwo) + "?"))
            if answer == (Qone*Qtwo):
                score1 = score1 + 1
                print("Correct!")
            else:
                print("Incorrect!")
        print("Your total score is " + str(score1) + " out of " + str(length))

#Medium difficulty
    if difficulty == "medium":
        length = int(input(("Please select how many questions you would like to answer:")))
        for i in range(length):
            global questionNum2
            global score2
            questionNum2 = questionNum2 + 1
            Qone = random.randint(1,10)
            Qtwo = random.randint(1,10)
            print("Question " + str(questionNum2) + " out of " + str(length))
            answer = int(input("What is " + str(Qone) + " * " + str(Qtwo) + "?"))
            if answer == (Qone*Qtwo):
                score2 = score2 + 1
                print("Correct!")
            else:
                print("Incorrect!")
        print("Your total score is " + str(score2) + " out of " + str(length))

#Hard difficulty
    if difficulty == "hard":
        length = int(input(("Please select how many questions you would like to answer:")))
        for i in range(length):
            global questionNum3
            global score3
            questionNum3 = questionNum3 + 1
            Qone = random.randint(5,20)
            Qtwo = random.randint(5,20)
            print("Question " + str(questionNum3) + " out of " + str(length))
            answer = int(input("What is " + str(Qone) + " * " + str(Qtwo) + "?"))
            if answer == (Qone*Qtwo):
                score3 = score3 + 1
                print("Correct!")
            else:
                print("Incorrect!")
        print("Your total score is " + str(score3) + " out of " + str(length))

#Main

multQuiz()
