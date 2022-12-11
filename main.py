import os
from pyfiglet import Figlet

# title
f = Figlet(font='slant')
print (f.renderText('PyCLI'))
print("Welcome to PyCLI! Select an action from 1 to 4:\n ")

while True:
    print("1.")
    print("2.")
    print("3.")
    print("4.Exit")

    choice = input(">>> ")
    choice = choice.strip()

    if (choice == "1"):
        print("hi!!!")

    elif(choice == "2"):
        print("i'm gay!!!")

    elif(choice == "3"):
        print("yolo")

    elif(choice == "4"):
        break

    else:
        print("Invalid option, please try again")