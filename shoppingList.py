#Siqi Tang
#Period 3
#To-do List
#January 22, 2025


#Init

shopping = []
count = 0

#Functions


def shoppingList():
    global shopping
    global count
    while True:
        try:
            print("Welcome to your grocery shopping list. Please select one of the following options: \n1. View current shopping list \n2. Add item to shopping list\n3. Remove item from shopping list \n4. Sort shopping list alphabetically. \n5. Count the items on shopping list. \n6. Exit.")
            userChoice = int(input("Select a number from 1-6"))


        #1: view

            if userChoice == 1:
                print(shopping)

        #2: add

            if userChoice == 2:
                add = input("What would you like to add onto the list?:")
                shopping.append(add)
                count = count + 1
                print("You have successfully added a task. Your list shopping list is now: " + str(shopping))

        #3: remove

            if userChoice == 3:
                remove = int(input("Select the item number you would like to remove:"))
                shopping.pop(remove - 1)
                count = count - 1
                print("You have successfully removed a task. Your shopping list is now: " + str(shopping))

        #4: sort
            if userChoice == 4:
                shopping.sort()
                print("You have successfully sorted your list. Your shopping list is now: " + str(shopping))

        #5: count
            if userChoice == 5:
                print("You currently have " + str(count) + " items in your shopping list.")

        #6: exit

            if userChoice == 6:
                print("Thank you for visiting your grocery shopping list.")
                break


        except:
            print("ERROR: Please enter a NUMBER 1-6.")



#Main
shoppingList()
