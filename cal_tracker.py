dailycal = int(input("Enter your daily calorie goal: "))
done = False
intake = 0

#inputting calories and meals
while not done:
    meal = str(input("Enter meal name (input q to stop):  "))
    if meal == "q":
        done = True
    else:
        cal = int(input("Enter calorie of the meal: "))
        intake += cal

#calculatin net calorie
net = intake - dailycal
if intake == dailycal:
    print ("Your are in maintance")
elif intake > dailycal:
    print (f"{net} calories surplus")
else:
    print (f"{abs(net)} calories in deficit")

    
