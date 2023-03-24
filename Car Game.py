offer = input(">")
if offer == "help" or offer == "Help" or offer == "HELP":
    print("""
    1.start-This starts the car
    2.Stop-This stops the car
    3. Quit- This exits the game
    """)

    option = int(input(">"))
    if option == 1:
        print("Car started...ready to go?")
    elif option == 2:
        print("Car stopped")
    elif option == 3:
        print("are you sure you wanna quit?")
    else:
        print("I don't understand the message")
else:
    print("I don't understand")
