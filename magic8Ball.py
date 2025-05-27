#Siqi Tang
#Period 3
#Magic 8ball
#January 24, 2025

#init

import random
import time
responses = ["No", "Not likely", "It seems out of reach", "I don't think so", "It is not possible", "Maybe", "Perhaps it could", "There is a possibility", "Probably", "There is a chance", "Certainly", "Without a doubt", "Yes", "I believe so", "You can count on it", "If you try hard enough!", "Not with that attitude", "I think you can do it!", "Better not tell you now", "Reply hazy, try again", "Doesn't look so bright", "Maybe you're a little delusional", "Uh oh", "Its looking good for you", "Ooooh yes, I see this happening!", "Don't worry, it'll happen" ]


#functions

def eightball():
    global responses
    while True:
            question = input("Welcome to the Magic 8-Ball! Ask any question and fate will decide whether or not it is possible:")
            number = random.randint(0,14)

            if question.endswith("?"):
                print("shake...")
                time.sleep(2)
                print("shake...")
                time.sleep(2)
                print("shake...")
                time.sleep(2)

                print(responses[number])
                playAgain = input("Play again? (yes, no)")
                if playAgain == "no":
                    print("Thanks for playing Magic 8-Ball!")
                    break

            else:
                print("Please ask a question with a question mark at the end.")



#main
eightball()
