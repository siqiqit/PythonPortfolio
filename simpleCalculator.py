#Siqi Tang
#Period 3
#Simple Calculator
#November 19, 2024


#Initialization
def add(num1, num2):
        result = num1 + num2
        print("The result is: " + str(result))

def subtract(num1, num2):
        result = num1 - num2
        print("The result is: " + str(result))

def multiply(num1, num2):
        result = num1 * num2
        print("The result is: " + str(result))

def divide(num1, num2):
        result = num1 / num2
        print("The result is: " + str(result))


#Functions

#Introduction
def simplecalc():
    print("Welcome Preschoolers to Simple Calculator")
    while True:
        print("""1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit""")
        operation = int(input("Enter an operation (1-5): "))



#Addition
        if operation == 1:
            int1= int(input("Enter your first number: "))
            int2= int(input("Enter your second number: "))
            add(int1,int2)

#Subtraction

        if operation == 2:
            int1= int(input("Enter your first number: "))
            int2= int(input("Enter your second number: "))
            subtract(int1,int2)

#Multiplication

        if operation == 3:
            int1= int(input("Enter your first number: "))
            int2= int(input("Enter your second number: "))
            multiply(int1,int2)

#Division

        if operation == 4:
            int1= int(input("Enter your first number: "))
            int2= int(input("Enter your second number: "))
            divide(int1,int2)

#Quit

        if operation == 5:
            print("Thank you for using Simple Calculator")
            break

#Main

simplecalc()
