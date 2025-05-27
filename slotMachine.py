#Siqi Tang
#Period 3
#Slot Machine
#January 28, 2025


#Init

import random
import time
symbols = ["❀", "✿", "❁", "✾", "7" ]
credit = 200
again = "q"

#functions

def slot_machine():
    global symbols
    global credit
    global again
    print("""Welcome to the Slot Machine! To begin, you will have 200 credits.

✧ Each spin will cost 10 credits
✧ Each twin (two of the same symbols) will earn you 5 credits
✧ Each 7 twins will earn you 20 credits
✧ Each triplet (three of the same symbols) will earn you 50 credits
✧ Each jackpot (three 7s) will earn you 400 credits
✧ Anything else will earn you nothing

 You may choose to end the game and keep the rest of your credits, but when you run out of credits, you may not spin anymore and the game is over. Good luck!""")

    while True:
        if credit < 10:
            print("You have insufficient credits to spin, thank you for playing the Slot Machine.")
            break

        selection = input("Please select an option: spin (1) or quit (2)")
        if selection == "1":
            credit = credit - 10
            print("Spinning...")
            time.sleep(1)

            one = random.choice(symbols)
            two = random.choice(symbols)
            three = random.choice(symbols)


#triplets
            if one == "❀" and two == "❀" and three == "❀":
                credit = credit + 50
                print("congrats, your combo is  [❀ ❀ ❀], you win! You now have " + str(credit) + " credits!")

            elif one == "✿" and two == "✿" and three == "✿":
                credit = credit + 50
                print("congrats, your combo is  [✿ ✿ ✿], you win! You now have " + str(credit) + " credits!")

            elif one == "❁" and two == "❁" and three == "❁":
                credit = credit + 50
                print("congrats, your combo is  [❁ ❁ ❁], you win! You now have " + str(credit) + " credits!")

            elif one == "✾" and two == "✾" and three == "✾":
                credit = credit + 50
                print("congrats, your combo is  [✾ ✾ ✾], you win! You now have " + str(credit) + " credits!")

#twins
            elif one != "❀" and two == "❀" and three == "❀":
                credit = credit + 5
                print("congrats, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")

            elif one == "❀" and two != "❀" and three == "❀":
                credit = credit + 5
                print("congrats, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")

            elif one == "❀" and two == "❀" and three != "❀":
                credit = credit + 5
                print("congrats, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")


            elif one != "✿" and two == "✿" and three == "✿":
                credit = credit + 5
                print("congrats, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")

            elif one == "✿" and two != "✿" and three == "✿":
                credit = credit + 5
                print("congrats, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")

            elif one == "✿" and two == "✿" and three != "✿":
                credit = credit + 5
                print("congrats, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")


            elif one != "❁" and two == "❁" and three == "❁":
                credit = credit + 5
                print("congrats, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")

            elif one == "❁" and two != "❁" and three == "❁":
                credit = credit + 5
                print("congrats, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")

            elif one == "❁" and two == "❁" and three != "❁":
                credit = credit + 5
                print("congrats, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")


            elif one != "✾" and two == "✾" and three == "✾":
                credit = credit + 5
                print("congrats, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")

            elif one == "✾" and two != "✾" and three == "✾":
                credit = credit + 5
                print("congrats, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")

            elif one == "✾" and two == "✾" and three != "✾":
                credit = credit + 5
                print("congrats, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")


            elif one != "7" and two == "7" and three == "7":
                credit = credit + 20
                print("wow, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")

            elif one == "7" and two != "7" and three == "7":
                credit = credit + 20
                print("wow, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")

            elif one == "7" and two == "7" and three != "7":
                credit = credit + 20
                print("wow, your combo was [ " + one + " " + two + " " + three + " ]. You now have " + str(credit) + " credits!")


#jackpot
            elif one == "7" and two == "7" and three == "7":
                credit = credit + 400
                print("No way you lucky soul, you pulled a [ 7 7 7 ]!!! Jackpot! You now have " + str(credit) + " credits!")

            else:
                print("RIP, your combo was [ " + one + " " + two + " " + three + " ]. Better luck next time! You lose... You now have " + str(credit) + " credits!")


        elif selection == "2":
            print("Thank you for playing the Slot Machine. " + str(credit) + " credits have been redeemed and will be sent out shortly." )
            break

        else:
            print("ERROR: Please enter either 1 or 2.")



#main

slot_machine()
