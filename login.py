#Siqi Tang
#Period 3
#Login
#December 4, 2024

#Initialization
#Functions

def login():
    
#Initialization
    valid_username = "BananaBread"
    valid_password = "IsSoYummy!"

#User input
    username=input("Hello, welcome to the Login page. Please enter your username:")
    username = username.upper() #capitalize any input the user puts in, preventing capitalization errors
    password=input("Please enter your password:")
    if username == "BANANABREAD" and password == valid_password:
        print("Welcome back, user! You have logged in.")
    else:
        print("Your username or password is incorrect. Please try again.")


#Main

login()
