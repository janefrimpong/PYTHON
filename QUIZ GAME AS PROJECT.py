print("\t WELCOME TO MY COMPUTER QUIZ!")

playing = input("Do you wanna play? : ")

if playing == "yes" or playing == "YES" or playing == "Yes":
    print("OK let's play then ")
    answer=input("What is the full meaning of CPU? : ")
    if answer=="Central Processing Unit" or answer=="CENTRAL PROCESSING UNIT" or answer=="central processing unit":
        print("Correct")
    else:
        print("Incorrect")
    answer = input("What is the full meaning of RAM? : ")
    if answer == "RANDOM ACCESS MEMORY" or answer == "Random Access Memory" or answer == "random access memory":
        print("Correct")
    else:
        print("Incorrect")

    answer = input("RAM is volatile, True /False? : ")
    if answer == "TRUE" or answer == "True" or answer == "true":
        print("Correct")
    else:
        print("Incorrect")

    answer = input("I take the name of the class, Who am I? : " )
    if answer == "CONSTRUCTOR " or answer == "Constructor" or answer == "constructor":
        print("Correct")
    else:
        print("Incorrect")

    answer = input("I am created when an object is instantiated, Who am I? : ")
    if answer == "CONSTRUCTOR" or answer == "constructor" or answer == "constructor":
        print("Correct")
    else:
        print("Incorrect")

    answer = input("An object is an instance of a class  : ")
    if answer == "YES" or answer == "Yes" or answer == "yes":
        print("Correct")
    else:
        print("Incorrect")
else:
    print("Quit")


