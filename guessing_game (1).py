#Siqi Tang
#Period 3
#Guessing Game
#November 11, 2024

#Initialization
import random #For randomizing numbers
import sys #For shutting down program at the end


#Function

#Introduction
def guess_this():
    ans=input("Hello user, welcome to The Guessing Game! Please select a difficulty level: easy, medium, or hard.")


#Easy route
    if ans == "easy":
        rando= random.randint(0, 10)
        win = 0
        print("Welcome to difficulty: easy of The Guessing Game! You will have three chances to guess a number between 0-10 to win!")
        for i in range(3):
            number=int(input("Guess the number here:"))
            if number == rando:
                print("Omg, you actually got it???")
                win = 1
                break
            else:
                print("Nope, try again!")
                win = 0
        if win == 0:
            print("Aww man, the mystery number was "+ str(rando) + ", better luck next time!")
        if win == 1:
            print("Congrats! The mystery number was "+ str(rando) + ", you win!")

#Medium route
    if ans == "medium":
        rando= random.randint(0, 20)
        win = 0
        print("Welcome to difficulty: medium of The Guessing Game! You will have three chances to guess a number between 0-20 to win!")
        for i in range(3):
            number=int(input("Guess the number here:"))
            if number == rando:
                print("Omg, you actually got it???")
                win = 1
                break
            else:
                print("Nope, try again!")
                win = 0
        if win == 0:
            print("Aww man, the mystery number was "+ str(rando) + ", better luck next time!")
        if win == 1:
            print("Congrats! The mystery number was "+ str(rando) + ", you win!")

#Hard route
    if ans == "hard":
        rando= random.randint(0, 100)
        win = 0
        print("Welcome to difficulty: hard of The Guessing Game! You will have three chances to guess a number between 0-100 to win!")
        for i in range(3):
            number=int(input("Guess the number here:"))
            if number == rando:
                print("Omg, you actually got it???")
                win == 1
                break
            else:
                print("Nope, try again!")
                win == 0
        if win == 0:
            print("Aww man, the mystery number was "+ str(rando) + ", better luck next time!")
        if win == 1:
            print("Congrats! The mystery number was "+ str(rando) + ", you win!")


def whole_game(): #This function is here so that I can give the option of playing again
    guess_this()
    ans=input("Would you like to play again? (yes, no)")
    if ans == "yes":
        whole_game()
    if ans == "no":
        print("Thank you for playing The Guessing Game!")
        sys.exit() #Shutting down the program


#Main

whole_game()

