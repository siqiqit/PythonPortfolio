#Siqi Tang
#Period 3
#Name Generator
#October 17, 2024


#Introduction
print("Have you ever wondered what is your spirit flower?")
print("Answer the questions below to find out!")
ans= input("Is your style more feminine or masculine?")


#Feminine route
if ans== "feminine":
    ans= input("Is your clothing aesthetic more cute or elegant?")

    #Cute route
    if ans== "cute":
        ans= input("Do you prefer the color white or red?")
        if ans== "white":
            print("Your spirit flower is Lily of the Valley!")
        if ans== "red":
            print("Your spirit flower is English Rose!")

    #Elegant route
    if ans=="elegant":
        ans= input("Do you prefer the color pink or purple?")
        if ans== "pink":
            print("Your spirit flower is Peony!")
        if ans== "purple":
            print("Your spirit flower is Hyacinth!")

#Masculine route
if ans== "masculine":
    ans= input("Is your clothing aesthetic more formal or casual?")

    #Formal route
    if ans== "formal":
        ans= input("Do you prefer the color green or blue?")
        if ans== "green":
            print("Your spirit flower is Viridiflora Tulip!")
        if ans== "blue":
            print("Your spirit flower is Hydrangea!")

    #Casual route
    if ans=="casual":
        ans= input("Do you prefer the color yellow or orange?")
        if ans== "yellow":
            print("Your spirit flower is Sunflower!")
        if ans== "orange":
            print("Your spirit flower is Marigold!")
