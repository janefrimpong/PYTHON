lucky_num = 5
num = 0
chance = 3
while num < chance:
    luck = int(input("Enter your lucky number :"))
    num += 1
    if luck == lucky_num:
        print("hey buddy!!,you won")
        break
    else:
        print("Dude try again, better luck next time")
