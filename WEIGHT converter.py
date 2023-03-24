weight = int(input("Enter your weight :"))
print("If you wanna convert from pounds into kilogram,type (k)")
print("If you wanna convert kilos into pounds, type (l)")
receive = input("K or L :")
if receive == "k" or receive == "K":
    print("weight in (kg) :", weight * 0.45, "kg")
elif receive == "L" or receive == "l":
    print("weight in pounds :", weight / 0.45, "lb")
else:
    print("please type L or K")