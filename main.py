from pyfiglet import Figlet

# title
f = Figlet(font='slant')
print(f.renderText('PyCLI'))
print("Welcome to PyCLI! Select an action from 1 to 4:\n ")

while True:
    print("1.About me!")
    print("2.What is PyCLI?")
    print("3.Opinion on Java")
    print("4.Exit")

    choice = input(">>> ")
    choice = choice.strip()

    if (choice == "1"):
        print("Chrono, 20, coding enthusiastic, loves drawing, playing games and of course CODING!")

    elif (choice == "2"):
        print("It's a command-line interface template based on Python, anyone can use the source code!")

    elif (choice == "3"):
        print("no.")

    elif (choice == "4"):
        break

    else:
        print("Invalid option, please try again")
