#Siqi Tang
#Period 3
#Story Game
#January 15, 2024

#Initialization
import random

#Functions

def youtuber():

    #Introduction
    print("Greetings player, welcome to YouTuber Simulator! In this game, you will model the path of a beginner YouTuber, and your decisions will impact whether you rise to the top or fall in the YouTubing world.")
    channel_name = input("To begin, please enter a YouTube channel name:")
    print("Wow, " + channel_name + "! What a fabulous choice!")

    channel_type = input("""Now, YouTubers range a lot when it comes to their content, and you must choose the type of content you want to put out there for your fans. Please select the one that feels most right to you! (1-2):
1. Gaming content creator
2. Informational content creator""")

    if int(channel_type) == 1:
        reputation = 100
        subscribers = 0

#Instructions
        print("Cool! You've chosen to pursue a gaming channel! Lets go over some basics.")
        print("You have two things to watch out for when you make decisions on uploading videos, and they are your reputation points and subscriber count. The decisions you make along the way will reflect these two categories and will determine the ending you get as a YouTuber, so make wise decisions.")
        print("After each video upload, the system will give you an overview of your stats for 3 videos.")
        print("Without further ado, lets get started!")

#Game

#scene 1
        scenario_1 = input("""A lot of youtubers have recently been playing this game called Phasmophobia. Would you hop on the bandwagon or choose to play an underappreciated game instead? (1-2)
1. Play Phasmophobia
2. Play underappreciated game""")
        if int(scenario_1) == 1:
            reputation = reputation - random.randint(10,15)
            subscribers = subscribers + random.randint(6500,8500)
            print("You have decided to play Phasmophobia. There is a steady stream of subscribers coming in.")
            print(channel_name + "'s reputation is now " + str(reputation) + " and its subscriber count is now "+ str(subscribers) + ".")
        if int(scenario_1) == 2:
            subscribers = subscribers + random.randint(3500,5000)
            print("You have decided to play the underappreciated game. Some people love that you shone light on such a good game.")
            print(channel_name + "'s reputation is now " + str(reputation) + " and its subscriber count is now "+ str(subscribers) + ".")

#scene 2
        scenario_2 = input(""""You got an offer to collab with another gaming youTuber who has a large fanbase, but is notorious in the gaming industry. Will you accept? (1-2)
1. Accept the collaboration
2. Kindly decline""")
        if int(scenario_2) == 1:
            reputation = reputation - random.randint(15,30)
            subscribers = subscribers + random.randint(7500,9500)
            print("You have accepted the collab. It went smoothly but some of your fans now have an iffy feeling about you.")
            print(channel_name + "'s reputation is now " + str(reputation) + " and its subscriber count is now "+ str(subscribers) + ".")
        if int(scenario_2) == 2:
            subscribers = subscribers + random.randint(1000,1500)
            print("You have declined the offer, but you still feel like you missed out on an opportunity.")
            print(channel_name + "'s reputation is now " + str(reputation) + " and its subscriber count is now "+ str(subscribers) + ".")

#scene 3
        scenario_3 = input("""You have been roped into a controversy with another gaming YouTuber during one of your gaming collabs. Will you make a genuine apology video or will you exaggerate it for the views? (1-2)"
1. Make genuine apology video
2. Exaggerate it""")
        if int(scenario_3) == 1:
            reputation = reputation - random.randint(0,10)
            subscribers = subscribers + random.randint(2500,4000)
            print("You have decided to make a genuine apology video. Many of your fans forgive you and are willing to take another chance on you.")
            print(channel_name + "'s reputation is now " + str(reputation) + " and its subscriber count is now "+ str(subscribers) + ".")
        if int(scenario_3) == 2:
            reputation = reputation - random.randint(20,35)
            subscribers = subscribers + random.randint(3500,7000)
            print("You have decided to exaggerate your apology video. You have gained a lot of traction for it but now some of your fans despise you.")
            print(channel_name + "'s reputation is now " + str(reputation) + " and its subscriber count is now "+ str(subscribers) + ".")

#conclusion
        if reputation >= 90 and subscribers <= 10000:
                print("You have been a gaming YouTuber whom everyone likes and although you have a smaller subscriber count, that doesn't mean you don't have potential for the future!")
        elif reputation >= 50 and subscribers <= 15000:
                print("Hey you're doing pretty good on your gaming career and you have an ok subscriber count! Good luck in the future!")
        else:
                print("A lot of people might hate you in the gaming communities but at least that cash is flowing in.")


    if channel_type == 2:
        reputation = 100
        subscribers = 0

#Instructions
        print("Cool! You've chosen to pursue a inscructions channel! Lets go over some basics.")
        print("You have two things to watch out for when you make decisions on uploading videos, and they are your reputation points and subscriber count. The decisions you make along the way will reflect these two categories and will determine the ending you get as a YouTuber, so make wise decisions.")
        print("After each video upload, the system will give you an overview of your stats for 3 videos.")
        print("Without further ado, lets get started!")

#Game

#scene 1
        scenario_1 = input("""A lot of people have been requesting a math video but you were planning an english one, which in general, more people usually watch. Which one would you go for? (1-2)
1. Make math video
2. Make english video""")
        if int(scenario_1) == 1:
            subscribers = subscribers + random.randint(3500,4500)
            print("You have decided to make a math video as per request of the people. They now learn to rely on you for help.")
            print(channel_name + "'s reputation is now " + str(reputation) + " and its subscriber count is now "+ str(subscribers) + ".")
        if int(scenario_1) == 2:
            reputation = reputation - random.randint(5,20)
            subscribers = subscribers + random.randint(5000,6500)
            print("You have decided to continue making your english video, people are watching it but some of your fans began to lose hope")
            print(channel_name + "'s reputation is now " + str(reputation) + " and its subscriber count is now "+ str(subscribers) + ".")

#scene 2
        scenario_2 = input(""""You want to go on vacation but its finals time right now. Do you delay your vacation to help students in need? (1-2)
1. Delay
2. Go on vacation""")
        if int(scenario_2) == 1:
            subscribers = subscribers + random.randint(4000,6000)
            print("You have decided to delay your vacation and upload videos. Students are very happy.")
            print(channel_name + "'s reputation is now " + str(reputation) + " and its subscriber count is now "+ str(subscribers) + ".")
        if int(scenario_2) == 2:
            reputation = reputation - random.randint(15,30)
            subscribers = subscribers + random.randint(4000,6000)
            print("You have decided to go on your vacation anyways, students are suffering.")
            print(channel_name + "'s reputation is now " + str(reputation) + " and its subscriber count is now "+ str(subscribers) + ".")

#scene 3
        scenario_3 = input("""You accidentally explained something wrong in one of your videos, do you quickly make another video to cover it or let it fester for traction? (1-2)"
1. Make a correct video and replace it
2. Let people laugh at it""")
        if int(scenario_3) == 1:
            reputation = reputation - random.randint(0,5)
            subscribers = subscribers + random.randint(3500,4500)
            print("You quickly made a replacement video and apologized for the mistake. Your fans are very happy.")
            print(channel_name + "'s reputation is now " + str(reputation) + " and its subscriber count is now "+ str(subscribers) + ".")
        if int(scenario_3) == 2:
            reputation = reputation - random.randint(20,35)
            subscribers = subscribers + random.randint(5000,7500)
            print("You have decided to keep it. Now people come to your channel exclusively to laugh at your mistake.")
            print(channel_name + "'s reputation is now " + str(reputation) + " and its subscriber count is now "+ str(subscribers) + ".")

#conclusion
        if reputation >= 90 and subscribers <= 15000:
                print("Your informative videos have been very helpful to students and they all like you. Even though your channel is small, you have somewhere to begin.")
        elif reputation >= 50 and subscribers <= 20000:
                print("Though you've made some questionable decisions, you have been on a good streak so far with subs. Continue the work and you'll get somewhere soon.")
        else:
                print("Maybe your videos aren't the most helpful. At least you got money in your pocket.")

#Main
youtuber()
