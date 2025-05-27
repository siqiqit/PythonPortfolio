#Siqi Tang
#Period 3
#CREATE Task: Emoticonne

#initialize
import random #To randomly generate the emoticon parts that build the whole
import time #To make the users wait a little before receiving their emoticon

#genLists #The list that will be used for general emoticon parts like the base and the hands
baseFront = ["( ", "[ ", "< ", "꒰ "]
baseBack = [" )", " ]", " >", " ꒱"]
leftHand = ["乁", "＼","∩", "ᕙ"]
rightHand = ["ㄏ", "/","∩", "ᕗ"]

#happyLists #The list for happy emoticon parts
happyEye1= ["^ ", "≧ ", "˘ ", "• "]
happyEye2= [" ^", " ≦", " ˘", " •"]
happyMouth= ["▽", "v", "ᴗ", "w"]
happyAcc= [" .☀︎ ݁˖", " ⊹ ࣪ ˖", " ⋆⭒˚.⋆", " ˙☼☀︎"]

#gloomyLists #The list for gloomy emoticon parts
gloomyEye1= ["T ", "╥ ", "´ ", "ᴗ "]
gloomyEye2= [" T", " ╥", " `", " ᴗ"]
gloomyMouth= ["□", "Д", "╭╮", "⌓"]
gloomyAcc= [". ݁˖☔︎︎", "⋆.࿔⛈༄", "⋆.°·☁︎", " ⛆✧₊⁺"]

#loveLists #The list for loving emoticon parts
loveEye1= ["♥ ", "♡ ", "ღ ", "ꈍ "]
loveEye2= [" ♥", " ♡", " ღ", " ꈍ"]
loveMouth= ["∇", "ᴗ", "o","ᗜ"]
loveAcc= ["---♡", "♡⸝⸝", "°˖➴<3", "༄.°♥"]

#history #A blank list to readily accept newly generated emoticons
history= []

#dictionary #This is to designate certain moods to be put in as the parameter of the function that randomly generates emoticon parts, makes it more organized
emoticon_selection ={
    "happy": { #If "happy" is called, it would apply these definitions based on emoticon part
        "leftEye": happyEye1,
        "rightEye": happyEye2,
        "mouth": happyMouth,
        "acc": happyAcc
        },
    "gloomy": { #If "gloomy" is called, it would apply these definitions based on emoticon part
        "leftEye": gloomyEye1,
        "rightEye": gloomyEye2,
        "mouth": gloomyMouth,
        "acc": gloomyAcc
        },
    "loving": { #If "loving" is called, it would apply these definitions based on emoticon part
        "leftEye": loveEye1,
        "rightEye": loveEye2,
        "mouth": loveMouth,
        "acc": loveAcc
        }
    }

#updatedList #Initial variables made so that they can be globalled and edited/used in both functions
leftEye = "x"
rightEye = "x"
mouth = "x"
acc = "x"


#functions

def emotiMood(mood): #The function that is used to randomly generate special emoticon parts according to the mood parameter that will be determined in the function it will be used in.

    global leftEye
    global rightEye
    global mouth
    global acc

    eyeNum = random.randint(0,3)
    leftEye= emoticon_selection[mood]["leftEye"][eyeNum]
    rightEye = emoticon_selection[mood]["rightEye"][eyeNum]
    mouth = emoticon_selection[mood]["mouth"][random.randint(0,3)]
    acc = emoticon_selection[mood]["acc"][random.randint(0,3)]
        #Using the dictionary I made above to specially select matching parts according to the mood.

    print("Loading your emoticon...")
    time.sleep(3) #Make them wait a little for the surprise emoticon.


def Emoticonne(name): #The main function, name parameter for user friendly and favor points

    global leftEye
    global rightEye
    global mouth
    global acc

    print("Welcome to Emoticonne, " +name+ "! Emoticonne is an emoticon generator that allows users to generate random emoticons based on your current mood!") #Introduction
    while True:
        choice = input("Feel free to explore our general catalog, " +name+ """! Please select what you would like to do (1-3):
        1. Generate a random emoticon
        2. Check emoticon history
        3. Quit""") #The general overarching catalog that users will be brought back to

        if choice == "1":
            while True:
                mood = input(name+ """, Welcome to the Emoticonne catalog. Here, we have a variety of emotions to select from to generate your own special emoticon! To begin, please select an emotion (1-3) or go back to the general catalog(4):
        1. Happy
        2. Gloomy
        3. Loving
        4. Go back to Catalog""") #The specific catalog for generating emoticons

            #Standard parts that will be randomly generated for every emoticon, regardless of mood.
                baseNum = random.randint(0,3)
                base1 = baseFront[baseNum]
                base2 = baseBack[baseNum]
                LftHand = leftHand[random.randint(0,3)]
                RgtHand = rightHand[random.randint(0,3)]

                if mood == "1":
                    print("Glad to hear that you're in a delightful mood today!")
                    emotiMood("happy") #Randomly generating happy emoticon parts
                    print("A happy emoticon for your sunny self, " + name + "!")

                if mood == "2":
                    print("Awe... we all have those days, don't we?")
                    emotiMood("gloomy") #Randomly generating gloomy emoticon parts
                    print("We hope you feel better soon, " + name + "!")

                if mood == "3":
                    print("Ouh! Glad you're sharing this love with others too!")
                    emotiMood("loving") #Randomly generating loving emoticon parts
                    print("We hope you love this emoticon too, " + name + "!")

                if mood == "4":
                    print("Alright! Taking you back to the catalog")
                    break #Back to the bigger while loop

                emoticon = str(LftHand + base1 + leftEye + mouth + rightEye + base2 + RgtHand + acc)

                history.append(emoticon) #Appending the newly generated emoticon to the history list
                print(emoticon)
                print("----------------------------------------------------------------------------------------") #Break border to make things more organized

        if choice == "2":
            print("Alright! Here is your emoticon history so far:")
            print(history) #Calling the history list of past generated emoticons

        if choice == "3":
            print("Thank you for using Emoticonne "+ name + "! We hope to see you again soon!")
            break #Stopping the whole program


#main

Emoticonne("Mimo") #Calling the function with user name
