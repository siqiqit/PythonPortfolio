#Siqi Tang
#Period 3
#Images
#February 24, 2025


#Initialize
from PIL import Image
import requests
from io import BytesIO
import random
import time

puplist = ["https://tinyurl.com/efdgyhtd", #samoyed. Image credit: Unsplash. Rafael Garcin. https://images.unsplash.com/photo-1625334955193-c7c208aba883?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D. July 3, 2021. Free to use under Unsplash license
           "https://tinyurl.com/334rbgfds", #goldenretriever. Image Credit: Unsplash. Justin Aikin. https://images.unsplash.com/photo-1523480717984-24cba35ae1ef?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D. April 11, 2018. Free to use under Unsplash license
           "https://tinyurl.com/2erfbredws", #pomeranian. Image Credit: Unsplash. Alvan Nee. https://images.unsplash.com/photo-1558236714-d1a6333fce68?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D. May 18, 2019. Free to use under Unsplash license
           "https://tinyurl.com/344kujhnbfdf", #australianshepherd. Image credit: Unsplash. Andy Køgl. https://images.unsplash.com/photo-1563538484631-e3a974e4263f?q=80&w=1956&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D. July 19, 2019. Free to use under Unsplash license
           "https://cdn.britannica.com/84/232784-050-1769B477/Siberian-Husky-dog.jpg"] #Husky. Image credit: Siberian Husky. Image. Encyclopædia Britannica. https://www.britannica.com/animal/Siberian-husky#/media/1/542620/267147 No CC license.


#Functions
def open_image(url): #basic function for opening images
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def img_rec():
    while True:
        choice = input("Welcome to Doggo Recommender, we serve to recommend potential dog breeds that may be a good fit for you. Would you like a breed recommendation? (yes, no):")
        if choice == "yes":
            img = random.randint(0,4) #randomization of images
            print("Generating Doggo recommendation...")
            time.sleep(2)
            open_image(puplist[img]) #uploading the image to terminal

            #descriptions of respective dog breeds
            if img == 0:
                print("Samoyeds are friendly, hardworking dogs that have the fluffiest white coat suited for deep winters. These bundles of joys are sure to bring excitement and happiness in your life.")
            if img == 1:
                print("Golden retrievers are known for their friendly attitudes and famous golden coat. These dogs are sturdy but are extremely gentle and kind in nature, and can be a fit for anyone.")
            if img == 2:
                print("Although small, pomeranians are very active, bold, and lively dogs. They have double coats that are suited for cold weather and their cute appearance are definitely something to consider.")
            if img == 3:
                print("Australian Shepherds are large herding dogs that have strikingly beautiful coats ranging from white, yellow, orange, brown, and black. These dogs are intelligent and have a lot of energy to match.")
            if img == 4:
                print("Huskies are known for their endurance and sturdiness especially in the winter. These hardworking dogs have joyous, loving personalities with a hint of mischief, and are sure to bring liveliness to any owner's days.")

        if choice == "no":
            print("Thank you for using Doggo Recommender.")
            break

#Main
img_rec()
