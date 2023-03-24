try:
    name=input("Enter your name: ")
    age=int(input("Enter your age : "))
except ValueError:
    print("age must be a number")